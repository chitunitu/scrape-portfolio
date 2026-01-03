# scrape-portfolio

Small, real-world Python web scraping demos built with `requests`, `BeautifulSoup`, and `pandas`.

## 1. Job Listings Scraper

**File:** `job_scraper.py`  
**Sample output:** `scraped_jobs.xlsx`

What it does:

- Scrapes job listings from a public job board.
- Extracts fields like job title, company, location, and link.
- Cleans the data and exports it to a structured Excel file for analysis or outreach.

## 2. Price Tracker Scraper

**File:** `price_scraper.py`  
**Sample output:** `scraped_prices.xlsx`

What it does:

- Scrapes product names and prices from an e-commerce page.
- Normalizes the data into rows (product, price, URL).
- Saves everything to Excel so non-technical users can filter and track price changes.

---

### Tech stack

- Python 3
- `requests` – HTTP requests
- `beautifulsoup4` – HTML parsing
- `pandas` – data cleaning & Excel export

These mini-projects show how I approach:

- Clean, reliable extraction using CSS selectors
- Respectful scraping with simple rate limiting
- Deliverables in formats clients can actually use (Excel/CSV)
