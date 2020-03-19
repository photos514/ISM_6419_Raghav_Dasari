#!/usr/bin/env python
# coding: utf-8

# In[16]:


from pandas import DataFrame, read_csv
import pandas as pd 


# In[17]:


import os
os.getcwd()


# In[18]:


os.chdir('C:\\Users\\rdasari\\Desktop')


# In[19]:


os.getcwd()


# In[20]:


file = r'C:\\Users\\rdasari\\Desktop\\HSG05.xls'
df = pd.read_excel(file)


# In[21]:


df.head()


# In[ ]:




