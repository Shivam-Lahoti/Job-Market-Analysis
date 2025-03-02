import pandas as pd
from sqlalchemy import create_engine
import os

os.makedirs("data/models", exist_ok=True)

df= pd.read_csv("data/cleaned/cleaned_jobs.csv")

#Connect to PostgreSQL database 
engine= create_engine('postgresql://user:password@localhost:5432/job_market')

#save DataFrame to database

df.to_sql('jobs', engine , if_exists='replace', index=False)
print("Data loaded into PostgreSQL")

