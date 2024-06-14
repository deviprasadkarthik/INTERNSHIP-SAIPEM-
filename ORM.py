#!/usr/bin/env python
# coding: utf-8

# In[12]:


from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql+mysqlconnector://root:12345678@localhost/python_sql1',echo=False)
Session=sessionmaker(bind=engine)
session=Session()
Base=declarative_base()
class Student(Base):
    __tablename__='student'
    
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    age=Column(Integer)
    grade=Column(String(50))
Base.metadata.create_all(engine)


# insert
# In[3]:


student1=Student(id=1,name="karthik",age=21,grade="GRADUATION")
student6=Student(id=6,name="i",age=21,grade="GRADUATION")
session.add_all([student1,student6])
session.commit()


# In[4]:


student2=Student(id=2,name="devi",age=21,grade="GRADUATION")
student3=Student(id=3,name="prasad",age=21,grade="GRADUATION")
student4=Student(id=4,name="palakurthy",age=21,grade="GRADUATION")
session.add_all([student2,student3,student4])
session.commit()


# # update
# 

# In[29]:


student=session.query(Student).filter(Student.name=='i').first()
student.name='THILAK'
session.commit()


# # delete
# 

# In[30]:


student=session.query(Student).filter(Student.name=="devi").first()
session.delete(student)
session.commit()


# In[ ]:




