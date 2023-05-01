#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def misfielded(z_score):
    threshold = 3
    # Convert array to numpy array
    import numpy as np
    np_z_score = np.array(z_score)
    d_type = np_z_score.dtype
    
    # Check array dimension
    z_score_shape = np_z_score.shape
    if len(z_score_shape) > 1:
        print('Condition_Misfielded: Input z_score contain Nested List')
        return() #Maybe Error code
    
    # Data type check for string
    data_type = d_type.type is np.str_
    
    if data_type:
        print('Condition_Misfielded: Input z_score contain string')
        return() #Maybe Error code
    
    output = [1 if i>=threshold else 0 for i in np_z_score]

    return output

