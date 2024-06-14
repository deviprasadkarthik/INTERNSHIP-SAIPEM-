#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import psycopg2 as pg
import sqlalchemy  as s

mysql_engine = s.create_engine('mysql+mysqlconnector://root:12345678@localhost/python_sql1')
print(mysql_engine)
df = pd.read_sql_query('Select * from student', mysql_engine)


# In[ ]:


with create_engine('postgresql+psycopg2://postgre:12345678@localhost/first')as con:
     df.to_sql('student1', con, if_exists='replace', index=False)
     print(con)    
print(f'Table {table_name} migrated successfully from MySQL to PostgreSQL.')


# In[ ]:





# In[ ]:




