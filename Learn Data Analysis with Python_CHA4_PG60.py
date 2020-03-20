#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
Location = "C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


df = df.sort_values(by=['fname','age','grade'],ascending=[True, True, True])
df.head()


# In[ ]:




