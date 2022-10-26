import scrapy

class Ayomain_Spider(scrapy.Spider):
    name = 'ayomain'
    start_urls = ["https://store.playstation.com/en-id/category/29696e1b-a942-4832-935d-ebd11b163263/1"]
    

    def parse(self, response):
        url = response.url
        
        for i in range(1,46):
            yield scrapy.Request(url=url+str(i), callback=self.parse_details)
    def parse_details(self, response):
        for text in response.css(".psw-product-tile__details"):
            yield{
                "title":text.css(".psw-t-body::text").get(),
                "price":text.css(".psw-m-r-3::text").get()}
        pass