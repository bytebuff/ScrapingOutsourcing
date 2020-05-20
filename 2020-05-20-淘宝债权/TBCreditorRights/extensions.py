import scrapy
import time, redis
from scrapy import signals
from scrapy.exceptions import DontCloseSpider


class SpiderRedisExensions(object):

    def __init__(self, crawler):
        self.crawler = crawler

    @classmethod
    def from_crawler(cls, crawler):

        # 实例化扩展对象
        ext = cls(crawler)

        # 将扩展对象连接到信号， 将signals.spider_idle 与 spider_idle() 方法关联起来。
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(ext.spider_idle, signal=signals.spider_idle)

        # return the extension object
        return ext

    def spider_opened(self, spider):
        print("opened spider %s redis spider Idle, Continuous idle limit： %d", spider.name, self.idle_number)

    def spider_closed(self, spider):
        print("closed spider %s, idle count %d , Continuous idle count %d",
                    spider.name, self.idle_count, len(self.idle_list))

    def next_req(self):
        redis_cli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0, decode_responses=True)
        url = str(redis_cli.blpop('tbcr')[1])
        print(url)
        return scrapy.Request(url)

    def spider_idle(self, spider):

        request = self.next_req()
        if request:
            self.crawler.engine.schedule(request, self)
        else:
            time.sleep(2)
        raise DontCloseSpider