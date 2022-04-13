#!/usr/bin/env python
# coding: utf-8

# In[13]:



from bs4 import BeautifulSoup
import requests


def main(URL):
    reqs = requests.get(URL)

# extract all the text 
# the GET request
    content = reqs.text

# convert the text to a beautiful soup object
    soup = BeautifulSoup(content, 'html.parser')

# Empty list to store the output
    urls = []

# For loop that iterates over all the tags
    for h in soup.findAll(class_="prFeature"):
	
	# looking for anchor tag inside the tag
        a = h.find(class_="prFeatureName")
	
        try:
		
		# looking for href inside anchor tag
            if 'href' in a.attrs:
			
			# storing the value of href
                url = a.get('href')
			
			# appending 
                urls.append(url)
			
	
        except:
            pass

# print
    for url in urls:
        print('https://www.industrybuying.com/electronics-robotics-4097'+url)
if __name__ == '__main__': 
    file = open("D:/datas/Desktop/9.txt", "r")

# iterating over the urls
    for links in file.readlines():
        main(links)


# In[ ]:




