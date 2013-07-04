# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from article_spider.items import Hadith
import codecs

class HadithSpider(BaseSpider):
    name = "Hadith"
    allowed_domains = ["valiasr-aj.com"]
    start_urls = ["http://www.valiasr-aj.com/fa/page.php?bank=maghalat&id=139"]

    def parse(self, response):
        items = []
        hxs = HtmlXPathSelector(response)
        ps = hxs.select("//p")      # select all lines
        classes = [p.select("@class").extract() for p in ps]
        classes = [(u'none' if len(c) == 0 else c[0]) for c in classes]
        len_ps = len(ps)
        self.log('equal len: %d == %d' % (len_ps, len(classes)))
        self.log('classes: %s' % repr(classes))
        ind = 0
        while (ind < len_ps - 1):
            item = Hadith()
            arabi_txt = []
            farsi_txt = []
            refs = []
            while (classes[ind] == u'arabi'):
                arabi_txt.append(ps[ind].select("span/text()").extract()[0])
                if (ind < len_ps - 1):
                    ind = ind + 1
            while (classes[ind] == u'tarjome'):
                farsi_txt.append(ps[ind].select("span/text()").extract()[0])
                if (ind < len_ps - 1):
                    ind = ind + 1
            while (classes[ind] == u'MsoFootnoteText'):
                refs.append(ps[ind].select("span/text()").extract()[0])
                if (ind < len_ps - 1):
                    ind = ind + 1
            if (len(farsi_txt) > 0 and len(arabi_txt) > 0):
                item['arabi'] = u'\n'.join(arabi_txt).encode('utf-8')
                item['farsi'] = u'\n'.join(farsi_txt).encode('utf-8')
                item['refs'] = u'\n'.join(refs).encode('utf-8')
                items.append(item)
            ind = ind + 1
        return items
