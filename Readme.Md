This script crawl-scrape all properties that sold in recent 7 days on price over $750000 in 52 states of USA from realtor.com.
The script fetch data from its API and and drop those listings that don't have buyer party email. 

The script extracting the following fields from each listing:
seller_represented_name
seller_represented_email
seller_rep_comp_name
seller_represented_company_email
            
buyer_rep_name
buyer_rep_email
buyer_rep_link
buyer_rep_company

            
property_url
list_date
last_sold_date
list_price
last_sold_price
city
state
postal_code
primary_photo


This is script is build in python scrapy framework.

Requirements: Python 3 +

Required dependencies:
scrapy
pandas

OPEN CMD in project path scrapy.cfg and Install Requirements by:
pip install -r requirements.txt


How to Run the program:
In the same CMD PATH: scrapy crawl sold -o output_file_name.csv

#############################################################################################




