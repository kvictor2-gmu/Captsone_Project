#!/usr/bin/env python
# coding: utf-8

# In[1]:


def z_score_value_length(raw_input):
    from scipy import stats #ref: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html
    import numpy as np
    
    # Get value length
    #ref: https://www.geeksforgeeks.org/find-the-length-of-each-string-element-in-the-numpy-array/
    value_length = [len(i) for i in raw_input]
    
    # Convert array to numpy array
    np_value_length = np.array(value_length)
    d_type = np_value_length.dtype
    
    # Check array dimension
    value_length_shape = np_value_length.shape
    if len(value_length_shape) > 1:
        print('Warning: Nested List detected')
        return() #Maybe Error code
    
    # Data type check for string
    data_type = d_type.type is np.str_
    
    if data_type:
        print('Warning: Calculated length contain string')
        return() #Maybe Error code
    
    # Calculate z score
    np_output = stats.zscore(np_value_length,axis = None)
    
    output = np.ndarray.tolist(np_output)
    
    # Check output length
    if len(raw_input) != len(output):
        print('Warning: Potential Input problem, Output length mismatch')
    
    
    return(output)

