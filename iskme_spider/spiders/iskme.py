# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class IskmeSpider(CrawlSpider):
    name = "iskme"
    allowed_domains = ["iskme.org", "web.archive.org"]
    start_urls = ['http://web.archive.org/web/20160516183059/http://www.iskme.org/']
    rules = (Rule(LinkExtractor(allow=('iskme'), deny=('iskme.org/archive'), unique=True, restrict_css=('div:not(#wm-ipp)'), deny_domains=('google.com', 'facebook.com', 'twitter.com', 'oercommons.org')), callback='parse_page', follow=True),)

    def parse_page(self, response):

        if 'iskme.org' in response.url:
            path = response.url.split('/')
        	# main_body = response.xpath('//div/*[@class="make-it-center"]').extract_first()

            yield {
            	'url': response.url,
            	# 'html': response.body,
                'path': path
            	# 'main_body': main_body
            }
