import csv
import pandas as pd
import xmlrpc.client

# Path to your CSV file
csv_file_path = "mldata.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Replace 'column_name' with the name of the column you want to select
selected_column = df['Type of company want to settle in?']

unique_words = selected_column.str.split().explode().unique()

# Convert unique_words to a list
unique_words_list = unique_words.tolist()

# Print the list of unique words
print(unique_words_list)

# url = 'http://localhost:8016'
# db = "careerappp"
# user_name = 'admin@gmail.com'
# password = 'admin'
url = 'http://localhost:8769'
db = "odoo"
user_name = 'admin'
password = 'admin'

# Authenticate with the Odoo server
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, user_name, password, {})

# Connect to the Odoo server
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Create records in the Odoo model
for word in unique_words_list:
    # Replace 'model_name' with the name of your Odoo model
    # Replace 'field_name' with the name of the field in the model where you want to store the word
    record_id = models.execute_kw(db, uid, password, 'res.company', 'create', [{'name': word}])

    print("Record created with ID:", record_id)