#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing relevant libraries
import pandas as pd
import sys
import os


# In[11]:


df=pd.read_excel('Ask A Manager Salary Survey 2021 (Responses).xlsx')


# In[18]:


def cell_size(lst):
    
    # Blank dictionary to story cell size info
    c_size = []

    # Iterating through each column and row to get the cell size information
    for a in lst:
        c_size.append(sys.getsizeof(a))
        
    return c_size


# In[19]:


#The output
cell_size(df['Job title'])

