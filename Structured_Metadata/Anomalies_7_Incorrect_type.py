# -*- coding: utf-8 -*-
"""Anomalies detection incorrect type.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ix45CBDhPi_Qh15uXD_kFhM0JrKfY0mY
"""

#Sample Input Column
Data_col = [1.3,2.2,3.3,1.3,2.2,3.3,2.4,2.4,1.3,2.2,3.3,2.4,1.3,2.2,3.3,2.4,"p","r",3.3,True,3.3,8.3,9.3,6.3,5.6,5.3,4.3,4.3,3.3,"hl","by",False,5.6,6.7,343.3,4,5,4,3,3.3,2.3,3.3,3.3,3.3,3.3,3,34,4.2,4.2,4.2,4.2,4.2,4.2,4.2,4.2,4,4,4,4,3,3 ]

# Create a dictionary to keep track of counts of each data type
data_type_counts = {}

# Loop over each row in the specified column and increment the count of the data type
for value in Data_col:
    data_type = type(value)
    if data_type not in data_type_counts:
        data_type_counts[data_type] = 0
    data_type_counts[data_type] += 1

# Find the most frequently occurring data type
most_common_data_type = max(data_type_counts, key=data_type_counts.get)

# Calculate the 10% frequency threshold
frequency_threshold = data_type_counts[most_common_data_type] * 0.1
flag_types = []
# Flag all data types with counts less than the threshold
for data_type, count in data_type_counts.items():
    if count < frequency_threshold:
      flag_types.append(data_type)


#Declaration of output 
Output_col=[]

for value in Data_col:
    data_type = type(value)
    if data_type in flag_types:
        Output_col.append(1)
    else:
      Output_col.append(0)

print(Output_col)