#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#Creating a dataframe variable to call the Dataset
df=pd.read_excel('Ask A Manager Salary Survey 2021 (Responses).xlsx')


# In[2]:


def col_dup(lst):
    
    if len(lst.shape)==1:
        
        #Number of rows
        c_len=len(lst)
        
        #Number of uniques
        uni=lst.nunique()
        
        #Number of duplicates
        dups=c_len-uni
    
        
        #Storing the output in a dictinary 
        final_lst=[c_len,uni,dups]
        
        #As a reference for user: No. of rows, uniques and duplicates   
        return final_lst
    else:
        print('Warning: Input needs to be single list')     


# In[3]:


col_dup(df['Job title'])


# In[ ]:




