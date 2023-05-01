#!/usr/bin/env python
# coding: utf-8

# In[1]:


def finding_outliers(z_scores):
    # Create an empty output list
    output_list = []

    # Loop through each z-score in the input list
    for z in z_scores:

        # Check if the absolute value of the z-score is greater than 3
        if abs(z) > 3:

            # If it is, append 1 to the output list
            output_list.append(1)
        else:
            # Otherwise, append 0 to the output list
            output_list.append(0)
    
    # Return the output list
    return output_list


# In[2]:


Z_scores = [1,2,2,3,50,9,1,5,48,39]

result = finding_outliers(Z_scores)
print(result) 


# In[ ]:




