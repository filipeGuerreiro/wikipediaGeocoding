'''
Created on Oct 14, 2015

@author: Filipe
'''
from BeautifulSoup import BeautifulSoup
import urllib2

def getHyperlinkText(html_page):
    
    data = html_page.read()
    
    soup = BeautifulSoup(data)
    
    res = []
    for link in soup.findAll('a'):
        
        if link.get('title') != None:
            #print link.get('title')
            res.append(link.get('title'))
    
    #print ', '.join(res)
    return res
        

if __name__ == '__main__':
    
    pageName = "https://en.wikipedia.org/wiki/Riddley_Walker"  
    html_page = urllib2.urlopen(pageName)
    
    hyperlinkList = getHyperlinkText(html_page)
    
    
    
    