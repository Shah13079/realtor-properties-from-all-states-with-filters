# Realtor.com Sold Listings Scraper

A Scrapy-based web scraper that collects recently sold property listings across all 50 US states from Realtor.com. The scraper targets high-value properties (above a configurable price threshold) sold within a recent time window, and extracts detailed seller/buyer representative contact information alongside property data.

## Disclaimer

This project is intended for educational purposes only. It scrapes publicly available data using rate-limited requests to avoid causing any disruption to the target website.

## Features

- Scrapes sold property listings from all 50 US states via the Realtor.com API
- Filters by minimum sale price and recency (configurable)
- Extracts seller and buyer representative contact details
- Retrieves property metadata including pricing, dates, location, and photos
- Filters out listings missing buyer representative email via a custom pipeline
- Paginates automatically through all result pages per state
- Outputs data to CSV (or any Scrapy-supported format)

## Tech Stack

- **Python 3.6+**
- **Scrapy** -- asynchronous web scraping framework
- **Pandas** -- reads the state list from an Excel file
- **itemadapter** -- normalizes item access in pipelines

## Architecture / Data Flow

1. **State iteration**: The spider reads `states.xlsx` to get all 50 US state names and codes.
2. **Search API requests**: For each state, a GraphQL query is sent to the Realtor.com search API requesting sold listings matching the price and date filters.
3. **Pagination**: The spider calculates total result pages and issues follow-up requests as needed.
4. **Property detail requests**: For each listing in the search results, a second GraphQL query fetches the full property detail page (advertiser/buyer contact info).
5. **Data extraction**: The spider extracts seller rep, buyer rep, property details, and location fields from the detail response.
6. **Pipeline filtering**: The `BuyerEmailPipeline` drops any item that lacks a `buyer_rep_email`, ensuring only actionable leads are exported.
7. **Output**: Scrapy's feed export writes the surviving items to CSV.

## Installation and Setup

1. Clone the repository:

```
git clone https://github.com/your-username/realtor-properties-from-all-states-with-filters.git
cd realtor-properties-from-all-states-with-filters
```

2. Create and activate a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

3. Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the spider from the project root directory (where `scrapy.cfg` is located):

```
scrapy crawl sold -o output.csv
```

This will scrape all 50 states and write results to `output.csv`. You can also use other Scrapy-supported formats:

```
scrapy crawl sold -o output.json
scrapy crawl sold -o output.jsonl
```

## Output Format

The scraper produces records with the following columns:

| Column | Description |
|---|---|
| `seller_represented_name` | Name of the seller's listing agent |
| `seller_represented_email` | Email of the seller's listing agent |
| `seller_rep_comp_name` | Name of the seller agent's brokerage |
| `seller_represented_company_email` | Email of the seller agent's brokerage |
| `buyer_rep_name` | Name of the buyer's agent |
| `buyer_rep_email` | Email of the buyer's agent |
| `buyer_rep_link` | Profile URL of the buyer's agent |
| `buyer_rep_company` | Name of the buyer agent's brokerage |
| `property_url` | Realtor.com URL for the property |
| `list_date` | Date the property was listed |
| `last_sold_date` | Date the property was last sold |
| `list_price` | Original listing price |
| `last_sold_price` | Final sale price |
| `city` | City where the property is located |
| `state` | State code (e.g., CA, NY) |
| `postal_code` | ZIP code |
| `primary_photo` | URL of the property's primary photo |

## Configuration

Key parameters can be adjusted in `realtor_listings/utilities.py`:

- **`MIN_PRICE`** (default: 750,000) -- Minimum sold price filter. Only properties sold at or above this amount are included.
- **`DAYS_BACK`** (default: 7) -- How many days back from today to search for sold listings.
- **`RESULTS_PER_PAGE`** (default: 42) -- Number of results per API page request.

Scrapy-level settings are in `realtor_listings/settings.py`:

- **`ROBOTSTXT_OBEY`** -- Set to `False` since the scraper uses the API directly.
- **`ITEM_PIPELINES`** -- Enables `BuyerEmailPipeline` to filter out listings without buyer email.

## Project Structure

```
realtor-properties-from-all-states-with-filters/
|-- scrapy.cfg                          # Scrapy deployment configuration
|-- requirements.txt                    # Python dependencies
|-- states.xlsx                         # List of US states and state codes
|-- realtor_listings/
|   |-- __init__.py
|   |-- items.py                        # Item definitions (dict-based)
|   |-- middlewares.py                  # Middleware placeholder
|   |-- pipelines.py                   # BuyerEmailPipeline (filters by buyer email)
|   |-- settings.py                    # Scrapy project settings
|   |-- utilities.py                   # API query builders and constants
|   |-- spiders/
|       |-- __init__.py
|       |-- sold_listings_spider.py    # Main spider for sold listings
|-- Readme.Md
```

## Author

Hussain (MrPythonic)

## License

This project is licensed under the MIT License.
