#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#To Determine Datatype
import pandas as pd
import numpy as np
def determine_data_type(data):
    # Create an empty list to store the data types of each value
    d_types = []

    # Loop through each value in the input list
    for value in data:
        # Check for None or missing values
        if value is None or pd.isna(value)== True:
            d_types.append('unknown')
        elif value == '' or value == " ":
            d_types.append('empty string')
        else:
            # Determine the data type of the value and add it to the list
            d_types.append(type(value).__name__)

    # Return the list of data types for each value
    return d_types
data_1 = [1, "A", '',None, True, 2, True, 4, "D",np.NaN, True, 5, "A", False, 6, "B", True, 7, "C", False, 8, "D", False]
d_types = determine_data_type(data_1)
print(d_types)

