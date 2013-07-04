# Scrapy settings for article_spider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'article_spider'

SPIDER_MODULES = ['article_spider.spiders']
NEWSPIDER_MODULE = 'article_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'article_spider (+http://www.yourdomain.com)'
