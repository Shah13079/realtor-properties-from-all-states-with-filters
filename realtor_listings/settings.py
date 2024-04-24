# Scrapy settings for realtor_listings project

BOT_NAME = 'realtor_listings'

SPIDER_MODULES = ['realtor_listings.spiders']
NEWSPIDER_MODULE = 'realtor_listings.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# DOWNLOAD_DELAY = 1
# DOWNLOADER_MIDDLEWARES = {'scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware': 610}
# # enable Zyte Proxy
# ZYTE_SMARTPROXY_ENABLED = True
# # the APIkey you get with your subscription
# ZYTE_SMARTPROXY_APIKEY = '743756a191f04b87b2de9714a33a65e1'


ITEM_PIPELINES = {
   'realtor_listings.pipelines.BuyerEmailPipeline': 300,
}

