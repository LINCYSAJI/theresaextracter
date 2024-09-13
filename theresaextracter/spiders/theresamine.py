import scrapy
from theresaextracter.items import TheresaextracterItem

class TheresamineSpider(scrapy.Spider):
    name = "theresamine"
    allowed_domains = ["www.mytheresa.com"]

    start_urls = ["https://www.mytheresa.com/int_en/men/shoes.html "]

    product_start = 0

    product_end = 1000

    def parse(self, response):

        products = response.xpath('//div[@class="list__container"]')

        for product in products:

            if self.product_start < self.product_end:

                items = product.xpath('.//a[@class="item__link"]/@href').get()
                if items:

                    yield response.follow(items, callback=self.parse_product)

                    self.product_start += 1

                else:

                    return
        if self.product_start < self.product_end:

            next_page = response.xpath(
                '//a[containes(@class,"action next")]/@href'
            ).get()

            if next_page:

                yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response):

        item=TheresaextracterItem()

        item['breadcrumbs']=response.xpath(
                '//div[@class="breadcrumbs"]/a/text()'
            ).getall()
        item['image_url']=response.xpath(
                 '//img[@class=""item__images__image"]/@src'
             ).get(),
        item['brand']=response.xpath(
                '//div[@class="item__info__header__designer "]/text()'
            ).get(),
        item['product_name']=response.xpath(
                 '//div[@class="item__info__name"]/a/text()'
             ).get(),
        item['listing_price']=response.xpath(
                 '///span[@class="pricing__prices__value pricing__prices__value--original"/span[@class="pricing__prices__price"]/text()'
             ).get(),
        item['offer_price']=response.xpath(
                 '//span[@class="pricing__prices__value pricing__prices__value--discount"]/span[@class="pricing__prices__price"/text()'
            ).get(),
        item['discount']=response.xpath(
                 '//div[@class="pricing__info"]/span[@class="pricing__info__percentage"/text()'
             ).get(),
        item['product_id']=response.xpath(
                 '//div[@class="accordion__body__content"]//ul/li[last()]/text()'
             ),
        item['sizes']=response.xpath(
                 '//div[@class="item__sizes"]/span[@class="item__sizes__size"]/text()'
             ).getall(),
        item['description']= response.xpath(
                 '//div[@class="accordion__body__content"]/p/text()'
            ).get(),
        item['other_images']=response.xpath(
                 '//div[contains(@class,"zoomermodal__main")]/img/@src'
             ),
        yield item



        # yield {
        #     "breadcrumbs": response.xpath(
        #         '//div[@class="breadcrumbs"]/a/text()'
        #     ).getall(),
        #     "image_url": response.xpath(
        #         '//img[@class=""item__images__image"]/@src'
        #     ).get(),
        #     "brand": response.xpath(
        #         '//div[@class="item__info__header__designer "]/text()'
        #     ).get(),
        #     "product_name": response.xpath(
        #         '//div[@class="item__info__name"]/a/text()'
        #     ).get(),
        #     "listing_price": response.xpath(
        #         '///span[@class="pricing__prices__value pricing__prices__value--original"/span[@class="pricing__prices__price"]/text()'
        #     ).get(),
        #     "offer_price": response.xpath(
        #         '//span[@class="pricing__prices__value pricing__prices__value--discount"]/span[@class="pricing__prices__price"/text()'
        #     ).get(),
        #     "discount": response.xpath(
        #         '//div[@class="pricing__info"]/span[@class="pricing__info__percentage"/text()'
        #     ).get(),
        #     "product_id": response.xpath(
        #         '//div[@class="accordion__body__content"]//ul/li[last()]/text()'
        #     ),
        #     "sizes": response.xpath(
        #         '//div[@class="item__sizes"]/span[@class="item__sizes__size"]/text()'
        #     ).getall(),
        #     "description": response.xpath(
        #         '//div[@class="accordion__body__content"]/p/text()'
        #     ).get(),
        #     "other_images": response.xpath(
        #         '//div[contains(@class,"zoomermodal__main")]/img/@src'
        #     ),
        # }
