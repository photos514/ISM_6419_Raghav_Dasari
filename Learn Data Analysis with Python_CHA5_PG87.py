#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])


# In[2]:


import pandas as pd
import numpy as np
Location = "C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot(kind='scatter', x='hours', y='grade')


# In[ ]:




