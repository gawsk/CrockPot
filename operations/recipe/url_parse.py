""" Module provides functions for parsing recipes """

from bs4 import BeautifulSoup
import urllib2


def allrecipes(url):
    # soup = BeautifulSoup(url)
    # for each_div in soup.findAll('li',{'class':'checkList__line'}):
    #     print each_div

    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    soup.prettify()

    # Recipe name
    for anchor in soup.findAll('h1', {'class':'recipe-summary__h1'}):
        print anchor.text


    # Ingredients
    for anchor in soup.findAll('span', {'class':'recipe-ingred_txt added'}):
        print anchor.text

    # Steps
    for anchor in soup.findAll('li', {'class':'step'}):
        print anchor.text


    # Prep time
    for anchor in soup.findAll('time', {'itemprop':'prepTime'}):
        print anchor.text

    # Cook time
    for anchor in soup.findAll('time', {'itemprop':'cookTime'}):
        print anchor.text

    # Total time
    for anchor in soup.findAll('time', {'itemprop':'totalTime'}):
        print anchor.text

    pass
