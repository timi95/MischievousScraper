from django.shortcuts import render
from lxml import html
import requests
from bs4 import BeautifulSoup
import nltk

# Create your views here.
def NameFetch1(request):
    x = requests.get('http://www.bbc.com/news/politics')
    soup = BeautifulSoup(x.content, "lxml")
    soup_text = soup.get_text()
    tokens = nltk.word_tokenize(soup_text)
    Jeremy = 'Corbyn'
    #Corbyn= 'Corbyn'

    Theresa = 'Theresa'
    #May = 'May'
    count_corb = 0
    count_may = 0
    for word in tokens:
        if word == Jeremy: #or word == Corbyn:
            count_corb+=1

    for word in tokens:
        if word == Theresa: #or word == May:
            count_may+=1    

    data_dic = {'Name1': count_corb, 'Name2': count_may}
    return render(request,"Polit_Scraper/Index.html", context= data_dic)






