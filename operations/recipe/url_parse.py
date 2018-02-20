""" Module provides functions for parsing recipes """

from bs4 import BeautifulSoup
import urllib2
from operations.recipe import recipe_modify


def allrecipes(url, user_id):
    """ Praser for allrecipes.com """

    url = url.split("?")[0]
    print url
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    soup.prettify()
    results = {'url':url}


    # Recipe name
    results['name'] = soup.findAll('h1', {'class':'recipe-summary__h1'})[0].text
    # for anchor in soup.findAll('h1', {'class':'recipe-summary__h1'}):
    #     print anchor.text

    # Recipe description
    results['description'] = soup.findAll('div', {'class':'submitter__description'})[0].text
    # for anchor in soup.findAll('div', {'class':'submitter__description'}):
    #     print anchor.text


    # Ingredients
    results['ingredients'] = [element.text for element in soup.findAll('span', {'class':'recipe-ingred_txt added'})]
    # for anchor in soup.findAll('span', {'class':'recipe-ingred_txt added'}):
    #     print anchor.text

    # Steps
    results['steps'] = [element.text for element in soup.findAll('li', {'class':'step'})]
    # for anchor in soup.findAll('li', {'class':'step'}):
    #     print anchor.text


    # # Prep time
    # for anchor in soup.findAll('time', {'itemprop':'prepTime'}):
    #     print anchor.text
    #
    # # Cook time
    # for anchor in soup.findAll('time', {'itemprop':'cookTime'}):
    #     print anchor.text
    #
    # # Total time
    # for anchor in soup.findAll('time', {'itemprop':'totalTime'}):
    #     print anchor.text
    recipe_modify.add_recipe_info(user_id, results)
