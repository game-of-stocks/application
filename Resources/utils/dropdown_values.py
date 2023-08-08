#packages related to dataframes
import pandas as pd
import numpy as np
from pathlib import Path

#Grabing the raw stock data and putting in dataframe

#this line commented out needed for notes sample file
# raw_stocks_data_to_load =  Path("../Data/Stock_Index_Raw_Data.csv")
raw_stocks_data_to_load =  Path("Resources/Data/Stock_Index_Raw_Data.csv")
raw_stocks_data_df = pd.read_csv(raw_stocks_data_to_load, header=0, parse_dates=True)
raw_stocks_data_df.sort_index(ascending = True, inplace = True)
# raw_stocks_data_df.head()


## Creating Stock Drop Down Options 

#create new dataframe to only grab the unique values by company and only grabbing the columns needed 
dropdown_df = raw_stocks_data_df.drop_duplicates('Company').reset_index()
dropdown_df = dropdown_df[['Company', 'Ticker', 'Industry']]

#display new dataframe
# dropdown_df


#creating a array to store the values for the dropdown 
dropdown_options_array = ['']

# Loop through the DataFrame and concat the display names of the dropdown options and push into array
for index, row in dropdown_df.iterrows():
    dropdown_value = row['Company'] + ' ('+ row['Ticker'] + ')' +' - ' + row['Industry']
    dropdown_options_array.append(dropdown_value)
    
# remove the exchange index from list  
chars_to_remove = ['(SPX)', '(NDAQ)']
dropdown_options_array = [item for item in dropdown_options_array if not any(char in item for char in chars_to_remove)]

#display dropdown_options array 
# display(dropdown_options_array)