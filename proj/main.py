'''
Created on Oct 14, 2015

@author: Filipe
'''
from BeautifulSoup import BeautifulSoup
import urllib2

def getHyperlinkText(html_page):
    
    soup = BeautifulSoup(html_page)
    
    res = []
    for link in soup.findAll('a'):
        res.append(link.get('title'))
    
    print '\n'.join(res)
    return res
        

if __name__ == '__main__':
    pageName = "https://en.wikipedia.org/wiki/Riddley_Walker"
    
    html_page = urllib2.urlopen(pageName)
    
    hyperlinkList = getHyperlinkText(html_page)
    
    
    
    