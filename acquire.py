#!/usr/bin/env python
# coding: utf-8

# In[1]:


# set up necessary imports
import env
import os
import pandas as pd


# In[2]:


# creating a connection to connect to the Codeup Student Database
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[3]:


def get_telco_data():
    '''This function will connect to the Codeup Student Database. It will then cache a local copy to the computer to use for later
        in the form of a CSV file. If you want to reproduce the results, you will need your own env.py file and database credentials.'''
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index = False)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''
    SELECT * FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)''' , get_connection('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df  



