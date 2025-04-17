# Code for ETL operations on Country-GDP data

# Importing the required libraries
import numpy as np
import pandas as pd
import glob
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n')

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    df = pd.DataFrame(columns=table_attribs)
    count = 0

    data = BeautifulSoup(requests.get(url).text, 'html.parser')

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        if count<10:
            col = row.find_all('td')
            if len(col)!=0:
                data_dict = {"Name": col[1].find_all('a')[1]["title"],
                            "MC_USD_Billion": float(col[2].contents[0][:-1])}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
                count+=1
        else:
            break
    # print(df)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    df_FX = pd.read_csv(csv_path, header=0)
    exchange_rate = dict(zip(df_FX.iloc[:,0], df_FX.iloc[:,1].apply(lambda x: float(x))))
    df['MC_GBP_Billion'] = df['MC_USD_Billion'].apply(lambda x: np.round(x * exchange_rate['GBP']))
    df['MC_EUR_Billion'] = df['MC_USD_Billion'].apply(lambda x: np.round(x * exchange_rate['EUR']))
    df['MC_INR_Billion'] = df['MC_USD_Billion'].apply(lambda x: np.round(x * exchange_rate['INR']))
    # print(df['MC_EUR_Billion'][4])
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index =False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(pd.read_sql(query_statement, sql_connection))

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

# Log the initialization of the ETL process 
dataURL = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
fxrate_csv_path = "exchange_rate.csv"
table_cols = ["Name", "MC_USD_Billion"]
output_csv_path = "./Largest_banks_data.csv"
db_name = "Banks.db"
table_name = "Largest_banks"
log_file = "code_log.txt"
log_progress("Preliminaries complete. Initiating ETL process")

# Extract data
df = extract(dataURL, table_cols)
log_progress("Data extraction complete. Initiating Transformation process")

# Transform data
df = transform(df, fxrate_csv_path)
log_progress("Data transformation complete. Initiating Loading process")

# Output to CSV
load_to_csv(df, output_csv_path)
log_progress("Data saved to CSV file")

# connect to db
sql_conn = sqlite3.connect(db_name)
log_progress("SQL Connection initiated")

# load to db
load_to_db(df, sql_conn, table_name)
log_progress("Data loaded to Database as a table, Executing queries")

# run queries
query_statement1 = f"SELECT * FROM {table_name}"
run_query(query_statement1, sql_conn)

query_statement2 = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement2, sql_conn)

query_statement3 = f"SELECT Name FROM {table_name} LIMIT 5"
run_query(query_statement3, sql_conn)

log_progress("Process Complete")

# close server connection
sql_conn.close()
log_progress("Server Connection closed")