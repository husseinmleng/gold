#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup
import csv


# In[2]:


url = 'http://goldpricez.com/eg/gram'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')


# In[15]:


soup.find('table', attrs={"id":"gold_price_table2"}).find_all('tr')


# In[22]:


my_list = [i.get_text().strip() for i in soup.find('table', attrs={"id":"gold_price_table2"}).find_all('td')]


# In[23]:


my_list


# In[24]:


units = [my_list[i] for i in range(0,len(my_list),2)]
units


# In[37]:


prices = [my_list[i] for i in range(1,len(my_list),2)]
# prices = [float(i.split()[0]) for i in prices]
prices


# In[38]:


data = {unit: price for unit, price in zip(units,prices)}
data


# In[34]:


with open("Gold.csv",'w') as csv_file:
    writer = csv.DictWriter(csv_file,fieldnames=["Unit", "Price"])
    writer.writeheader()
    for key, value in data.items():
        writer.writerow({"Unit":key,"Price":value})


# In[ ]:





# In[ ]:




