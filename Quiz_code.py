#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
df = pd.read_csv(r'C:\Hamoye\FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='gbk' )


# In[12]:


df.head()


# In[15]:


#Question 11
df.groupby('Item').sum()


# In[17]:


#Question 12 and 14
df.describe(include = 'all')


# In[18]:


#Question 13
df.isnull().sum()


# In[26]:


#Question 19
df.groupby('Area')['Y2018'].sum()


# In[18]:


df.shape


# In[21]:


#Question 17 and 18
df.groupby('Element')['Y2018'].sum()


# In[4]:


#Question 20
country = df.drop_duplicates()


# In[14]:


#Question 20
country = df['Area'].unique()
print(country)


# In[6]:


#Question 16
df.groupby('Element')['Y2014'].sum()


# In[8]:


#Question 15
df.groupby('Element').sum()


# In[ ]:




