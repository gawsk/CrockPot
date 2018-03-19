""" Module provides functions for parsing recipes """

import urllib2
from bs4 import BeautifulSoup
from operations.recipe import recipe_modify

def allrecipes(url, user_id):
    """ Parser for allrecipes.com """

    url = url.split("?")[0]
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    soup.prettify()
    results = {'url':url}


    results['name'] = soup.findAll('h1', {'class':'recipe-summary__h1'})[0].text
    results['description'] = soup.findAll('div', {'class':'submitter__description'})[0].text
    results['ingredients'] = [element.text for element in \
                                soup.findAll('span', {'class':'recipe-ingred_txt added'})]
    results['steps'] = [element.text for element in soup.findAll('li', {'class':'step'})]

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


    #TODO: if not sucess, tell user they already have the recipe...
    return recipe_modify.add_recipe_info(user_id, results)