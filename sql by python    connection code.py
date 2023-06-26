#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[ ]:


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootuser",
  database="vineetdb1"
)
if mydb.is_connected():

    print("successfully connected")
else:
    print("issue to connect")


# In[ ]:


#inserting data into mysql table
# dekho table me vaule insert karne ke pahle 
# database aap banyenge mysql application se (installation ke baad)
# aur table chahe to application se bana le ya mysql CMD ke ander bhi bana sakte hai 
# aaage ki process python ke ander hogi in pysql


# In[ ]:


cursor=mydb.cursor()
code=int(input("entercode:"))
name=input("enter name:")
salary=int(input("enter salary:"))
query="Insert into emp values({},'{}',{})".format(code,name,salary)
cursor.execute(query)
mydb.commit()
print("inserted successfully")


# In[ ]:





# In[ ]:




