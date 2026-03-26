# Scrapy settings for realtor_listings project

BOT_NAME = 'realtor_listings'

SPIDER_MODULES = ['realtor_listings.spiders']
NEWSPIDER_MODULE = 'realtor_listings.spiders'

# Disabled because the spider uses the API directly, not HTML pages
ROBOTSTXT_OBEY = False

# Filter items through BuyerEmailPipeline to drop listings without buyer email
ITEM_PIPELINES = {
   'realtor_listings.pipelines.BuyerEmailPipeline': 300,
}
