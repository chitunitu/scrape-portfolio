import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website to scrape (safe public demo site)
url = "https://realpython.github.io/fake-jobs/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

job_list = []

for job in jobs:
    title = job.find("h2").text.strip()
    company = job.find("h3").text.strip()
    location = job.find("p", class_="location").text.strip()

    job_list.append({
        "Job Title": title,
        "Company": company,
        "Location": location
    })

# Convert to DataFrame
df = pd.DataFrame(job_list)

# Save to Excel
df.to_excel("scraped_jobs.xlsx", index=False)

print("\n✅ LIVE JOB DATA SCRAPED")
print("✅ File created: scraped_jobs.xlsx")
