"""Spider for scraping sold property listings from Realtor.com."""

import json
import logging
from pathlib import Path

import scrapy
import pandas as pd

from ..utilities import property_query, req_headers, sold_listing_query, RESULTS_PER_PAGE

logger = logging.getLogger(__name__)

# Path to the Excel file containing US state names and codes
STATES_FILE = Path(__file__).resolve().parent.parent.parent / 'states.xlsx'


class SoldListingsSpider(scrapy.Spider):
    """Crawl sold listings across all 50 US states via the Realtor.com API.

    For each state listed in ``states.xlsx``, the spider queries the search
    API for recently sold properties above a price threshold, then fetches
    the full property detail page for each result to extract seller/buyer
    representative contact information.
    """

    name = 'sold'
    allowed_domains = ['www.realtor.com']

    def start_requests(self):
        """Generate initial search requests for every state in the spreadsheet."""
        page_num = 1
        offset = 0
        total_pages = 0

        df = pd.read_excel(STATES_FILE)
        for index, row in df.iterrows():
            state = row['states']
            state_code = row['state_code']
            state, state_code = state.strip(), state_code.strip()

            yield scrapy.Request(
                url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(sold_listing_query(state, page_num, offset, state_code)),
                callback=self.parse_page,
                method="POST",
                dont_filter=True,
                meta={
                    "state_name": state,
                    "state_code": state_code,
                    "page_num": page_num,
                    "offset": offset,
                    "total_pages": total_pages
                },
                headers=req_headers
            )

    def parse_page(self, response):
        """Parse a search results page and request detail pages for each listing."""
        page_num = response.request.meta['page_num']
        offset = response.request.meta['offset']
        total_pages = response.request.meta['total_pages']
        state_name = response.request.meta['state_name']
        state_code = response.request.meta['state_code']

        json_response = json.loads(response.body)
        total_count = json_response.get("data").get('home_search').get("total")

        pages_calculation = (int(total_count) // RESULTS_PER_PAGE) + 1
        page_listings = json_response.get("data").get('home_search').get("results")

        for listing in page_listings:
            property_id = listing.get('property_id')
            yield scrapy.Request(
                url="https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta",
                body=json.dumps(property_query(property_id)),
                callback=self.parse_property_page,
                method="POST",
                headers=req_headers
            )

        page_num += 1
        offset += RESULTS_PER_PAGE
        total_pages += 1

        if total_pages < pages_calculation:
            yield scrapy.Request(
                url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(sold_listing_query(state_name, page_num, offset, state_code)),
                callback=self.parse_page,
                dont_filter=True,
                method="POST",
                headers=req_headers,
                meta={
                    "state_name": state_name,
                    "state_code": state_code,
                    "page_num": page_num,
                    "offset": offset,
                    "total_pages": total_pages
                }
            )

    def parse_property_page(self, response):
        """Extract seller/buyer details and property metadata from a detail response."""
        primary_photo = buyer_details = buyer_rep_email = ' '
        buyer_rep_name = buyer_rep_link = buyer_rep_company = ''
        seller_rep_name = seller_rep_email = seller_rep_comp_name = seller_rep_comp_email = ''
        home_data = property_url = list_date = last_sold_date = ''
        last_sold_price = list_price = city = state = postal_code = ''

        json_response = json.loads(response.body)
        home_data = json_response.get("data", {}).get("home", {})

        try:
            advertiser_details = home_data.get("advertisers")[0]
            buyer_details = home_data.get("buyers")[0]
        except (TypeError, AttributeError):
            logger.warning("Failed to extract advertiser/buyer details for property: %s",
                           response.url)
            return

        # Seller information
        seller_rep_name = advertiser_details.get('name')
        seller_rep_email = advertiser_details.get("email")
        seller_rep_comp_name = advertiser_details.get("office").get("name")
        seller_rep_comp_email = advertiser_details.get("office").get("email")

        # Buyer information
        buyer_rep_name = buyer_details.get("name")
        buyer_rep_email = buyer_details.get("email")
        buyer_rep_link = buyer_details.get("href")
        buyer_rep_company = buyer_details.get("office").get("name")

        # Property details
        property_url = home_data.get("href")
        list_date = home_data.get("list_date")
        last_sold_date = home_data.get("last_sold_date")
        last_sold_price = home_data.get("last_sold_price")
        list_price = home_data.get("list_price")

        # Primary photo
        primary_photo_small = home_data.get("primary_photo").get("href")
        primary_photo = primary_photo_small.replace('.jpg', '-w1024_h768_x1') + '.jpg'

        # Location
        location = home_data.get('location').get('address')
        city = location.get("city")
        state = location.get("state_code")
        postal_code = location.get("postal_code")

        yield {
            # Seller information
            'seller_represented_name': seller_rep_name,
            'seller_represented_email': seller_rep_email,
            'seller_rep_comp_name': seller_rep_comp_name,
            'seller_represented_company_email': seller_rep_comp_email,
            # Buyer information
            'buyer_rep_name': buyer_rep_name,
            'buyer_rep_email': buyer_rep_email,
            'buyer_rep_link': buyer_rep_link,
            'buyer_rep_company': buyer_rep_company,
            # Property details
            "property_url": property_url,
            "list_date": list_date,
            "last_sold_date": last_sold_date,
            "list_price": list_price,
            "last_sold_price": last_sold_price,
            "city": city,
            "state": state,
            "postal_code": postal_code,
            "primary_photo": primary_photo
        }
