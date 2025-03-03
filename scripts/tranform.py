import pandas as pd
import spacy
import os

path= "data/cleaned"
if not os.path.exists(path):
    os.makedirs(path)
    print("Path Created")
else: 
    print("Path already present")


#Load Raw Data
df= pd.read_csv("data/raw/Raw_data.csv")
print(df.head())
print(df.columns)

# Clean salary column (if 'Salary Estimate' exists)
if 'Salary Estimate' in df.columns:
    def clean_salary(salary):
        if isinstance(salary, str):
            # Remove dollar signs, commas, and text like '(Glassdoor est.)'
            salary = salary.replace('$', '').replace(',', '').replace('(Glassdoor est.)', '').strip()
            print(f"Processing salary: {salary}")  # Debugging

            # Handle salary ranges (e.g., 111K-181k)
            if '-' in salary:
                salary = salary.split('-')[0]  # Take the lower bound
                print(f"Extracted lower bound: {salary}")  # Debugging
            
            # Handle 'K' notation (e.g., 111K -> 111000)
            if 'K' in salary:
                salary = salary.replace('K', '')
                salary = float(salary) * 1000  # Convert to full number
                return int(salary)
            
            # Convert to integer
            try:
                return int(float(salary))  # Handle cases like '120000.0'
            except ValueError:
                print(f"Invalid salary value: {salary}")  # Debugging
                return None  # Skip invalid values
        return None

    df['salary'] = df['Salary Estimate'].apply(clean_salary)
else:
    print("Warning: 'Salary Estimate' column not found. Skipping salary cleaning.")


# Drop duplicates
df = df.drop_duplicates()

# Extract skills using NLP (if 'Job Description' exists)
nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    # Debug: Print the input text
    print(f"\nProcessing job description:\n{text}")
    
    # Load the text into a spaCy document
    doc = nlp(text)
    
    # Debug: Print all entities and their labels
    print("\nEntities found in the text:")
    for ent in doc.ents:
        print(f"Text: {ent.text}, Label: {ent.label_}")
    
    # Extract skills (entities labeled as "SKILL")
    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    
    # Debug: Print the extracted skills
    print("\nExtracted skills:")
    print(skills)
    
    return skills

if 'Job Description' in df.columns:
    df['skills'] = df['Job Description'].apply(extract_skills)
else:
    print("Warning: 'Job Description' column not found. Skipping skill extraction.")

# Save cleaned data
df.to_csv(os.path.join(path,"cleaned_jobs.csv"), index= False)
print("Data cleaned and saved")