'''
Created on Oct 21, 2015

@author: Filipe
'''

import urllib2
import json


WIKIGEO_API = ("https://en.wikipedia.org/w/api.php?"
               "action=query&prop=coordinates&format=json&titles=")


def extractCoordinates(link):
    urlFriendlyString = link.replace(' ', '%20')
    #http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    #wikipediaResponse = http.request('GET', WIKIGEO_API+urlFriendlyString)
    wikipediaResponse = urllib2.urlopen(WIKIGEO_API+urlFriendlyString)
    try:
        jsonResponse = json.load(wikipediaResponse)
        lat = jsonResponse['query']['pages'].values()[0]['coordinates'][0]['lat']
        lon = jsonResponse['query']['pages'].values()[0]['coordinates'][0]['lon']
        return [lat, lon]
    except:
        return None, None
