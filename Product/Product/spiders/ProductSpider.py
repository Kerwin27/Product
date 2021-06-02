from urllib.parse import urlencode

import scrapy
from scrapy import Request

from Product.items import ProductItem


class ProductspiderSpider(scrapy.Spider):
    name = 'ProductSpider'
    headers = {
        'user-agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/70.0.3538.25Safari/537.36ore/1.70.3870.400QQBrowser/10.8.4405.400'
    }

    def start_requests(self):

        url = 'https://search.jd.com/search?keyword=%E5%8D%8E%E4%B8%BA&qrst=1&wq=%E5%8D%8E%E4%B8%BA&ev=559_101701'
        yield Request(url, headers=self.headers)

    def parse(self, response, **kwargs):
        item = ProductItem()
        Infros = response.xpath('//*[@class="gl-warp clearfix"]/li')
        count = 0
        for Info in Infros:
            item['Url'] = 'http:' + Info.xpath('//*[@class="p-name p-name-type-2"]/a/@href').extract()[count]
            count += 1
            yield item
