#topic modeling using The Hindu article on Rahul Gandhi's accusations against BJP in Rajya Sabha polls.
#https://www.thehindu.com/news/national/after-vote-chori-and-sarkar-chori-charges-rahul-gandhi-accuses-bjp-of-seat-chori-in-rajya-sabha-polls/article71089851.ece?cx_testId=127&cx_testVariant=cx_1&cx_artPos=1&cx_experienceId=EXPO56ZDYSGX&cx_experienceActionId=showRecommendationsD6E1OEQYOG3N57
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

scrape_url = os.getenv("article_url")

def scrape_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_div = soup.select('#schemaDiv > p:nth-child(1)')  # Adjust the selector based on the actual HTML structure
    if article_div:
        return article_div[0].get_text(separator='\n').strip()
    else:
        raise Exception("Article not found on the page.")
if __name__ == "__main__":
    try:
        article = scrape_article(scrape_url)
        print(article)
    except Exception as e:
        print(f"Error: {e}")