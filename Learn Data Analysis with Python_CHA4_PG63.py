#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
Location = "C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[17]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours',data=df).fit()
result.summary()


# In[18]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ exercise + hours',data=df).fit()
result.summary()


# In[28]:


#Create a new column where you convert gender to numeric values, like
#1 for female and 0 for male. Can you now add gender to your regression?
#Does this improve your R-squared?

df['gender2'] = df['gender'].replace(['female','male'],[1,0])


# In[29]:


df.head()


# In[31]:


import statsmodels.formula.api as sm
result = sm.ols(formula='grade ~ age + exercise + hours + gender2',data=df).fit()
result.summary()


# In[ ]:




