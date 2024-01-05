import sqlite3
import pandas as pd

# using SQLite3 to create and connect to the process to a new database 
conn = sqlite3.connect('STAFF.db')

# Create and Load the table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Reading the CSV file
file_path = 'INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

# Loading the data to a table
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')

# Running basic queries on data
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing only FNAME column of data 
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing the total number of entries in the table 
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Appending some data to the table
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

# data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# The count Query 
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Close te connection to database 
conn.close()