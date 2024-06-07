#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


url="https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv"
df=pd.read_csv(url)


# In[32]:


df.sample(10)


# In[34]:


df["Name"].head(10)


# In[37]:


df.tail()


# In[6]:


df.info()


# In[40]:


df['Year'].unique()


# In[39]:





# In[ ]:




