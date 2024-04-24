## Disclaimer
This script is intended for educational purposes only. There is no intention to harm or overload the targeted website. The script is designed to scrape publicly available data using appropriate techniques to avoid causing any downtime for the website.

---

### Overview
This script scrapes all properties sold in the last 7 days with prices over $750,000 across all 50 states of the USA from realtor.com. The script fetches data from the realtor.com API and filters out listings that do not have a buyer party email.

---

### Extracted Fields
- seller_represented_name
- seller_represented_email
- seller_rep_comp_name
- seller_represented_company_email
- buyer_rep_name
- buyer_rep_email
- buyer_rep_link
- buyer_rep_company
- property_url
- list_date
- last_sold_date
- list_price
- last_sold_price
- city
- state
- postal_code
- primary_photo

---

### Framework
This script is built using the Python Scrapy framework.

---

### Requirements
- Python 3 +

### Required Dependencies
- scrapy
- pandas

---

### Installation
To install the required dependencies, open CMD in the project path (where `scrapy.cfg` is located) and run:
```
pip install -r requirements.txt
```
---

### Run program

Navigate to the project directory in CMD and run the following command:
```
scrapy crawl sold -o output_file_name.csv
```

Regards
Hussain (Mrpythonic)
