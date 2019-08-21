from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerRunner

class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return 'scrapy crawlall'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for name in spider_list:
            self.crawler_process.crawl(name)
        self.crawler_process.start()


