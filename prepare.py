import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import RFE, SelectKBest, f_regression
from sklearn.linear_model import LinearRegression, TweedieRegressor, LassoLars

import acquire

############################## IMPUTE MISSING VALUES  ##############################

def impute(df, strategy, column_list):
    ''' 
    take in a df strategy and column list
    return df with listed columns imputed using input strategy
    '''
    #create imputer   
    imputer = SimpleImputer(strategy=strategy)
    #fit/transform selected columns
    df[column_list] = imputer.fit_transform(df[column_list])

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

############################## PREP OD DEATHS ##############################

def prep_set(df):
    #use function from acquire.py
    df = acquire.od_deaths_df()

    #drop columns
    df = df.drop(columns=['Unnamed: 0', 'ID', 'DateType', 'ResidenceCounty','ResidenceState', 'DeathCounty', 'InjuryCounty','InjuryState', 'ResidenceCityGeo', 'InjuryCityGeo', 'Other', 'OtherSignifican', 'LocationifOther', 'DeathCityGeo', 'InjuryCity'])  

    #handle null values
    #impute with mean for numeric column
    df = impute(df, 'mean', ['Age'])
    #imputing with most frequent value for descrete columns
    df = impute(df, 'most_frequent', ['Date', 'Sex', 'Race','ResidenceCity', 'DeathCity', 'Location', 'DescriptionofInjury', 'InjuryPlace', 'MannerofDeath']) 

    #change ACCIDENT to Accident for uniformity
    df = df.replace({'MannerofDeath': 'ACCIDENT'}, {'MannerofDeath': 'Accident'})
    #change accident to Accident for uniformity
    df = df.replace({'MannerofDeath': 'accident'}, {'MannerofDeath': 'Accident'})
    
    #change race options
    df = df.replace({'Race': 'Asian, Other'}, {'Race': 'Other'})
    df = df.replace({'Race': 'Asian Indian'}, {'Race': 'Other'})   
    df = df.replace({'Race': 'Chinese'}, {'Race': 'Other'}) 
    df = df.replace({'Race': 'Native American, Other'}, {'Race': 'Other'})
    df = df.replace({'Race': 'Hawaiian'}, {'Race': 'Other'}) 
    df = df.replace({'Race': 'Hispanic, White'}, {'Race': 'Hispanic'}) 
    df = df.replace({'Race': 'Hispanic, Black'}, {'Race': 'Hispanic'}) 

    # create dummy columns for race
    race_dummies = pd.get_dummies(df.Race)
    # add dummy columns to df
    df = pd.concat([df, race_dummies], axis=1)

    #change datatype
    df.Age = df.Age.astype(int)
    df.Fentanyl_Analogue = df.Fentanyl_Analogue.astype(int)

    return df

