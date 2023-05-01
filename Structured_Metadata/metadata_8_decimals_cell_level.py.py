


import pandas as pd
def calculate_decimal_values(my_list):
    op_list=[] # output list
    for  i in my_list:
        decimal_places = str(i).split('.')[1]
        if decimal_places =='0':
            op_list.append(0)
        else: 
            op_list.append(len(decimal_places))
    return op_list## output list with number of decimal points in input list respectively.
def calculate_value_length(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    df[numeric_cols] = df[numeric_cols].fillna(0)
    op_df = pd.DataFrame()
    for num_col in numeric_cols:
        decimal_length_list = calculate_decimal_values(df[num_col].tolist())
        op_df[num_col] = decimal_length_list
    return op_df
file_path ="Ask A Manager Salary Survey 2021 (Responses) - Form Responses 1.csv"
df = calculate_value_length(file_path)






