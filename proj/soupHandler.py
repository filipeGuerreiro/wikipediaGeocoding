'''
Created on Oct 21, 2015

@author: Filipe
'''

from bs4 import BeautifulSoup

''' 
    Receives a webpage and returns a dictionary with the 
    key: text of hyperlink and as value: the soup html tree pointer.
'''
def getHyperlinks(html_page):
    
    html_doc = html_page.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    
    res = dict()
    for link in soup.find_all(soupFunction):
        
        if link.get('title') != None:
            linkText = link.get('title').encode('utf8')
            res[linkText] = link
            
    #print ', '.join(res)
    return res, soup

''' Returns true if the tag is in the main body of the article '''
def soupFunction(tag):
    if tag.name == 'a':
        if tag.parent.name == 'p':
            try:
                if tag.parent.parent['class'][0] == 'mw-content-ltr':
                    return True
            except:
                return False
    return False
