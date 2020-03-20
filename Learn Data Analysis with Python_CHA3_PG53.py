#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
Location = "C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[7]:


df.take(np.random.permutation(len(df))[:500])


# In[ ]:




