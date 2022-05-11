This script crawl-scrape all properties that sold in recent 7 days on price over $750000 in 52 states of USA from realtor.com.
The script fetch data from its API and and drop those listings that don't have buyer party email. 

**The script extracting the following fields from each listing:**<br>
1) seller_represented_name
2) seller_represented_email
3) seller_rep_comp_name
4) seller_represented_company_email
            
5) buyer_rep_name
6) buyer_rep_email
7) buyer_rep_link
8) buyer_rep_company

            
9) property_url
10) list_date
11) last_sold_date
13) list_price
14) last_sold_price
15) city
16) state
17) postal_code
18) primary_photo


This is script is build in python scrapy framework.

Requirements: Python 3 +

**Required dependencies:**<br>
scrapy
pandas

**OPEN CMD in project path scrapy.cfg and Install Requirements by:** <br>
pip install -r requirements.txt


**How to Run the program:**<br>
In the same CMD PATH: scrapy crawl sold -o output_file_name.csv

#############################################################################################




