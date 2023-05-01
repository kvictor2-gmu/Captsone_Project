#!/usr/bin/env python
# coding: utf-8

# # Value Length by Cell level 

# In[2]:


given_input_list = ['Timestamp', '4/27/2021', '4/27/2021', 'How old are you?', '25-34', '25-34', 'What industry do you work in?', 'Education (Higher Education)', 'Computing or Tech', 'Job title', 'Research and Instruction Librarian', 'Change & Internal Communications Manager', 'If your job title needs additional context, please clarify here:', 'High school, FT', 'Data developer/ETL Developer', 'What is your annual salary? (You\'ll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)', '55000', '54600', 'How much additional monetary compensation do you get, if any (for example, bonuses or overtime in an average year)? Please only include monetary compensation here, not the value of benefits', '0', '4000', 'Please indicate the currency', 'USD', 'USD', 'If "Other," please indicate the currency here:', '', '', 'If your income needs additional context, please provide it here:', '', 'I work for a Charter School', 'What country do you work in?', 'United States', 'USA', 'If you\'re in the U.S., what state do you work in?', 'Massachusetts', 'Tennessee', 'What city do you work in?', 'Boston', 'Chattanooga', 'How many years of professional work experience do you have overall?', '5-7 years', '8 - 10 years', 'How many years of professional work experience do you have in your field?', '5-7 years', '2 - 4 years', 'What is your highest level of education completed?', 'Master\'s degree', 'College degree', 'What is your gender?', 'Woman', 'Non-binary', 'What is your race? (Choose all that apply.)', 'White', 'Hispanic, Latino, or Spanish origin, White']

gen_output_list = [len(str(x)) for x in given_input_list]

print(gen_output_list)


# In[ ]:




