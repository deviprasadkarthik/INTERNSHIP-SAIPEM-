#!/usr/bin/env python
# coding: utf-8

# # US - Baby Names

# ### Introduction:
# 
# We are going to use a subset of [US Baby Names](https://www.kaggle.com/kaggle/us-baby-names) from Kaggle.  
# In the file it will be names from 2004 until 2014
# 
# 
# ### Step 1. Import the necessary libraries

# In[9]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv). 

# In[10]:


url="https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv"
df=pd.read_csv(url)


# ### Step 3. Assign it to a variable called baby_names.

# In[11]:


baby_name=df.copy()
baby_name.sample(10)


# ### Step 4. See the first 10 entries

# In[7]:


baby_name.head(25)


# In[8]:


baby_name.tail()


# ### Step 5. Delete the column 'Unnamed: 0' and 'Id'

# In[31]:


baby_name.drop('Id' ,axis=1)


# In[32]:


baby_name.drop('Unnamed: 0' ,axis=1)


# ### Step 6. Is there more male or female names in the dataset?

# In[33]:


baby_names.Gender.value_counts()


# ### Step 7. Group the dataset by name and assign to names

# In[19]:


names = baby_name.drop('Year', axis = 1).groupby('Name').sum()


# In[20]:


names


# ### Step 8. How many different names exist in the dataset?

# In[41]:


baby_names["Name"].nunique()


# ### Step 9. What is the name with most occurrences?

# In[44]:


baby_names.groupby('Name').Count.sum().sort_values(ascending = False)


# ### Step 10. How many different names have the least occurrences?

# In[26]:


names[names.Count == names.Count.min()].shape[0]


# ### Step 11. What is the median name occurrence?

# In[ ]:





# ### Step 12. What is the standard deviation of names?

# In[23]:


baby_name.groupby('Name').Count.sum().std()


# ### Step 13. Get a summary with the mean, min, max, std and quartiles.

# In[24]:


baby_name.describe()


# In[ ]:




