#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd

def unpack_sql_results(sql_results, column_names):
    print('\t'.join(column_names))
    for row in sql_results:
        print('\t'.join(map(str, row)))
    df = pd.DataFrame(sql_results, columns=column_names)
    return df


column_names = ['PROJECTS', 'NUMBER OF LINES']



A = input("Enter the SQL data as a list of tuples: ")


sql_results = eval(A)

df = unpack_sql_results(sql_results, column_names)

print(df)


# In[ ]:




