import scrapy


class StrainSpider(scrapy.Spider):
	name = "strain2"
	start_urls = [
		'https://www.weedsta.com/strains',
	]


	def parse(self, response):
		for strains in response.css('div.fl_list'):
			yield {
				'Strain' : strains.css('div:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)::text').get(),
				'Type' : strains.css('div:nth-child(1) > div:nth-child(2) > p:nth-child(2)::text').get(),
				'TGK' : strains.css('div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3)::text').get(),
				'About' : strains.css('div:nth-child(3) > p:nth-child(1)::text').get(),
				'Feeling' : strains.css('div.feeling > .attribute::text').getall(),
				'Medical' : strains.css('div.medical > .attribute::text').getall(),
	
			}

		NEXT_PAGE_SELECTOR = '.more_btn1 > a:nth-child(1)::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).get()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page),callback=self.parse)


		


