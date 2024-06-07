#!/usr/bin/env python
# coding: utf-8

# # Occupation

# ### Introduction:
# 
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user). 

# In[3]:


df=pd.read_csv("/Users/deviprasadkarthikp/Downloads/u.csv")
df.sample(25)


# ### Step 3. Assign it to a variable called users.

# In[4]:


users=df.copy()
users.sample(10)



# In[5]:


users.tail(10)


# In[6]:


users.info


# In[7]:


users.info()


# ### Step 4. Discover what is the mean age per occupation

# In[8]:


users.groupby('occupation').age.mean()


# ### Step 5. Discover the Male ratio per occupation and sort it from the most to the least

# In[11]:





# ### Step 6. For each occupation, calculate the minimum and maximum ages

# In[9]:


print(users.groupby('occupation').age.min())
print(users.groupby('occupation').age.max())


# ### Step 7. For each combination of occupation and gender, calculate the mean age

# In[10]:


users.groupby('occupation').age.agg(['min', 'max'])


# ### Step 8.  For each occupation present the percentage of women and men

# In[12]:


ocup = users.groupby(['occupation', 'gender']).agg({'gender': 'count'})
occup_count = users.groupby(['occupation']).count()
occup_gender = ocup.div(occup_count, level = "occupation")
occup_gender.loc[:, 'gender']


# In[ ]:




