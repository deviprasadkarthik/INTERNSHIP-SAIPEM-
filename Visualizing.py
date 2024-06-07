#!/usr/bin/env python
# coding: utf-8

# # Visualizing Chipotle's Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# set this so the graphs open internally
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# ### Step 3. Assign it to a variable called chipo.

# In[3]:


url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df=pd.read_csv(url,sep="\t")


# In[4]:


chipo=df.copy()


# ### Step 4. See the first 10 entries

# In[5]:


chipo.head(10)


# In[6]:


chipo.tail(10)


# In[7]:


chipo.info()


# ### Step 5. Create a histogram of the top 5 items bought

# In[8]:


chipo.item_name.value_counts()[0:5].plot(kind='bar')

plt.xlabel('Items')
plt.ylabel('Number of Times Ordered')
plt.title('Most ordered Chipotle\'s Items')


# ### Step 6. Create a scatterplot with the number of items orderered per order price
# #### Hint: Price should be in the X-axis and Items ordered in the Y-axis

# In[12]:


chipo["item_price"]=chipo["item_price"].str.strip("$")

chipo.sample(10)


# In[14]:


chipo["item_price"]=chipo["item_price"].astype("float")


# In[17]:


o = chipo.groupby('order_id').sum()
plt.scatter(x = o.item_price, y = o.quantity, s = 50, c = 'indigo')
plt.xlabel('price')
plt.ylabel(' ordered')
plt.title('Number of items ordered per order price')


# ### Step 7. BONUS: Create a question and a graph to answer your own question.

# In[ ]:




