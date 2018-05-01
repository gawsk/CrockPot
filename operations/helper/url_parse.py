""" Module provides functions for parsing recipes """

import urllib2
from bs4 import BeautifulSoup
from operations.recipe import recipe_modify

def name(soup, results):
    results['name'] = (soup.findAll('h1', {'class':'recipe-summary__h1'})[0].text).encode('ascii', 'ignore')
    return results

def description(soup, results):
    results['description'] = (soup.findAll('div', {'class':'submitter__description'})[0].text).encode('ascii', 'ignore')
    return results

def ingredients(soup, results):
    results['ingredients'] = ([element.text for element in \
                                soup.findAll('span', {'class':'recipe-ingred_txt added'})])
    return results

def steps(soup, results):
    results['steps'] = ([element.text for element in soup.findAll('li', {'class':'step'})])
    return results

def image(soup, results):
    results['image_url'] = (soup.findAll("img", {"class":"rec-photo"})[0]['src'])
    return results


def allrecipes(url, category_id, user_id):
    """ Parser for allrecipes.com """

    url = url.split("?")[0]
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'lxml')
    soup.prettify()
    results = {'url':url}

    results = name(soup, results)
    results = description(soup, results)
    results = ingredients(soup, results)
    results = steps(soup, results)
    results = image(soup, results)




    return recipe_modify.add_recipe_info(user_id, category_id, results)
