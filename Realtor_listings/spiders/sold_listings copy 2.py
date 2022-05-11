
import scrapy
from ..utilities import property_query, req_headers , sold_items_with_no_state
import json
import pandas as pd


class SoldListingsSpider(scrapy.Spider):
    name = 'sold'

    allowed_domains = ['www.realtor.com']

    
    def start_requests(self):
        #Reading states from excel file
        page_num = 1
        offset = 0
        total_pages = 0

        df = pd.read_excel(r'states.xlsx', )
        for index, row in df.iterrows():
            state=row['states']
            code = row['state_code']
            state,code=state.strip(),code.strip()

        
                
            yield scrapy.Request(
                url = "https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(sold_items_with_no_state(state,page_num,offset,code)),
                callback=self.parse_page,
                method="POST",
                dont_filter=True,

                meta={
                    "state_location":state,
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

        state_location = response.request.meta['state_location']
        state_code = response.request.meta['state_code']

        json_response = json.loads(response.body)
        total_count = json_response.get("data").get('home_search').get("total")

        #count total pages
        
        pages_calculation = (int(total_count)//42)+1
        
        
     
        page_listings = json_response.get("data").get('home_search').get("results")

        print("State:",state_location)
        print("total_count:",total_count)
        

        for property in page_listings:
            property_id = property.get('property_id')

            yield scrapy.Request(
                url = "https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta",
                body=json.dumps(property_query(property_id)),
                callback=self.parse_property_page,
                method="POST",
                headers= req_headers,
               
              
                 )

    
        page_num+=1
        offset+=42
        total_pages+=1

        if total_pages < pages_calculation :
        
            yield scrapy.Request(
                url="https://www.realtor.com/api/v1/hulk_main_srp?client_id=rdc-x&schema=vesta",
                body=json.dumps(sold_items_with_no_state(state_location,page_num,offset,state_code)),
                callback=self.parse_page,
                dont_filter=True,
                method="POST",
                headers= req_headers,
                meta={
                    "state_location":state_location,
                    "state_code":state_code,
                    "page_num":page_num,
                    "offset":offset,
                    "total_pages":total_pages
                } 
            )

        

            
    def parse_property_page(self, response):
        primary_photo=buyer_details=buyer_rep_email=buyer_rep_name=buyer_rep_link=buyer_rep_company=''
        seller_rep_name = seller_rep_email = seller_rep_comp_name = seller_rep_comp_email = ''
        prop_details = property_url = list_date = last_sold_date = last_sold_price = list_price = ''
        prop_city = prop_state =prop_postal =''
        json_response = json.loads(response.body)
        
        try:
            adv_details = json_response.get("data").get("home").get("advertisers")[0]
            buyer_details = json_response.get("data").get("home").get("buyers")[0]
        except (TypeError,AttributeError):
            pass
        
        try:
            #seller information
            seller_rep_name = adv_details.get('name')
            seller_rep_email = adv_details.get("email")
            seller_rep_comp_name = adv_details.get("office").get("name")
            seller_rep_comp_email = adv_details.get("office").get("email")
        except (UnboundLocalError,AttributeError):
            pass
        
        #buyer information
        try:
            buyer_rep_name = buyer_details.get("name")
            buyer_rep_email = buyer_details.get("email")
            buyer_rep_link = buyer_details.get("href")
            buyer_rep_company = buyer_details.get("office").get("name")
        except (UnboundLocalError,AttributeError):
            pass

        #property details
        try:
            prop_details = json_response.get("data").get("home")
            property_url = prop_details.get("href")
            list_date = prop_details.get("list_date")
            last_sold_date = prop_details.get("last_sold_date")
            last_sold_price = prop_details.get("last_sold_price")
            list_price = prop_details.get("list_price")
        except (UnboundLocalError,AttributeError):
            pass

        #primary photo
        try:
            primary_photo_low = json_response.get('data').get("home").get("primary_photo").get("href")
            primary_photo = primary_photo_low.replace('.jpg','-w1024_h768_x1')+'.jpg'
        except (AttributeError):pass

        #location
        try:
            prop_city = json_response.get('data').get("home").get("location").get("address").get("city")
            prop_state = json_response.get('data').get("home").get("location").get("address").get("state_code")
            prop_postal = json_response.get('data').get("home").get("location").get("address").get("postal_code")
        except (UnboundLocalError,AttributeError):
            pass
       

        yield{
            'seller_represented_name':seller_rep_name,
            'seller_represented_email':seller_rep_email,
            'seller_rep_comp_name':seller_rep_comp_name,
            'seller_represented_company_email':seller_rep_comp_email,
            
            'buyer_rep_name':buyer_rep_name,
            'buyer_rep_email':buyer_rep_email,
            'buyer_rep_link':buyer_rep_link,
            'buyer_rep_company':buyer_rep_company,

            
            "property_url":property_url,
            "list_date":list_date,
            "last_sold_date":last_sold_date,
            "list_price":list_price,
            "last_sold_price":last_sold_price,
            "city":prop_city,
            "state":prop_state,
            "postal_code":prop_postal,
            "primary_photo":primary_photo


            }


    
        
            
