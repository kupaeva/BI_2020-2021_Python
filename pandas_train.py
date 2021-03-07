#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib as plt


# In[3]:


path = '/home/kupaeva/Документы/train.csv'


# In[4]:


df = pd.read_csv(path)


# In[7]:


df


# In[33]:


df = df.rename(df.pos, axis='index')


# In[95]:


mean_fraction = df[['A_fraction', 'T_fraction', 'G_fraction', 'C_fraction']]


# In[96]:


mean_fraction


# In[97]:


mean_fraction = mean_fraction.apply(lambda row: row.fillna(1 - row.sum()), axis=1)


# In[98]:


mean_fraction


# In[93]:


mean_fraction.plot(kind='bar', stacked=True, figsize=(20, 10),color = ['gold', 'darkcyan', 'skyblue', 'violet'], 
                   xlabel = 'position of nucleotide', ylabel = 'part of nucleotide', )


# In[109]:


df.matches


# In[111]:


great_matches = df.loc[df.matches > df.matches.mean()]


# In[114]:


great_matches = great_matches[['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']]


# In[ ]:


great_matches.to_csv(path_or_buf = '/home/kupaeva/Документы/train_part.csv')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




