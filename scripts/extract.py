import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

path= "data/raw"
if not os.path.exists(path):
    os.makedirs(path)
    print("Path Created")
else: 
    print("Path already present")
    


os.makedirs("data/raw", exist_ok=True)

url="https://www.indeed.com/jobs?q=data+engineer&l=New+York"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

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

# Debug: Print the number of jobs extracted
print(f"Extracted {len(jobs)} jobs")

#convert to dataframe

df= pd.DataFrame(jobs)

print(df.head())


df.to_csv(os.path.join(path,"raw_jobs.csv"), index=False)
print("Data extracted and save to location")

