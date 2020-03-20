#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
Location = "C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[14]:


# Create the bin dividers
bins = [70,80]


# In[15]:


# Create names for the four groups
group_names = ['pass', 'fail']


# In[17]:


df['Status'] = ['pass' if x > 80 else 'fail' for x in df['grade']] 
df.head()


# In[ ]:




