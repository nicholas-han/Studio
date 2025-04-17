import glob
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

log_file = "log_file.txt" 
target_file = "transformed_data.csv"

def extract_file(file_to_process):
    if(file_to_process.endswith(".csv")):
        return pd.read_csv(file_to_process)
    if(file_to_process.endswith(".json")):
        return pd.read_json(file_to_process,lines=True)
    if(file_to_process.endswith(".xml")):
        dataframe = pd.DataFrame(columns=["name","height","weight"])       
        for person in ET.parse(file_to_process).getroot():
            name = person.find("name").text
            height = float(person.find("height").text)
            weight = float(person.find("weight").text)
            dataframe = pd.concat([dataframe, pd.DataFrame([{"name":name, "height":height,"weight":weight}])],ignore_index=True)
        return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
    files_to_extract = glob.glob("*.csv") + glob.glob("*.json") + glob.glob("*.xml")
    for file in files_to_extract:
        if file != target_file:
            extracted_data = pd.concat([extracted_data, extract_file(file)], ignore_index=True) 
    return extracted_data

def transform(data): 
    data['height'] = round(data['height'] * 0.0254,2) 
    data['weight'] = round(data['weight'] * 0.45359237,2) 
    
    return data

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file)

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n')

# Log the initialization of the ETL process 
log_progress("ETL Job Started") 
 
# Log the beginning of the Extraction process 
log_progress("Extract phase Started")
extracted_data = extract()
 
# Log the completion of the Extraction process 
log_progress("Extract phase Ended")
 
# Log the beginning of the Transformation process 
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)
 
# Log the completion of the Transformation process 
log_progress("Transform phase Ended")
 
# Log the beginning of the Loading process 
log_progress("Load phase Started")
load_data(target_file,transformed_data) 
 
# Log the completion of the Loading process 
log_progress("Load phase Ended")
 
# Log the completion of the ETL process 
log_progress("ETL Job Ended")