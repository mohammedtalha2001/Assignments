#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


data=pd.read_csv("netflixData.csv")
data


# In[9]:


plot=data["Production Country"].value_counts().head(20).to_numpy()
label= data["Production Country"].value_counts().head(20).keys()
plt.figure(figsize=(30,10))
sns.set(font_scale=1.5)
plt.bar(label,plot)
plt.show()


# In[ ]:




