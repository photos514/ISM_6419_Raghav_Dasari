#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
from sqlalchemy import create_engine


# In[28]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db
db_file = r'C:\\Users\\rdasari\\Downloads\\datasets\\datasets\\salesdata.db'
engine = create_engine(r"sqlite:///{}"
.format(db_file))
sql = 'SELECT * from scores'
sales_data_df = pd.read_sql(sql, engine)
sales_data_df

