#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from urllib import error
from html import unescape
import requests
import json 
from bs4 import BeautifulSoup
import time


# In[2]:


def download(method,url,param=None,data=None, timeout=1, maxretries=10):
    headers ={"user-agent":"#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    #res = requests.request(method,url,param=param,data=data,headers=headers)
    
    try:
        resp=requests.request(method, url,params=param,data=data, headers=headers)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500<=e.response.status_code<600 and maxretries>0:
            print(maxretries)
            
            download(method,url,param,data,timeout,maxretries-1)
        else:
            print(e.response.status_code)
            print(e.response.reason)
    return resp
    


# In[ ]:




