#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path = "C:/Users/HP/Downloads/food_coded.csv"


# In[3]:


df = pd.read_csv(path)


# In[5]:


df.head()


# In[6]:


df.columns


# In[8]:


ndf = df[['cook','eating_out','employment','ethnic_food', 'exercise','fruit_day','income','on_off_campus','pay_meal_out','sports','veggies_day']]
ndf.head()


# In[9]:


ndf.tail()


# In[10]:


#data exploration and visualization
import seaborn as sns


# In[12]:


sns.pairplot(ndf)


# In[ ]:




