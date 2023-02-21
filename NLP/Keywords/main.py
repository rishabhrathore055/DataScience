# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from rake_nltk import Rake

def extract_keywords():
    session = HTMLSession()
    url = 'https://www.musicradar.com/reviews/tech/akg-c214-172209'
    response = session.get(url)
    return response.html.find('div#article-body', first=True).text

r = Rake()
r.extract_keywords_from_text(extract_keywords())
print(r.extract_keywords_from_text)
# print(r.get_ranked_phrases_with_scores()) 
# print(r.get_ranked_phrases()) 
