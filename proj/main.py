'''
Created on Oct 14, 2015

@author: Filipe

'''
from bs4 import BeautifulSoup
import urllib2

#from geopy.geocoders import Nominatim
from geopy.geocoders import GeoNames


def getHyperlinkText(html_page):
    
    html_doc = html_page.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print soup.find('mw-content-text')
    
    res = []
    for link in soup.find_all(soupFunction):
        
        if link.get('title') != None:
            #print link.get('title').encode('utf8')
            linkText = link.get('title').encode('utf8')
            res.append(linkText)
            
    
    #print ', '.join(res)
    return res


def soupFunction(tag):
    if tag.name == 'a':
        if tag.parent.name == 'p':
            if tag.parent.parent['class'][0] == 'mw-content-ltr':
                return True
    return False


def geocode(hyperlinkList):
    geolocator = GeoNames(country_bias='UK', username='filipeguerreiro')
    for query in hyperlinkList:
        location = geolocator.geocode(query)
        if location != None:
            print query, ':', location.latitude, ',', location.longitude
         

if __name__ == '__main__':
    
    pageName = "https://en.wikipedia.org/wiki/Riddley_Walker"  
    html_page = urllib2.urlopen(pageName)
    
    hyperlinkList = getHyperlinkText(html_page)
    
    geocode(hyperlinkList)
    
    
    