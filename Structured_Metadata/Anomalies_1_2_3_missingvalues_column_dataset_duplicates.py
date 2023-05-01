#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Anomalies Detection Algorithm: Missing Value
def missing_values(null_values, value_length):
    """
    Returns a list of equal length as input lists, where a 1 is returned for each element where
    null_values = 1 or value_length = 0, and a 0 is returned otherwise.
    """
    if len(null_values) != len(value_length):
        raise ValueError("Input lists must be of the same length.")
    
    missing_values = []
    for i in range(len(null_values)):
        if null_values[i] == 1 or value_length[i] == 0:
            missing_values.append(1)
        else:
            missing_values.append(0)
    
    return missing_values
null_values = [1, 0, 1, 0, 0]
value_length = [0, 5, 0, 3, 0]

result = missing_values(null_values, value_length)
print(result) 


# In[2]:


#Anomalies Detection Algorithm: column_duplicates
def finding_column_duplicates(input_):
    """
    Returns a binary number showing whether any columns have duplicates or not.  
    If the number of unique columns is less than the number of rows and the number of duplicates is greater than 0,
    the binary number is set to 1. Otherwise, the binary number is set to 0.
    """
    nrow = input_[0]
    n_unique = input_[1]
    n_duplicate = input_[2]

    if n_unique < nrow or n_duplicate > 0:
        return 1
    else:
        return 0


# In[3]:


input_ = [15,16, 17]

result = finding_column_duplicates(input_)
print(result) 


# In[4]:


#Anomalies Detection Algorithm: dataset_duplicates
def finding_dataset_duplicates(input_1):
    """
    Returns a binary number showing whether or not any rows have duplicates.
    If the number of unique columns is less than the number of rows and the number of row duplicates is greater than 0,
    the binary number is set to 1. Otherwise, the binary number is set to 0.
    """
    nrow = input_1[0]
    n_unique = input_1[1]
    n_duplicate_rows = input_1[2]

    if n_unique < nrow or n_duplicate_rows > 0:
        return 1
    else:
        return 0


# In[5]:


input_2 = [19,20,21]

result = finding_dataset_duplicates(input_2)
print(result) 


# In[ ]:




