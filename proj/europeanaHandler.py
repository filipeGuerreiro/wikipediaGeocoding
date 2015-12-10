'''
Created on Oct 21, 2015

@author: Filipe
'''
import urllib2
import json
import re

EUROPEANA_API = ("http://europeana.eu/api/v2/search.json?"
                 "wskey=3STkxBhE8&rows=1&qf=TYPE:IMAGE&query=")



def extractImageEuropeana(link):
    urlFriendlyString = link.replace(' ', '%20')
    europeanaResponse = urllib2.urlopen(EUROPEANA_API+urlFriendlyString)
    jsonResponse = json.load(europeanaResponse)
    try:
        return jsonResponse['items'][0]['edmPreview'][0]
    except KeyError:
        return '--Europeana image not found--'

def changeImageDirectory(soup):
    i = []
    images = soup.findAll('link')
    for j in images:
        if not re.search('//', str(headerlink['href'])):
            headerlink['href'] = "https://wikipedia.org" + headerlink['href']
        else:
            i.append(headerlink)
    for div in soup.findAll('div'):
        for link in div.findAll('a', href=True):
            if not re.search('//|#', str(link['href'])):
                link['href'] = "https://wikipedia.org" + link['href']
            else:
                i.append(link)

def appendPopupStyleHeader(soup):
    styleTag = soup.new_tag('style')    
    styleTag.insert(0, 'a img.popup { display:none; } a:hover img.popup { display:inline; }')
    soup.head.append(styleTag)


def appendImageToLink(link, image):
    link.append('<img class=\"popup\" src=\"'+image+"\"/>")






    