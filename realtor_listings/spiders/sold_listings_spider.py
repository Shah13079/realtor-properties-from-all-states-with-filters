
import scrapy
from ..utilities import property_query, req_headers , sold_listing_query
import json
import pandas as pd


class SoldListingsSpider(scrapy.Spider):
    name = 'sold'
    allowed_domains = ['www.realtor.com']
    
    def start_requests(self):
        page_num = 1
        offset = 0
        total_pages = 0
        #Reading states names from excel file
        df = pd.read_excel(r'states.xlsx', )
        for index, row in df.iterrows():
            state=row['states']
            code = row['state_code']
            state,code=state.strip(),code.strip()

        
            yield scrapy.Request(
                url = "https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(sold_listing_query(state,page_num,offset,code)),
                callback=self.parse_page,
                method="POST",
                dont_filter=True,

                meta={
                    "state_name":state,
                    "state_code":code,
                    "page_num":page_num,
                    "offset":offset,
                    "total_pages":total_pages
                }
                ,
                headers = req_headers
                        )
        

    def parse_page(self, response):
        page_num = response.request.meta['page_num']
        offset = response.request.meta['offset']
        total_pages = response.request.meta['total_pages']
        state_name = response.request.meta['state_name']
        state_code = response.request.meta['state_code']

        json_response = json.loads(response.body)
        total_count = json_response.get("data").get('home_search').get("total")
        
        # how much total pages to search
        pages_calculation = (int(total_count)//42)+1
        page_listings = json_response.get("data").get('home_search').get("results")
        # Iterate over each listing
        for property in page_listings:
            property_id = property.get('property_id')
            yield scrapy.Request(
                url = "https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta",
                body=json.dumps(property_query(property_id)),
                callback=self.parse_property_page,
                method="POST",
                headers= req_headers
                 )

        page_num+=1
        offset+=42
        total_pages+=1

        if total_pages < pages_calculation :
            yield scrapy.Request(
                url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(sold_listing_query(state_name,page_num,offset,state_code)),
                callback=self.parse_page,
                dont_filter=True,
                method="POST",
                headers= req_headers,
                meta={
                    "state_name":state_name,
                    "state_code":state_code,
                    "page_num":page_num,
                    "offset":offset,
                    "total_pages":total_pages
                } 
            )

        

    def parse_property_page(self, response):
        primary_photo = buyer_details = buyer_rep_email = ' '
        buyer_rep_name = buyer_rep_link = buyer_rep_company=''
        seller_rep_name = seller_rep_email = seller_rep_comp_name = seller_rep_comp_email = ''
        home_data = property_url = list_date = last_sold_date = ''
        last_sold_price = list_price = city = state = postal = ''
         

        json_response = json.loads(response.body)
        home_data = json_response.get("data", {}).get("home", {})

        try:
            adv_details = home_data.get("advertisers")[0]
            buyer_details = home_data.get("buyers")[0]
        except (TypeError,AttributeError):
            pass
        
        
        #seller information
        seller_rep_name = adv_details.get('name')
        seller_rep_email = adv_details.get("email")
        seller_rep_comp_name = adv_details.get("office").get("name")
        seller_rep_comp_email = adv_details.get("office").get("email")
       
        
        #buyer information
        buyer_rep_name = buyer_details.get("name")
        buyer_rep_email = buyer_details.get("email")
        buyer_rep_link = buyer_details.get("href")
        buyer_rep_company = buyer_details.get("office").get("name")
       

        #property details
        property_url = home_data.get("href")
        list_date = home_data.get("list_date")
        last_sold_date = home_data.get("last_sold_date")
        last_sold_price = home_data.get("last_sold_price")
        list_price = home_data.get("list_price")
    

        #primary photo
        primary_photo_small = home_data.get("primary_photo").get("href")
        primary_photo = primary_photo_small.replace('.jpg','-w1024_h768_x1')+'.jpg'
     
        
        #location
        location = home_data.get('location').get('address')
        city = location.get("city")
        state = location.get("state_code")
        postal = location.get("postal_code")
      
       

        yield{
            # Seller information
            'seller_represented_name':seller_rep_name,
            'seller_represented_email':seller_rep_email,
            'seller_rep_comp_name':seller_rep_comp_name,
            'seller_represented_company_email':seller_rep_comp_email,
            # Buyer information
            'buyer_rep_name':buyer_rep_name,
            'buyer_rep_email':buyer_rep_email,
            'buyer_rep_link':buyer_rep_link,
            'buyer_rep_company':buyer_rep_company,

            # property details
            "property_url":property_url,
            "list_date":list_date,
            "last_sold_date":last_sold_date,
            "list_price":list_price,
            "last_sold_price":last_sold_price,
            "city":city,
            "state":state,
            "postal_code":postal,
            "primary_photo":primary_photo

            }


    
        
            
