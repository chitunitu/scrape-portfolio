import requests
from bs4 import BeautifulSoup
import pandas as pd

# Amazon-style demo store (100% legal)
url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")

product_list = []

for product in products:
    name = product.h3.a["title"]
    price = product.find("p", class_="price_color").text

    product_list.append({
        "Product Name": name,
        "Price": price
    })

# Save to Excel
df = pd.DataFrame(product_list)
df.to_excel("scraped_prices.xlsx", index=False)

print("\n✅ PRODUCT PRICES SCRAPED SUCCESSFULLY")
print("✅ File created: scraped_prices.xlsx")
