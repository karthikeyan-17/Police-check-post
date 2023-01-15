#!/usr/bin/env python
# coding: utf-8

# # Police Dataset
# 
# Here,
# The data from a police check post is given.
# 
# I'm going to analyze this dataset using the Pandas DataFrame

# In[1]:


import pandas as pd


# In[3]:


df=pd.read_csv(r"C:\Users\Sathiyamurthy\Downloads\Police Data.csv")


# In[4]:


df


# # i)Remove the missing column that only contains missing values

# In[5]:


df.isnull().sum()


# In[6]:


df.drop(columns='country_name', inplace=True)


# In[7]:


df


# # ii) For Speeding, were Men or Women stopped more often?

# In[8]:


df.head()


# In[9]:


df[df.violation == 'Speeding'].driver_gender.value_counts()


# # Does gender affect who gets searched during a stop?

# In[10]:


df.groupby('driver_gender').search_conducted.sum()


# In[11]:


df.search_conducted.value_counts()


# # (mapping + data-type casting)
# 
# 
# # iv) what is the mean stop_duration?

# In[12]:


df.stop_duration.value_counts()


# In[14]:


df["stop_duration"]=df["stop_duration"].map({'0-15 Min' : 7.5,'16-30 Min' :24,'30+ Min' : 45})


# In[15]:


df


# In[17]:


df["stop_duration"].mean()


# # Groupby, Describe
# 
# # v) compare the age distributions for each violation

# In[20]:


df.groupby('violation').driver_age.describe()


# In[ ]:




