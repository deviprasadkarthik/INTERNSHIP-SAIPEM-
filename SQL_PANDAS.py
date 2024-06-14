#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install sqlalchemy psycopg2-binary


# In[23]:


import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


import mysql.connector 


cnx = mysql.connector.connect(user='root', password='12345678',
                                 host='127.0.0.1',
                                 database='python_sql')
# cnx.close()


# In[1]:


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:12345678@localhost/first')
connection = engine.connect()


# In[ ]:





# In[13]:


df = pd.read_sql_table('eci_data_2024',engine)


# In[14]:


df.head()


# In[15]:


df.tail()


# In[16]:


df.info()


# In[17]:


df['State'].unique()


# In[21]:


df['Party'].unique()


# In[42]:


plt.figure(figsize=(10, 10))
df_ = df.groupby('Party', as_index=False).sum()
df_top10 = df_.sort_values(by='Total Votes', ascending=False).head(10)
plt.pie(df_top10  ['Total Votes'], labels=df_top10['Party'], autopct='%1.1f%%', startangle=140)
plt.title('Votes Distribution by Party')
plt.show()


# In[35]:


plt.figure(figsize=(12, 6))
plt.bar(df['State'], df['Total Votes'], color='brown')
plt.xlabel('State')
plt.ylabel('Number of Votes')
plt.title('Number of Votes by State')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[41]:


top_candidate = df.head(5)
plt.figure(figsize=(10, 10))
plt.bar(top_candidate['Candidate'], top_candidate['Total Votes'], color='orange')
plt.xlabel('Candidate')
plt.ylabel('Number of Votes')
plt.title('Top Candidate with Most Votes')
plt.show()


# In[ ]:




