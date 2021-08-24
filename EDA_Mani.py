#!/usr/bin/env python
# coding: utf-8

# IMPORTING LIBRARIES

# In[33]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# READING DATA

# In[6]:


file_data="F:\\popind.csv"
my_data=pd.read_csv(file_data,index_col="Year")


# DATA WITH NaN VALUES

# In[5]:


my_data


# In[7]:


my_data.isnull().sum()


# DATA AFTER REMOVING NaN VALUES

# In[35]:


my_data=my_data.dropna()
my_data


# In[ ]:


DIFFERENT TYPES OF PLOTS ARE SHOWN HERE


# In[14]:


sns.lineplot(data=my_data["Population"],label="Population")
plt.title("Indian Population Growth")
plt.xlabel("Year")
plt.ylabel("Growth Rate")


# In[37]:


plt.figure(figsize=(15,5))
sns.barplot(x=my_data.index, y=my_data["Population"])
plt.title("Indian Population Growth")
plt.xlabel("Year")
plt.ylabel("Growth Rate")


# In[15]:


plt.figure(figsize=(10,5))
sns.heatmap(data=my_data, annot=True)


# In[22]:


file_dataa="F:\\IndiaPopulation.csv"
my_dataa=pd.read_csv(file_dataa,index_col="Year")
sns.relplot(x='Population',y='GrowthRate',data=my_dataa)


# In[24]:


sns.distplot(x = my_data['Population'], bins = 10)


# In[19]:


sns.jointplot(x = my_dataa['Population'], y =my_dataa['GrowthRate'], kind = 'scatter')


# In[26]:


sns.stripplot(y =my_data['Population'], x = my_data['GrowthRate'])


# In[ ]:




