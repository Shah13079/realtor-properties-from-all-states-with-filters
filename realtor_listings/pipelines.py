"""Item pipelines for filtering scraped listings."""

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class BuyerEmailPipeline:
    """Drop listings that do not have a buyer representative email.

    Only items with a non-empty ``buyer_rep_email`` field are passed
    through; all others are discarded so the output contains only
    actionable leads.
    """

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('buyer_rep_email'):
            return item
        else:
            raise DropItem(f"Missing buyer representative email in {item}")
