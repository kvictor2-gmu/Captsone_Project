import numpy as np

gen_output_list = []
for reading in given_input_list:
    if isinstance(reading, str) and reading.lower() in ['null', 'nan', 'n/a', '']:
        gen_output_list.append(1)
    elif isinstance(reading, float) and np.isnan(reading):
        gen_output_list.append(1)
    else:
        gen_output_list.append(0)

print(gen_output_list)
