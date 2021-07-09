#################### INDIVIDUAL PROJECT####################

#import libraries
import pandas as pd

#################### ACQUIRE INDIVIDUAL PROJECT####################

def od_deaths_df():
    '''
    This function reads in the od_deaths_df csv 
    and turns it into a pandas dataframe
    '''
    df = pd.read_csv('drug_deaths.csv')
          
    return df