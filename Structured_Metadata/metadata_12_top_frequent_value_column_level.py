#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Calling relevant libraries
import sys
import pandas as pd
import os


# In[9]:


df=pd.read_excel('Ask A Manager Salary Survey 2021 (Responses).xlsx')


# In[22]:


#Function to calculate constancy
def constancy(lst):
    col = lst.value_counts().head(5)
    return col


# In[10]:


constancy(df['Job title'])

