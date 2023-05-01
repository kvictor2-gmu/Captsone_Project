#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
#Creating a dataframe variable to call the Dataset
df=pd.read_excel('Ask A Manager Salary Survey 2021 (Responses).xlsx')
df.drop(['Timestamp','Unnamed: 18', 'Unnamed: 19', 
                'Unnamed: 20', 'Unnamed: 21','Unnamed: 22','Unnamed: 23'], axis=1, inplace=True)


# In[17]:


#The actual code
def dup_df(da):
    
    #Number of rows
    df_len=len(da)
    
    #Number of duplicates
    df_dup=da.duplicated().values.sum()
    
    #Number of uniques 
    df_uni=df_len-df_dup
    
    #Storing the output
    lis=[df_len,df_uni,df_dup]
    
    # Reference for user:No. of rows, uniques and duplicates
    return lis


# In[18]:


dup_df(df)

