#!/usr/bin/env python
# coding: utf-8

# In[13]:


list=[1,2,3,4,5,6,7,8,9]
list.append(10)
print(list)


# In[14]:


import pandas as pd


# In[19]:


df=pd.DataFrame({'NAME':["A","B","C"],'MARKS':[22,33,44]})


# In[20]:


df


# In[42]:


import numpy as np


# In[43]:


n1=np.array([1,2,3,4,5])
n1


# In[44]:


n2=np.array([[1,2,3,4,5],[1,2,3,4,5]])
n2


# In[45]:


type(n2)


# In[46]:


nz=np.zeros((10,9))# 10 are rows and 9 are columns number 
nz


# In[47]:


nf=np.full((5,5),15)
nf


# In[48]:


n1=np.array([1,2,3,4,5])
n2=np.array([10,20,30,40,50])


# In[53]:


np.column_stack((n2,n1))


# In[55]:


n1=np.arange(1,5)
n1


# In[6]:


import matplotlib as mpl


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




