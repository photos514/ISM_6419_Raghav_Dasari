#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 


# In[9]:


import os
os.getcwd()


# In[10]:


os.chdir('C:\\Users\\rdasari\\Desktop')


# In[11]:


os.getcwd()


# In[14]:


file = r'C:\\Users\\rdasari\\Desktop\\HSG05.xls'
df = pd.read_excel(file)


# In[15]:


df.head()


# In[ ]:




