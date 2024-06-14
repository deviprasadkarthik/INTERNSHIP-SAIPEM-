#!/usr/bin/env python
# coding: utf-8

# In[11]:


import mysql.connector 


cnx = mysql.connector.connect(user='root', password='12345678',
                                 host='127.0.0.1',
                                 database='python_sql1')
mysql_cursor=cnx.cursor()
mysql_cursor.execute("Select * from student") 
data=mysql_cursor.fetchall()


# In[13]:


import psycopg2


# In[18]:


postgres_con = psycopg2.connect(host="localhost", user="postgres", password="12345678", dbname="first")
postgres_cursor=postgres_con.cursor()
table_schema='''CREATE TABLE student(
                 id INTEGER,
                 name VARCHAR(50),
                 age INTEGER,
                 grade VARCHAR(50))'''
postgres_cursor.execute(table_schema)
postgres_con.commit()

                                


# In[20]:


for row in data:
    insert="INSERT INTO student(id,name,age,grade) VALUES(%s,%s,%s,%s)"
    postgres_cursor.execute(insert,row)
postgres_con.commit()

mysql_cursor.close()
cnx.close()
postgres_cursor.close()
postgres_con.close()


# In[ ]:




