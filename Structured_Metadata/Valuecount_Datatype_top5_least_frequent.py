#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

current_dir = os.getcwd()
print(current_dir)


# In[2]:


#To determine value count,output is one final list.
import pandas as pd

# defining a function called 'count_values' which takes 'file_path' as input
def count_values_1(file_path):
    # read csv file using pandas read_csv function and store in 'df' variable
    df = pd.read_csv(file_path)
    
    # create an empty list called 'output' to store the value counts of each column
    output = []
    
    # loop through each column of dataframe
    for col in df.columns:
        # create an empty list called 'value_counts' to store the value counts of each row in column
        value_counts = []
        
        # loop through each row of the column and count the number of times each unique value appears in the column
        for value in df[col]:
            # check if value is null, if yes, append 0 to the 'value_counts' list, else count the number of times the value appears in the column
            if pd.isnull(value):
                value_counts.append(0)
            else:
                count = df[col].value_counts()[value]
                value_counts.append(count)
        # append the 'value_counts' list to the 'output' list
        output.extend(value_counts)
    # return the 'output' list containing value counts of each column
    return output

file_path = 'Dataset.csv'
counts = count_values_1(file_path)
print(counts)


# In[3]:


#To determine Datatype,output is one final list.
import pandas as pd

# Read in the CSV dataset
df = pd.read_csv('Dataset.csv')

# Create an empty list to store the data types of each value
d_types_1 = []

# Loop through each column in the DataFrame
for col in df.columns:
    # Loop through each value in this column
    for value in df[col]:
        # Check for empty string or NA values
        if pd.isna(value):
            d_types_1.append('unknown')
        elif value == '':
            d_types_1.append('empty string')
        else:
            # Determine the data type of the value and add it to the list
            d_types_1.append(type(value).__name__)

# Print the list of data types for each value
print(d_types_1)


# In[4]:


#To determine Inconstancy, output is one final list.
import pandas as pd

def find_least_frequent(file_path):
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(file_path, skiprows=[0])
    
    # Create an empty list to store the output
    output = []
    
    # Loop through each column in the dataframe
    for col in df.columns:
        # Convert the column to a list
        column_list = df[col].tolist()
        
        # Determine the frequency of each unique value in the column using pandas value_counts() function
        frequency = pd.Series(column_list).value_counts()
        
        # Get the top 5 least frequent values in the column
        least_frequent = frequency.tail(5)
        
        # Append the column name and the top 5 least frequent values to the output list
        for value in least_frequent.index.tolist():
            if value not in output:
                output.append(value)
    
    # Return the output list
    return output

file_path = 'Dataset2.csv'
output = find_least_frequent(file_path)
print(output)


# In[ ]:




