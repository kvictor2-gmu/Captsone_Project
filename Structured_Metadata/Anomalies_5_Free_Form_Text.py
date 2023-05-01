#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
#Creating a dataframe variable to call the Dataset
df=pd.read_excel('Ask A Manager Salary Survey 2021 (Responses).xlsx')
df.head()


# In[3]:


def free_form(lst):
    if len(lst.shape)==1 and lst.dtype==object:
        f_lst=lst.str.len().apply(lambda x:1 if x>50 else 0)
        return f_lst
    else:
        print('Warning: Input should be a string type and/or single list')


# In[4]:


free_form(df['Job title'])


# In[5]:


free_form(df[['Job title','How old are you?']])


# In[ ]:




