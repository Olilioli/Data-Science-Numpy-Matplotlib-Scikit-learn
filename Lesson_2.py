#!/usr/bin/env python
# coding: utf-8

# In[9]:


### Вычисления с помощью Numpy


# In[ ]:


### Задание 1


# In[ ]:


import numpy as np


# In[12]:


a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])


# In[13]:


mean_a = a.mean(axis = 0)


# In[5]:


mean_a


# In[10]:


### Задание 2


# In[14]:


a_centered = np.subtract(a, mean_a)


# In[15]:


a_centered


# In[16]:


### Задание 3


# In[18]:


ac1 = a_centered[:, 0]


# In[19]:


ac2 = a_centered[:, 1]


# In[21]:


a_centered_sp = np.dot(ac1,ac2)


# In[22]:


a_centered_sp


# In[24]:


N = a.shape[0]


# In[25]:


N


# In[26]:


my_cov = a_centered_sp / (N-1)


# In[27]:


my_cov


# In[ ]:


### Задание 4**


# In[28]:


np.cov(a.transpose())


# In[ ]:




