import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE, SelectKBest, f_regression
from sklearn.linear_model import LinearRegression, TweedieRegressor, LassoLars

import acquire

############################## NULL VALUES ##############################

def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    ''' 
    take in a dataframe and a proportion for columns and rows
    return dataframe with columns and rows not meeting proportions dropped
    '''
    # calc column threshold
    col_thresh = int(round(prop_required_column*df.shape[0],0)) 
    # drop columns with non-nulls less than threshold
    df.dropna(axis=1, thresh=col_thresh, inplace=True) 
    # calc row threshhold
    row_thresh = int(round(prop_required_row*df.shape[1],0))  
    # drop columns with non-nulls less than threshold
    df.dropna(axis=0, thresh=row_thresh, inplace=True) 
    
    return df   

############################## IMPUTE MISSING VALUES  ##############################

def impute(df, my_strategy, column_list):
    ''' 
    take in a df strategy and cloumn list
    return df with listed columns imputed using input stratagy
    '''
    #create imputer   
    imputer = SimpleImputer(strategy=my_strategy)
    #fit/transform selected columns
    df[column_list] = imputer.fit_transform(df[column_list])

    return df

############################## PREP ZILLOW  ##############################

def prep_od(df):
    '''
    This function takes in the od_deaths_df acquired ,
    then drops or nulls all null values
    Returns a cleaned od_deaths_df.
    '''
    #import from acquire.py
    df = acquire.od_deaths_df

    #replace blank spaces and special characters
    df = df.replace(r'^\s*$', np.nan, regex=True)

    #handle null values
    #drop using threshold
    df = handle_missing_values(df, prop_required_column = .5, prop_required_row = .5)
    #impute continuous columns using mean
    df = impute(df, 'mean', ['Age'])
    # imputing descrete columns with most frequent value
    df = impute(df, 'most_frequent', ['Date', 'DateType', 'Sex', 'Race','ResidenceCity', 'DeathCity', 'Location', 'DescriptionofInjury', 'InjuryPlace', 'MannerofDeath']) 

    #replace values in MannerofDeath for uniformity
    #change ACCIDENT to Accident for uniformity
    df = df.replace({'MannerofDeath': 'ACCIDENT'}, {'MannerofDeath': 'Accident'})
    #change accident to Accident for uniformity
    df = df.replace({'MannerofDeath': 'accident'}, {'MannerofDeath': 'Accident'})   

    #change dtype
    df.Age = df.Age.astype(int)

    return df

############################## OD DEATHS SPLIT ##############################

def od_deaths_split(df, target):
    '''
    This function take in get_zillow  from aquire.py and performs a train, validate, test split
    Returns train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test
    and prints out the shape of train, validate, test
    '''
    #create train_validate and test datasets
    train, test = train_test_split(df, train_size = 0.8, random_state = 123)
    #create train and validate datasets
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123)

    #Split into X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]

    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]

    X_test = test.drop(columns=[target])
    y_test = test[target]

    # Have function print datasets shape
    print(f'train -> {train.shape}')
    print(f'validate -> {validate.shape}')
    print(f'test -> {test.shape}')
   
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test