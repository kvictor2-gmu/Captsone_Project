#!/usr/bin/env python
# coding: utf-8

# In[43]:


def z_score(raw_input):
    from scipy import stats #ref: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.zscore.html
    import numpy as np
    
    # Convert array to numpy array
    np_input = np.array(raw_input)
    d_type = np_input.dtype
    
    # Check array dimension
    input_shape = np_input.shape
    if len(input_shape) > 1:
        print('Warning: Nested List detected')
        return() #Maybe Error code
    
    # Data type check for string
    data_type = d_type.type is np.str_
    
    if data_type:
        print('Warning: List contain string')
        return() #Maybe Error code
    
    # Calculate z score
    np_output = stats.zscore(np_input,axis = None)
    
    output = np.ndarray.tolist(np_output)
    
    # Check output length
    if len(raw_input) != len(output):
        print('Warning: Potential Input problem, Output length mismatch')
    
    
    return(output)

