#cerner_2^5_2017
import urllib2
import json
import sys
#list of stopwords to be ignored for item search
stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours    ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]
#Determine the zip code of your current location
location_zip = json.load(urllib2.urlopen('http://freegeoip.net/json/'))['zip_code']
#Default the zipcode to current location zipcode & item to Milk
zipcode = location_zip
item = 'Milk'
#logic to process command line arguments
if len(sys.argv) <=2:
	if len(sys.argv) == 2:
		if sys.argv[1].isdigit():
			zipcode = sys.argv[1]
		else:
			print "Invalid zipcode!! Defaulting to your current zipcode and showing if it has Milk"
	else: 
		print "Invalid number of arguments provided!! Next time please provide Zipcode and the item to search. Defaulting to your current zipcode and showing if it has Milk"
elif len(sys.argv) >= 3:
	if sys.argv[1].isdigit(): #checks if zipcode provided is valid
		zipcode = sys.argv[1]
	item = sys.argv[2]
#if item is a stopword, default it to Milk
if item in stopwords:
	item = 'Milk'
#find out walmart store id closest to the given Zipcode
stores_obj = json.load(urllib2.urlopen('http://api.walmartlabs.com/v1/stores?format=json&zip='+zipcode+'&apiKey=w254jk8ty7fmsgbdrpx2667b'))
if len(stores_obj) == 0:
	print "No walmart in and around this Zipcode Or Invalid Zip"
	sys.exit()
else:
	print "Closest walmart is:"+stores_obj[0]['name'] +  ", " +stores_obj[0]['streetAddress'] + ", " + stores_obj[0]['city'] + ", " + stores_obj[0]['stateProvCode']
#find out whether the item provided is present in the given store
items_obj = json.load(urllib2.urlopen('http://search.mobile.walmart.com/search?query='+item+'&store='+str(stores_obj[0]['no'])))
if items_obj['count'] == 0:
	print "No such item labelled "+ item +" in your nearest Walmart"
else:
	print item + " Found at " + stores_obj[0]['name']