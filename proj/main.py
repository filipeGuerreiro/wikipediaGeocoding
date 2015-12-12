'''
Created on Oct 14, 2015

@author: Filipe

'''

import urllib2
import codecs
import HTMLParser
import os

#from geopy.geocoders import GeoNames
#from pprint import pprint
from soupHandler import getHyperlinks
from europeanaHandler import appendImageToLink, extractImageEuropeana,\
    appendPopupStyleHeader, changeImageDirectory
from wikipediaHandler import extractCoordinates


def main():
    #pageName = "https://en.wikipedia.org/wiki/Russell_Hoban"  
    
    print 'Insira o link'
    pageName = raw_input('---> ')
    
    html_page = urllib2.urlopen(pageName)    
    hyperlinkDict, soup = getHyperlinks(html_page)
    
    for link, tag in hyperlinkDict.iteritems():
        lat, lon = extractCoordinates(link)
        if lat != None:
            print link, lat, lon
    
            image = extractImageEuropeana(link, lat, lon)
            changeImageDirectory(soup)
            appendImageToLink(tag, image)
    
    appendPopupStyleHeader(soup)
    
    fileName = os.path.dirname(os.path.abspath(__file__)) + 'output.html'
    fout = codecs.open(fileName, 'w', 'utf-8')
    htmlParser = HTMLParser.HTMLParser()
    fout.write(htmlParser.unescape(soup.prettify()))


'''def geocode(hyperlinkList):
    geolocator = GeoNames(country_bias='UK', username='filipeguerreiro')
    for query in hyperlinkList:
        location = geolocator.geocode(query)
        if location != None:
            print query, ':', location.latitude, location.longitude'''
            

if __name__ == '__main__':
    
    main()