# -*- coding: utf-8 -*-
import scrapy,re
from Cnblogs.items import CnblogsItem

class CnblogsSpiderSpider(scrapy.Spider):
    name = 'cnblogs_spider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/']

    def parse(self, response):
        datas = response.xpath('//div[@id="post_list"]//div[@class="post_item"]')
        for data in datas:
            item = CnblogsItem()
            item['title'] = data.xpath(".//h3/a/text()").extract_first()
            # print(title)
            item['author'] = data.xpath('.//div[@class="post_item_foot"]/a/text()').extract_first()
            item['author_url'] = data.xpath(".//div[@class='post_item_foot']/a/@href").extract_first()
            Introduction = ''.join(data.xpath(".//p[@class='post_item_summary']/text()").extract())
            item["Introduction"] = re.sub(r'\s','',Introduction)
            reading = ''.join(data.xpath(".//div[@class='post_item_foot']//span[@class='article_view']/a/text()").extract_first())
            item["reading"] = re.sub(r'\s','',reading)
            comments = ''.join(data.xpath('.//div[@class="post_item_foot"]/span[@class="article_comment"]/a/text()').extract())
            item['comments'] = re.sub(r'\s','',comments)
            Release_time = ''.join(data.xpath(".//div[@class='post_item_foot']/text()").extract())
            item['Release_time'] = re.sub("[\r\n]",'',Release_time).strip()
            item['origin_url'] = data.xpath(".//h3/a/@href").extract_first()
            yield item
        next_url = response.xpath("//div[@class='pager']//a/@href").extract()[-1]
        # print(next_url)
        yield scrapy.Request(url=response.urljoin(next_url),callback=self.parse)