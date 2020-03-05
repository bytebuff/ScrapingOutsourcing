from scrapy.commands import ScrapyCommand

class Command(ScrapyCommand):

    requires_project = True

    def short_desc(self):
        return "Crawl Spiders"

    def run(self, args, opts):

        # 读取每个爬虫名字
        spnames = self.crawler_process.spider_loader.list()
        for spname in spnames:
            self.crawler_process.crawl(spname)
        self.crawler_process.start()
