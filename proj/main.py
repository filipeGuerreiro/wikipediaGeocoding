'''
Created on Oct 14, 2015

@author: Filipe

'''
from bs4 import BeautifulSoup
import urllib2
import json
import codecs

#from geopy.geocoders import Nominatim
from geopy.geocoders import GeoNames
from pprint import pprint

WIKIGEO_API = ("https://en.wikipedia.org/w/api.php?"
               "action=query&prop=coordinates&format=json&titles=")

EUROPEANA_API = ("http://europeana.eu/api/v2/search.json?"
                 "wskey=3STkxBhE8&rows=1&qf=TYPE:IMAGE&query=")


def getHyperlinkText(html_page):
    
    html_doc = html_page.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    res = dict()
    for link in soup.find_all(soupFunction):
        
        if link.get('title') != None:
            linkText = link.get('title').encode('utf8')
            res[linkText] = link
            
    #print ', '.join(res)
    return res, soup


def soupFunction(tag):
    if tag.name == 'a':
        if tag.parent.name == 'p':
            if tag.parent.parent['class'][0] == 'mw-content-ltr':
                return True
    return False


def appendPopupStyleHeader(soup):
    styleTag = soup.new_tag('style')    
    styleTag.insert(0, 'a img.popup { display:none; } a:hover img.popup { display:inline; }')
    soup.head.append(styleTag)


def appendImageToLink(link, image):
    link.append('<img class=\"popup\" src=\"'+image+"\"/>")


def geocode(hyperlinkList):
    geolocator = GeoNames(country_bias='UK', username='filipeguerreiro')
    for query in hyperlinkList:
        location = geolocator.geocode(query)
        if location != None:
            print query, ':', location.latitude, location.longitude
         

def extractCoordinates(link):
    urlFriendlyString = link.replace(' ', '%20')
    wikipediaResponse = urllib2.urlopen(WIKIGEO_API+urlFriendlyString)
    jsonResponse = json.load(wikipediaResponse)
    try:
        lat = jsonResponse['query']['pages'].values()[0]['coordinates'][0]['lat']
        lon = jsonResponse['query']['pages'].values()[0]['coordinates'][0]['lon']
        return [lat, lon]
    except KeyError:
        return None, None
    

def extractImageEuropeana(link):
    urlFriendlyString = link.replace(' ', '%20')
    europeanaResponse = urllib2.urlopen(EUROPEANA_API+urlFriendlyString)
    jsonResponse = json.load(europeanaResponse)
    try:
        return jsonResponse['items'][0]['edmPreview'][0]
    except KeyError:
        return '--Europeana image not found--'
    

if __name__ == '__main__':
    
    pageName = "https://en.wikipedia.org/wiki/Riddley_Walker"  
    html_page = urllib2.urlopen(pageName)    
    hyperlinkDict, soup = getHyperlinkText(html_page)
    
    for link, tag in hyperlinkDict.iteritems():
        lat, lon = extractCoordinates(link)
        if lat != None:
            print link, lat, lon
            #geoLocations.append(link)
            image = extractImageEuropeana(link)
            appendImageToLink(tag, image)
    
    appendPopupStyleHeader(soup)
    fout = codecs.open('C:\\Users\\Filipe\\Desktop\\PRI\\fout.html', 'w', 'utf-8')
    fout.write(soup.prettify())