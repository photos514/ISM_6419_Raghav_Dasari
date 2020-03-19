#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


get_ipython().system('pip install xlrd')
print('xlrd installed!')


# In[4]:


import os
os.getcwd()


# In[5]:


os.chdir('C:\\Users\\rdasari\\Desktop')


# In[6]:


os.getcwd()


# In[11]:


df_can = pd.read_csv('C:\\Users\\rdasari\\Desktop\\all_040_in_12.P1.csv')


# In[12]:


df_can.head()

