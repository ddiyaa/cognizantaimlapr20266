#scrape the site in .env

import os
import re
from dotenv import load_dotenv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import requests

  
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

scrape_url = os.getenv("scrape_url")
language = os.getenv("language")

#create the headers 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

#read text from the url
def read_text_from_url(url):
      
        response = requests.get(url, headers=headers,timeout=20)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def create_tokens(text):
    #print(text[0].text)
    #clean the text
    cleaned_text = text[0].text.lower()
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)
    #print(cleaned_text)
    #tokenization
    tokens = word_tokenize(cleaned_text)
    return tokens

def stopword_removal(tokens):
    stop_words = set(stopwords.words(language))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    return filtered_tokens

def stemming(tokens):
   
    porter_stemmer = PorterStemmer()
    stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
    return stemmed_tokens

if __name__ == "__main__":
    try:
        text = read_text_from_url(scrape_url)
        #print(text[:500])  # Print the first 500 characters of the fetched text
        #html parsing
        soup = BeautifulSoup(text, 'html.parser')
        #extracting the quotes
        #find by xpath
        text = soup.select('#content_inner > article > p')
        tokens = create_tokens(text)
        tokens = stopword_removal(tokens)
        tokens = stemming(tokens)
        #count the number of tokens
        print(f"Number of tokens: {len(tokens)}")
        print(f"Tokens: {tokens}")

    except Exception as e:
        print(str(e))
  