import pandas as pd
import spacy
import os

os.makedirs("data/cleaned", exist_ok=True)

#Load Raw Data
df= pd.read_csv("data/raw/raw_jobs.csv")

#clean salary column
def clean_salary(salary):
    if salary!= "Not Provided":
        salary= salary.replace('$','').replace(',','')
        if '-' in salary:
            salary = salary.split('-')[0]
        return int(salary)
    return None

df['salary']= df['salary'].apply(clean_salary)

# No duplicate
df = df.drop_duplicates()

#Extract skills using NLP
nlp= spacy.load("en_core_web_sm")

def extract_skills(text):
    doc= nlp(text)
    skills= [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return skills

df['skills']= df['title'].apply[extract_skills]

# Save cleaned data
df.to_csv("data/cleaned/cleaned_jobs.csv", insex= False)
print("Data cleaned and saved")