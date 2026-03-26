"""Scrapy settings for the realtor_listings project.

Configures the bot name, spider module locations, robots.txt behaviour,
and the item pipeline used to filter results.
"""

BOT_NAME = 'realtor_listings'

SPIDER_MODULES = ['realtor_listings.spiders']
NEWSPIDER_MODULE = 'realtor_listings.spiders'

# Disabled because the spider uses the API directly, not HTML pages
ROBOTSTXT_OBEY = False

# Filter items through BuyerEmailPipeline to drop listings without buyer email
ITEM_PIPELINES = {
   'realtor_listings.pipelines.BuyerEmailPipeline': 300,
}
