#clean the data replace the missing values with mean and median
import pandas as pd
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as stop_words
from linearalgebra.configurations.conf import Config

def clean_data(file_path):
    #read the data
    data = pd.read_excel(file_path)
    #replace the zero values in insulin column with null values
    data['Insulin']=data['Insulin'].replace(0, pd.NA)
    #replace the missing values in insulin column with mean
    data['Insulin']=data['Insulin'].fillna(data['Insulin'].mean(), 
                                           inplace=True)
    #save the cleaned data to a new file
    cleaned_file_path = file_path.replace('.xlsx', '_cleaned.xlsx')
    data.to_excel(cleaned_file_path, index=False)
    return data

def clean_employee_data(file_path):
    data = pd.read_csv(file_path)
    #removing special characters from the first name column
    data['first_name'] = data['first_name'] \
        .str.replace('[^a-zA-Z]', '', regex=True)
    #replace inconsistent date of joining values to indian date format
    data['date_of_joining'] = pd.to_datetime \
         (data['date_of_joining'],errors='coerce') \
            .dt.strftime('%d-%m-%Y')
    #convert the gender column to lowercase
    data['gender'] = data['gender'].str.lower()
    #replace m to male and f to female
    data['gender'] = data['gender'] \
        .replace({'m': 'male', 'f': 'female'})
    #check email accoding to the standard email format
    data['email'] = data['email'].str.lower()
    data['email'] = data['email'] \
        .str.replace('[^a-zA-Z0-9@._]', '', regex=True)
    #check for duplicate row by first name and email
    #count the number of duplicate rows
    duplicate_count = data.duplicated(subset=['first_name', 'email']) \
            .sum()
    print(f"Number of duplicate rows: {duplicate_count}")
    data = data.drop_duplicates(subset=['first_name', 'email'])
    #save the cleaned data to a new file
    cleaned_file_path = file_path.replace('.csv', '_cleaned.csv')   
    data.to_csv(cleaned_file_path, index=False)
    return data
def clean_cyber_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    #remove stop words from the data
    documents=[f for f in data.split('\n') if f.strip()]
    print(f"Number of documents: {len(documents)}")
    #read word by word and remove stop words for NLP
    #write the cleaned data to a new file    
    new_array=[]
    for doc in documents:
       new_doc=  "".join([word for word in doc.split() 
                 if word.lower() not in stop_words])
       new_array.append(new_doc)
    cleaned_file_path = file_path.replace('.txt', '_cleaned.txt')
    with open(cleaned_file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(new_array))       
        

    return documents
     


if __name__ == "__main__":
    file_path = Config.cleandata_path
    file_path_v1=Config.cleandata_path_v1
    cleaned_data = clean_data(file_path)
    print(cleaned_data.head())
    cleaned_employee_data = clean_employee_data(file_path_v1)
    print(cleaned_employee_data.head())
    cyber_path=Config.cyber_path
    cleaned_cyber_data = clean_cyber_data(cyber_path)
    print(cleaned_cyber_data[:5])