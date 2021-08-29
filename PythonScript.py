import requests
import scrapy

#setting url variable to given website
url = 'https://brickset.com/sets/year-1998'

headers2 = {'User-Agent':'Mobile'}
#for status code
r = requests.get(url, headers=headers2)
#for header
h = requests.head(url)
#printing status code, 200 means ok, 404 means not found
print("Status code: ", r.status_code)
#printing header
print("__________HEADER__________")
print(headers2)
#for loop to print line by line, formatting
for x in h.headers:
    print(x, ":", h.headers[x])
print("_________End of header_________")





class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = [url]

    def parse(self, response):
        css_selector='img'
        for x in response.css(css_selector):
            newsel='@src'
            yield{
                'Image Link': x.xpath(newsel).extract_first(),
            }


#recurse
        Page_Selector = '.next a ::attr(href)'
        next_page = response.css(Page_Selector).extract_first()
        if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )