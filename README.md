# wikipediaGeocoding
## Required libraries:
- Beautifulsoup4
- geopy

Given a link to a Wikipedia page, this extracts a list of the names for geographical
locations that you can identify in that page. These names can be any type of geographical
location (e.g. countries, cities, points of interest, etc.). This search is limited to
names that appear in the article text and have an hyperlink.
The names found are matched to an entry in the Geonames database. All
locations are disambiguated, i.e. it is able to tell if the name “Paris”
corresponds to a city in France, or to a city in Togo, or to any other place. 
The Geonames webservice is used.

For example, given the Wikipedia page at https://en.wikipedia.org/wiki/Riddley_
Walker, you can find the locations:

• Canterbury Cathedral (lat:51.27987, lng:1.08176)
• Kent (lat:51.16667, lng:0.66667)
• Dover (lat:51.13333, lng:1.3)
• Waterford (lat:52.25833, lng:-7.11194)
• Austin (lat:30.26715, lng:-97.74306)