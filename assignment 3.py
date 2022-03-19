#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np


# In[9]:


data = pd.read_csv("netflix.csv")
data.head()


# In[10]:


def cast_len(val):
    if val == "None":
        return 0
    else:
            return len(str(val).split(", "))


# In[12]:


data["cast"].isnull().sum()


# In[13]:


data["cast"].replace(np.nan, "None", inplace=True)


# In[ ]:


data.tail()


# In[14]:


data["Cast_Member"] = data["cast"].apply(cast_len)


# In[15]:


data.tail()


# In[3]:


data.groupby(["type","genre",]).count()


# In[16]:


data.groupby(["release_year","type"]).count()


# In[17]:


data.loc[0:10,["type","country"]]


# In[ ]:




