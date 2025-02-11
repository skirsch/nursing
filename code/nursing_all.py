'''
This is the most recent version of the nursing code

This was run on the most recent CMS US nursing home data in 2025.

See CFR_graphs.xlsx and the nursing_grouped tab.

data source: https://data.cms.gov/covid-19/covid-19-nursing-home-data/data


Write a csv file of groupings for the nursing home data for resident covid cases, covid deaths and all deaths 
grouped by week and state.

Create the file by running the current script.

'''

import pandas as pd
import csv # for the quoting option on output
from datetime import timedelta

# expand these files locally from the nursing.zip file
source_file="../data/all.csv"

output_file="../analysis/nursing_grouped.csv"

def read_nursing_csv(filename):
    """
    Processes the CSV file, calculates summary statistics, and returns both dataframes.

    Args:
        file_path (str, optional): Path to the source data file. Defaults to an array of "../data/nursing/faclevel_{year}".

    Returns:
        tuple: A tuple containing the DataFrame containing the 
    """
    print("reading file...")

    selected_cols = ['Week Ending', 'Provider State', 'Residents Weekly Confirmed COVID-19',
                     'Residents Weekly COVID-19 Deaths','Residents Weekly All Deaths', 'Total Number of Occupied Beds',    
                     ]
    
    # Read the data files into a DataFrame
  

    df = pd.read_csv(filename, usecols=selected_cols, 
                      dtype={'Provider State':str},
                      parse_dates=['Week Ending'])

    #group by week ending and state

    grouped_df = df.groupby(['Week Ending', 'Provider State'], as_index=False).sum()

    # ok so this is our final source dataframe with lots of info.
    # so we can do various groupby analyses on it.
    return grouped_df

def write_df_to_csv(df1, filename):
  """Writes a pandas DataFrame to a CSV file.

  Args:
    df: The pandas DataFrame to write.
    filename: The name of the CSV file to create.

  """
  # don't muck with the original

  
  print("writing file to disk...", filename)
  
  # make sure strings have quotes around them to ensure excel doesn't interpret 12-15 as a date
  # quoting=csv.QUOTE_NONNUMERIC will quote dates which is a problem
  df.to_csv(filename, index=False, quoting=csv.QUOTE_NONE)

df=read_nursing_csv(source_file) 
write_df_to_csv(df, output_file)
