import pandas as pd
from sqlalchemy import create_engine
import os

path= "data/cleaned"
if not os.path.exists(path):
    os.makedirs(path)
    print("Path Created")
else: 
    print("Path already present")


df= pd.read_csv(os.path.join(path,"cleaned_jobs.csv"))

#Connect to PostgreSQL database 
engine= create_engine('postgresql://user:password@localhost:5432/job_market')

#save DataFrame to database

df.to_sql('jobs', engine , if_exists='replace', index=False)
print("Data loaded into PostgreSQL")

