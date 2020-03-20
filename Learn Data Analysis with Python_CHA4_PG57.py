#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[19]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=GradeList,columns=['Names','Grades','BSD','MSD','PhD'])
df


# In[17]:


df['Grades'].count() # number of values


# In[20]:


df['Grades'].mean() # arithmetic average


# In[21]:


df['Grades'].std() # standard deviation


# In[22]:


df['Grades'].min() # minimum


# In[23]:


df['Grades'].max() # maximum


# In[24]:


df['Grades'].quantile(.25) # first quartile


# In[25]:


df['Grades'].quantile(.5) # second quartile


# In[26]:


df['Grades'].quantile(.75) # third quartile


# In[27]:


df['Grades'].mean()


# In[28]:


df['Grades'].mode()


# In[29]:


df['Grades'].var()


# In[ ]:




