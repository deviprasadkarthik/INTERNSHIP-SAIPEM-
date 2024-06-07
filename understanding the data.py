#!/usr/bin/env python
# coding: utf-8

# # Ex3 - Getting and Knowing your Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[28]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[29]:


#url="https://github.com/justmarkham/DAT8/blob/master/data/u.user"
#df=pd.read_csv(url,sep='\t')


# In[30]:


df=pd.read_csv("/Users/deviprasadkarthikp/Downloads/u.csv")
df.sample(25)


# ### Step 3. Assign it to a variable called users and use the 'user_id' as index

# In[31]:


user=df.set_index("user_id", inplace = True)


# ### Step 4. See the first 25 entries

# In[102]:


users=df.copy()
users.head(25)


# ### Step 5. See the last 10 entries

# In[35]:


users.tail(10)


# ### Step 6. What is the number of observations in the dataset?

# In[38]:


users.info


# In[37]:


len(users)


# ### Step 7. What is the number of columns in the dataset?

# In[39]:


users.shape


# ### Step 8. Print the name of all the columns.

# In[41]:


print(users.columns)


# ### Step 9. How is the dataset indexed?

# In[46]:


users.index


# ### Step 10. What is the data type of each column?

# In[52]:


users.info()


# ### Step 11. Print only the occupation column

# In[53]:


print(users["occupation"])


# ### Step 12. How many different occupations are in this dataset?

# In[72]:


users["occupation"].unique()


# In[ ]:





# ### Step 13. What is the most frequent occupation?

# In[99]:


a= users["occupation"].value_counts()
print(a.index[0])


# ### Step 14. Summarize the DataFrame.

# In[100]:


users.describe().round(2)


# ### Step 15. Summarize all the columns

# In[101]:


users.describe(include='all').round(2)


# ### Step 16. Summarize only the occupation column

# In[93]:


users["occupation"].describe()


# ### Step 17. What is the mean age of users?

# In[90]:


users['age'].mean()


# ### Step 18. What is the age with least occurrence?

# In[91]:


users['age'].min()


# In[ ]:




