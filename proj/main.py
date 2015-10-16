'''
Created on Oct 14, 2015

@author: Filipe
'''
from bs4 import BeautifulSoup
import urllib2

from geopy.geocoders import Nominatim

def getHyperlinkText(html_page):
    
    html_doc = html_page.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    #print soup.find('div', id='bodyContent').p
    
    res = []
    for link in soup.find_all('a'):
        
        if link.get('title') != None:
            #print link.get('title').encode('utf8')
            res.append(link.get('title').encode('utf8'))
    
    #print ', '.join(res)
    return res
        

if __name__ == '__main__':
    
    pageName = "https://en.wikipedia.org/wiki/Riddley_Walker"  
    html_page = urllib2.urlopen(pageName)
    
    hyperlinkList = getHyperlinkText(html_page)
    
    geolocator = Nominatim()
    for query in hyperlinkList:
        location = geolocator.geocode(query)
        if location != None:
            print query,':',location.latitude,',',location.longitude
    
    
    