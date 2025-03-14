import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="job_market",
    user="postgres",
    password="123456789@Ab",  # Replace with your password
    host="localhost",
    port="5432"
)

# Create a cursor object
cursor = conn.cursor()

# Query the jobs table
cursor.execute("SELECT * FROM jobs LIMIT 5;")
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()