# -*- coding = utf-8 -*-
# @Time: 2024/11/11 16:03
# @Author: Zhihang Yi
# @File: run_spiders.py
# @Software: PyCharm

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from DataSource.spiders.flightradar24 import Flightradar24Spider


def run_spiders():
    # 配置项目的环境设定。
    process = CrawlerProcess(get_project_settings())
    # 开始爬虫。
    process.crawl(Flightradar24Spider)
    # 阻塞式启动爬虫。
    process.start()


if __name__ == '__main__':
    run_spiders()
