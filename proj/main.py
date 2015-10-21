'''
Created on Oct 14, 2015

@author: Filipe

'''

import urllib2
import codecs

from geopy.geocoders import GeoNames
from pprint import pprint
from soupHandler import getHyperlinks
from europeanaHandler import appendImageToLink, extractImageEuropeana,\
    appendPopupStyleHeader
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
            #geoLocations.append(link)
            #image = extractImageEuropeana(link)
            #appendImageToLink(tag, image)
    
    #appendPopupStyleHeader(soup)
    #fout = codecs.open('C:\\Users\\Filipe\\Desktop\\PRI\\fout.html', 'w', 'utf-8')
    #fout.write(soup.prettify())


'''def geocode(hyperlinkList):
    geolocator = GeoNames(country_bias='UK', username='filipeguerreiro')
    for query in hyperlinkList:
        location = geolocator.geocode(query)
        if location != None:
            print query, ':', location.latitude, location.longitude'''
            

if __name__ == '__main__':
    
    main()