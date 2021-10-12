"""
bs4 is used to parse text content
requests import get #extract web content
gensim is used for summarization of text
"""

from bs4 import BeautifulSoup 
import requests

from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

def get_only_text(url):
    """
    return the title and the text of the article
    at the specified url
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    # text = soup.text
    title = ' '.join(soup.title.stripped_strings)
    return title, text

article = get_only_text("https://www.vox.com/policy-and-politics/2019/5/30/18642535/california-ab5-misclassify-employees-contractors")
sArticleTitle = article[0]
sArticleText = article[1]
print('-' * 12 + '\Original text: \n')
print("Article title = " + sArticleTitle)
nWordCounter = len(str.split(sArticleText))
print("Words in article: " + str(nWordCounter))
print('-' * 12)
print(sArticleText)
print('-' * 12)


#Summarization [1]:
sTextSummary = summarize(sArticleText,word_count=100)
# sTextSummary = summarize(repr(sArticleText), ratio = 0.01)
print('-' * 12 + '\nText summary: \n')
print('Length = ' + str(len(sTextSummary)))
print('-' * 12)
print(sTextSummary)
print('-' * 12)

#Summarization [2]:
sTextSummary = summarize(sArticleText,ratio=0.07)
# sTextSummary = summarize(repr(sArticleText), ratio = 0.01)
print('-' * 12 + '\nText summary: \n')
print('Length = ' + str(len(sTextSummary)))
print('-' * 12)
print(sTextSummary)
print('-' * 12)

# Keywords :
sKeywords = keywords(sArticleText)
print('-' * 12 + '\nKeywords[1]: \n')
print(sKeywords)

sKeywords = keywords(sArticleText,ratio=0.1,lemmatize=True)
print('-' * 12 + '\nKeywords[2]: \n')
print(sKeywords)