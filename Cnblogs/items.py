# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class CnblogsItem(Item):
    # 标题
    title = Field()
    # 作者
    author = Field()
    # 简介
    Introduction = Field()
    # 阅读
    reading = Field()
    # 评论
    comments = Field()
    # 文章的详细页链接
    origin_url = Field()
    # 发布时间
    Release_time = Field()
    # 博主的主页链接
    author_url = Field()
