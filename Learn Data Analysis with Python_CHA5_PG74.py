#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,83,77,78,95]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,
columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', '')
df.plot()


# In[24]:


import matplotlib.pyplot as plt
df.plot()
displayText = "Bob's 76 that says “Wow!”"
xloc = 1
yloc = df['Grades'].max()
xtext = -30
ytext = 0
plt.annotate(displayText,xy=(xloc, yloc),xytext=(xtext,ytext),xycoords=('axes fraction', 'data'),textcoords='offset points')


# In[ ]:




