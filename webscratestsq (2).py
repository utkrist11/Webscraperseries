#!/usr/bin/env python
# coding: utf-8

# In[72]:


#!/usr/bin/env python
# coding: utf-8

# In[11]:


from bs4 import BeautifulSoup
import requests


def main(URL):
    # op file append mode
    File = open("D:/datas/Desktop/1234.csv", "a")

    # specifying user agent
    HEADERS = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
               'Accept-Language': 'en-US, en;q=0.5'})

    # HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # product title
    try:
        # Outer Tag Object
        title = soup.find(
            "span", attrs={'class': 'productTitle fullWidth'})
        title_value = title.string

        # Title as a string value
        title_string = title_value.strip().replace(',', '')
        #File.write(f"{title_string}")

    except AttributeError:
        title_string = "NA"
    print("product Title = ", title_string)
    
    
    
  
    # savingtitle in file
    # File.write(f"{title_string},")

    # retrieving price

    price = soup.find_all("div", attrs={'class': 'mainPrice'})
    for ftr in price:
        p1 = ftr.find(class_="price")
        p2 = p1.text.replace(',','').replace('\n','').replace(' ','')
            #File.write(f"{p2}")
        #for span in price:
            #print("product price = "span.text)
       # price = price.find("span").string.strip().replace(',', '')
    #except AttributeError:
        #p2 = "NA"
        print("Product price = ",p2)
        File.write(f"{p2}")
    
     # retrieving price
    try:
        pricewithgst = soup.find(
            "span", attrs={'class': 'AH_PricePerPiece'}).string.strip().replace(',', '')
    except AttributeError:
        pricewithgst = "NA"
    print("Products price gst = ", pricewithgst)

    # saving
    # File.write(f"{price},")

    try:
        discount = soup.find(
            "span", attrs={'id': 'AH_Discount'}).string.strip().replace(',', '')
    except AttributeError:
        discount = "NA"
    print("Products discount = ", discount)

    # saving
    # File.write(f"{discount},")

    # retrieving product description
    try:
        description = soup.find("div", attrs={'id': 'description'})
        description = description.find(
            "p", attrs={'class': 'mart'}).string.strip().replace(',', '')
    except AttributeError:

        try:
            description = soup.find("p", attrs={'class': 'mart'}).find_all(
                'p').string.strip().replace(',', '')
        except:
            description = "NA"
    print("Description = ", description)

    # File.write(f"{description},")

    # rating
    try:
        ratings = soup.find("div", attrs={'class': 'pro-review-star'})
        ratings = ratings.find("p").string.strip().replace(',', '')

    except AttributeError:
        ratings = "NA"
    print("Ratings = ", ratings)
    # File.write(f"{ratings},")

    File.write(
        f"{title_string} , {pricewithgst} ,{discount} ,{description} , {ratings} ,")
    
       #image 
    img_src = soup.find("div", attrs={'class': 'squzeImgae'})
    img_src = img_src.find("img")['src']
    print("image_url = ", img_src)
    File.write(f"{img_src}")
    
    
    #product url    
    url = soup.find("link", attrs={'rel': 'canonical'})
    url1 = url.get("href")
    #if 'href' in url:
			
			# storing the value of href
                #url1 = url.get('href')
    print("page url = ", url1)
    File.write(f"{url1}")  
    
    #keywords
    keywords = soup.find("meta", attrs={'name': 'keywords'})
    keywords1 = keywords.get("content")
    print("keywords = ", keywords1)
    File.write(f"{keywords1}")
    
    #brandlink products
    brand = soup.find("div", attrs={'class': 'interlink'})
    brand1 = brand.find("span")
    brand2 = brand1.find("a")
    if 'href' in brand2.attrs:
        brandlink = brand2.get("href")
    print("brand_link = https://industrybuying.com"+brandlink)
    File.write(f"{brandlink}")
    
    

    # print featurename status

    # feature1 = soup.find_all("div", attrs={'class': 'featureNamePr'})
    # for ftr in feature1:
    #     abc = ftr.find(class_="featureNamePr")
    #     xyz = ftr.text.replace(' ', '').replace('\n', '')
    #     File.write(f"{xyz} ,")

    #     print("featureName = ", xyz)

    # # featureslist
    # divTag = soup.find_all("div", attrs={'class': 'featureValuePr'})
    # for tag in divTag:
    #     unwanted = tag.find('span')
    #     v = unwanted.extract()
    #     value1 = tag.text.replace('  ', '').replace('\n', '')
    #     File.write(f"{value1} ,")
    #     print("featuresofproduct = ", value1)

    feature1 = soup.find_all("div", attrs={'class': 'featureNamePr'})
    divTag = soup.find_all("div", attrs={'class': 'featureValuePr'})

    for ftr, tag in zip(feature1, divTag):
        xyz = ftr.text.replace(' ', '').replace('\n', '').replace(': :', ' :')
        value1 = tag.text.replace('  ', '').replace('\n', '')
        File.write(f"{xyz} {value1} ,")
        print(f"{xyz} {value1} ")
        
        
        
 
    
    # saving  and closing the line
    File.write("\n")

    # closing the file
    File.close()



if __name__ == '__main__': 
    file = open("D:/datas/Desktop/lol.txt", "r")

# iterating over the urls
    for links in file.readlines():
        main(links)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




