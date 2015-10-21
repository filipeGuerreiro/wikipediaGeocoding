'''
Created on Oct 21, 2015

@author: Filipe
'''
import urllib2
import json

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


def appendPopupStyleHeader(soup):
    styleTag = soup.new_tag('style')    
    styleTag.insert(0, 'a img.popup { display:none; } a:hover img.popup { display:inline; }')
    soup.head.append(styleTag)


def appendImageToLink(link, image):
    link.append('<img class=\"popup\" src=\"'+image+"\"/>")
    


if __name__ == '__main__':
    pass