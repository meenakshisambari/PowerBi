import pandas as pd
import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Pundarikam14@',
    'database': 'women'  # your database name
}

# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Load the CSV file into a DataFrame
df = pd.read_csv('C:/Users/meena/Desktop/cleaned_Womens_Clothing_E-Commerce_Reviews.csv')

# Fetch existing dimension entries
cursor.execute('SELECT division_id, division_name FROM division_dim')
division_map = {name: id for id, name in cursor.fetchall()}

cursor.execute('SELECT department_id, department_name FROM department_dim')
department_map = {name: id for id, name in cursor.fetchall()}

cursor.execute('SELECT class_id, class_name FROM class_dim')
class_map = {name: id for id, name in cursor.fetchall()}

# Inserting records
for index, row in df.iterrows():
    try:
        # Fetching foreign key IDs with checks
        division_id = division_map.get(row['division_name'])
        department_id = department_map.get(row['department_name'])
        class_id = class_map.get(row['class_name'])

        # Check if any foreign key is not found and log the skipped row
        if not division_id or not department_id or not class_id:
            print(f"Skipping row {index + 1}: Foreign key not found for division_name='{row['division_name']}', department_name='{row['department_name']}', class_name='{row['class_name']}'.")
            continue

        # Insert into product_fact
        sql_query = '''
            INSERT INTO product_fact (clothing_id, age, title, review_text, rating, recommended_ind, positive_feedback_count, division_id, department_id, class_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(sql_query, (row['clothing_id'], row['age'], row['title'], row['review_text'], row['rating'], row['recommended_ind'], row['positive_feedback_count'], division_id, department_id, class_id))

        conn.commit()
        print(f"Inserted row {index + 1} successfully.")
    except mysql.connector.Error as err:
        print(f"Error inserting row {index + 1}: {err}")

# Close the cursor and connection
cursor.close()
conn.close()
