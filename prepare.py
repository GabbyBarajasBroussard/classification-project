#!/usr/bin/env python
# coding: utf-8

# In[1]:


# First I am setting up the notebooke with the necessary imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings("ignore")

from acquire import get_telco_data


# In[2]:


# now I am naming my dataframe telco and calling it from the csv file made in the acquire file.
telco= pd.read_csv("telco.csv")
telco.info()


# In[3]:


#ensure that any duplicate customers are removed from the dataframe
telco.drop_duplicates(subset=['customer_id'], keep='last')


# In[4]:


#making single variable columns
telco['years_tenure'] = telco.tenure / 12
telco['is_family']=telco["partner" or "dependents"] == 'Yes'
telco['is_senior']=telco["senior_citizen"]== "Yes"
telco['has_phones']= telco['phone_service' or 'multiple_lines']== 'Yes'
telco['has_paperless_billing']= telco['paperless_billing']=='Yes'
telco['has_streaming']= telco["streaming_tv" or "streaming_movies"] == 'Yes'
telco['has_support_features']= telco['device_protection' or 'tech_support']=='Yes'
telco['has_security_features']= telco['online_security' or 'online_backup'] =='Yes'


# In[5]:


#making dummy variables
telco_dummies = pd.get_dummies(telco.churn, drop_first=True)
telco_dummies.head(3)


# In[6]:


# attaching the dummy variables onto the data frame
telco = pd.concat([telco, telco_dummies], axis=1)
#renaming the column from yes to is_churn for clarity
telco= telco.rename(columns={'Yes': 'is_churn'})
#ensuring that the dummy variables are attached to the dataframe
telco.head(3)


# In[7]:


# removing id columns and string variable columns
telco= telco.drop(columns=["churn","paperless_billing","device_protection", "tech_support", "senior_citizen","phone_service", "streaming_tv", "streaming_movies", "partner","dependents","online_security", "online_backup","Unnamed: 0","customer_id","payment_type_id","tenure","contract_type_id", "internet_service_type_id"])
telco.head()


# In[8]:


#checking the Dtypes and Columns of my clean dataframe
telco.info()


# In[9]:


def clean_telco(cached=True):
    '''This function acquires and prepares the telco data from a local csv, default. Passing cached=False acquires fresh data from sql and writes to csv. Returns the telco df with dummy variables encoding churn'''
    # use my aquire function to read data into a df from a csv file
    df = get_telco_data()
    # drop duplicates
    df.drop_duplicates(inplace=True)
    #making single variable columns
    df['monthly_tenure'] = df.tenure / 12
    df['is_family']=df["partner" and "dependents"] == 'Yes'
    df['is_couple']=df["partner"]=="Yes"
    df['is_senior']=df["senior_citizen"]== "Yes"
    df['has_phones']= df['phone_service' or 'multiple_lines']== 'Yes'
    df['has_paperless_billing']= df['paperless_billing']=='Yes'
    df['has_streaming']= df["streaming_tv" or "streaming_movies"] == 'Yes'
    df['has_support_features']= df['device_protection' or 'tech_support']=='Yes'
    df['has_security_features']= df['online_security' or 'online_backup'] =='Yes'
    # create dummy columns for churn
    telco_dummies = pd.get_dummies(df.churn, drop_first=True)
    
    # add dummy columns to df
    df = pd.concat([df, telco_dummies], axis=1)
    # rename dummy columns
    df= df.rename(columns={'Yes': 'is_churn'})
    # removing id columns and string variable columns
    df= df.drop(columns=["churn","paperless_billing","device_protection", "tech_support", "senior_citizen","phone_service", "streaming_tv", "streaming_movies", "partner","dependents","online_security", "online_backup","Unnamed: 0","customer_id","payment_type_id","tenure","contract_type_id", "internet_service_type_id"])
    return df

# In[10]:
#combining my split, train, test data and my clean data into one dataframe
def prep_telco_data():
    df = clean_telco()
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.is_churn)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.is_churn)
    return train, validate, test