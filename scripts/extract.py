import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

os.makedirs("data/raw", exist_ok=True)

url="https://www.indeed.com/jobs?q=data+engineer&l=New+York"

#Get Request
response= requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Extract job details

jobs= []

for job in soup.find_all('div', class_='job_seen_beacon'):
    title = job.find('h2', class_='jobTitle').text.strip()
    company = job.find('span', class_='companyName').text.strip()
    location = job.find('div', class_='companyLocation').text.strip()
    salary = job.find('div', class_='salary-snippet')
    salary = salary.text.strip() if salary else "Not Provided"
    jobs.append({
        'title': title,
        'company': company,
        'location': location,
        'salary': salary
    })

#convert to dataframe

df= pd.DataFrame(jobs)

df.to_csv("data/raw/raw_jobs.csv", index=False)
print("Data extracted and save to location")

