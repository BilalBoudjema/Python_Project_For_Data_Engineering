import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Initialization of known entities
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_25'
csv_path = 'top_25_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# Loading the webpage for Webscraping
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Scraping of required information
tables = data.find_all('tbody')
# Rows of the first table
rows = tables[0].find_all('tr')


for row in rows:
    if count<25:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Film": col[1].contents[0],
                         "Year": col[2].contents[0],
                         "Rotten Tomatoes' Top 100": col[3].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

df['Year'] = pd.to_numeric(df['Year'])

# Filter for films released in the 2000s
# filtered_df = df[(df['Release_Year'] >= 2000) & (df['Release_Year'] <= 2009)]


# Filter for films released in the 2000s
filtered_df = df[df['Year'] >= 2000]

# Print the filtered DataFrame
print(filtered_df)

# Storing the data to csv
df.to_csv(csv_path)


# Storing the data to  database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
