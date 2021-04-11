# importing libraries
import sys
import os.path
import logging
import pandas as pd
from pandas.core.common import flatten

logging.basicConfig(level=logging.DEBUG)

# getting filename as argument
filename = sys.argv[1]

# check if file exist or not
if os.path.isfile(filename):
  try:
    logging.info("Read employee excel file")
    employee_df = pd.read_excel(filename)

    logging.info("Normalize date columns in standard format")
    employee_df['Date of Birth'] = pd.to_datetime(employee_df['Date of Birth'], errors='coerce')
    employee_df['Date of Joining'] = pd.to_datetime(employee_df['Date of Joining'], errors='coerce')

    logging.info("Concat column FirstName and LastName to get Full Name")
    employee_df['Employee Name'] = employee_df['First Name'] + ' ' + employee_df['Last Name']

    logging.info("Employee list based on quarter of joining")
    print(employee_df.groupby('Quarter of Joining')['Employee Name','Date of Birth'].apply(lambda g: list(flatten(g.sort_values('Date of Birth').drop(['Date of Birth'],axis=1).values.tolist()))).to_dict())

  except Exception as error:
    print('Caught this error: ' + repr(error))
else:
  raise Exception(filename+" does not exist")

