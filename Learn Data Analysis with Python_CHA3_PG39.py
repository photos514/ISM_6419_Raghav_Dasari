#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
Location = "C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[6]:


#Can you create a column for timemgmt that shows busy 
#if a student exercises more than three hours per week AND studies more than seventeen hours per week?

df['timemgmt'] = np.where((df['exercise'] > 3) & (df['hours'] > 17),'busy', 'not busy')
df.tail(10)


# In[ ]:




