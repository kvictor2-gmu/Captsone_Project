#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#To Determine Valuecount
import numpy as np

# Define the function to count the number of occurrences of each value in the input list
def value_count(data):
    output = []  # Create an empty list to store the count of each value
    for value in data:  # Loop through each value in the input list
        if pd.isna(value)== True or value is None or value == '' or value == " " :  # Check if the value is NaN, None, an empty string or a whitespace
            output.append(0)  # If the value is NaN, None, an empty string or a whitespace, append 0 to the output list
        else:
            count = sum([1 for val in data if val == value])  # I count the number of occurrences of the value in the input list
            output.append(count)  # Append the count of the value to the output list
    return output

#Input list
data_2 = [1, "A", np.NaN, None, True, 2, True, 4, "D", True, 5, "A", False, 6, "B", True, 7, "C", False, 8, "D", None]

counts = value_count(data_2)

# Print the output list
print(counts)

