#!/usr/bin/env python
# coding: utf-8

# # Ex1 - Filtering and Sorting Data

# This time we are going to pull data directly from the internet.
# Special thanks to: https://github.com/justmarkham for sharing the dataset and materials.
# 
# ### Step 1. Import the necessary libraries

# In[24]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv). 

# In[ ]:





# In[25]:


url="https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
df=pd.read_csv(url,sep='\t')


# In[69]:


df


# In[ ]:


### Step 3. Assign it to a variable called chipo.


# In[27]:


chipo=df.copy


# In[28]:


chipo.info()


# ### Step 4. How many products cost more than $10.00?

# In[43]:


chipo["item_price"]=chipo["item_price"].str.strip('$')
chipo.sample(10)


# In[75]:


result = chipo.loc[chipo['quantity'] == 1 & (chipo['item_price'] > 10)]
print(result)
result.count().unique()


# In[ ]:





# In[67]:


df.item_price = [float(value[1 : -1]) for value in df.item_price]


# In[68]:


chipo.query('item_price > 10').item_name.nunique()


# In[49]:


chipo['item_price'] = pd.to_numeric(chipo['item_price'], errors='coerce')
chipo['item_price'] = chipo['item_price'].fillna(0)
chipo['item_price'] = chipo['item_price'].round().astype(int)
print(chipo)


# In[56]:


duplicates = chipo.drop_duplicates(subset=['item_name'])
duplicates1 = chipo.drop_duplicates(subset=['quantity'])



# In[54]:


count=0
if quantity==1 and item_price>10:
    count+=1
print(count)
    


# ### Step 5. What is the price of each item? 
# ###### print a data frame with only two columns item_name and item_price

# In[57]:


df[['item_name', 'item_price']]


# ### Step 6. Sort by the name of the item

# In[60]:


a=chipo.sort_values(by='item_name')
print


# ### Step 7. What was the quantity of the most expensive item ordered?

# In[65]:


chipo.sort_values(by = "item_price", ascending = False).head(1)


# ### Step 8. How many times was a Veggie Salad Bowl ordered?

# In[78]:


chipo[chipo.item_name == 'Veggie Salad Bowl'].shape[0]


# In[ ]:





# ### Step 9. How many times did someone order more than one Canned Soda?

# In[76]:


chipo[(chipo.item_name == 'Canned Soda') & (chipo.quantity > 1)].shape[0]


# In[ ]:




