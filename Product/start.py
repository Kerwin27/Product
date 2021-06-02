from scrapy import cmdline

cmdline.execute("scrapy crawl ProductSpider --nolog -o Product.csv".split())
