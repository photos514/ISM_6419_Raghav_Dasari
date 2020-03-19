#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import glob


# In[15]:


import os
os.getcwd()


# In[16]:


os.chdir('C:\\Users\\rdasari\\Desktop')


# In[17]:


os.getcwd()


# In[18]:


all_data = pd.DataFrame()
for f in glob.glob("C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\weekly_call_data\\weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[19]:


all_data.head()


# In[25]:


all_data.count()

