#topic modeling using The Hindu article on Rahul Gandhi's accusations against BJP in Rajya Sabha polls.
#https://www.thehindu.com/news/national/after-vote-chori-and-sarkar-chori-charges-rahul-gandhi-accuses-bjp-of-seat-chori-in-rajya-sabha-polls/article71089851.ece?cx_testId=127&cx_testVariant=cx_1&cx_artPos=1&cx_experienceId=EXPO56ZDYSGX&cx_experienceActionId=showRecommendationsD6E1OEQYOG3N57
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

scrape_url = os.getenv("lyrics_url")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_article(url):
    response = requests.get(url,headers=headers,timeout=20)
    soup = BeautifulSoup(response.text, 'html.parser')
    lyrics_div = soup.find('pre','lyric-body')
    if lyrics_div:
        return lyrics_div.get_text(separator='\n').strip()
    else:
        raise Exception("Lyrics not found on the page.")
    
def topic_modeling(article):
    # Placeholder for topic modeling implementation
    # You can use libraries like Gensim or LDA for actual topic modeling
    print("Topic modeling is not implemented yet.")

if __name__ == "__main__":
    try:
        article = scrape_article(scrape_url)
        print(article)
    except Exception as e:
        print(f"Error: {e}")