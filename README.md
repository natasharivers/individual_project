![image](https://user-images.githubusercontent.com/80594235/125494606-d979da7d-a93b-490b-a5ea-7989cc6cc06a.png)

# Individual Project-  Drug Related Overdose Deaths

## Natasha Rivers
### July 14, 2021

______________________________________________________________________________________________________

## Abstract
Being able to better understand the drug epidemic that has ripped across our country may help save the lives of those who are syffering from drug addiction. I chose to use age as the target variable in this project. Being able to target individuals of specific ages may allow us the create programs for that specific age range and possibly save lives. I created several visualizations, hypothesis tests and models to show the data. Ultimately, the OLS model performed best, outperforming the LassoLars, TweedieRegressor and the baseline models.  


## Goals
- To determine if age plays a roll in drug related overdose deaths
- Create models that can predict age of individuals who are deceased due to drug overdose

______________________________________________________________________________________________________

## Deliverables

- An easily accessible Final Notebook
- A Readme.md that explains this project, details the planning process and allows for reproducibility

______________________________________________________________________________________________________

## Data Dictionary


| Target                  |       Datatype       |  Definition           |
|-------------------------|----------------------|-----------------------|
| Age                     | 5105 non-null: int64 | Age at time of death  |


| Feature                 |       Datatype         |    Definition                                      |
|-------------------------|------------------------|:--------------------------------------------------:|
|Date                     |5105 non-null: object   |date of reported death                              |
|Sex                      |5105 non-null: object   |gender of deceased                                  |
|Race                     |5105 non-null: object   |race of deceased                                    |
|RecidenceCity            |5105 non-null: object   |City where individual lived                         |
|DeathCity                |5105 non-null: object   |City where individual died                          |
|Location                 |5105 non-null: object   |physical location of death                          |
|DescriptionofInjury      |5105 non-null: object   |cause of injury                                     |
|InjuryPlace              |5105 non-null: object   |physical location where individual was injured      |
|COD                      |5105 non-null: object   |reason why individual died                          |
|Heroin                   |5105 non-null: int64    |in system at time of death (Boolean)                |
|Cocain                   |5105 non-null: int64    |in system at time of death (Boolean)                |
|Fentanyl                 |5105 non-null: object   |in system at time of death (Boolean)                |
|Fentanyl_Analogue        |5105 non-null: int64    |in system at time of death (Boolean)                |
|Oxycodone                |5105 non-null: int64    |in system at time of death (Boolean)                |
|Oxymorphine              |5105 non-null: int64    |in system at time of death (Boolean)                |
|Ethanol                  |5105 non-null: int64    |in system at time of death (Boolean)                |
|Hydrocodone              |5105 non-null: int64    |in system at time of death (Boolean)                |
|Benzodiazepine           |5105 non-null: int64    |in system at time of death (Boolean)                |
|Methodone                |5105 non-null: int64    |in system at time of death (Boolean)                |
|Amphet                   |5105 non-null: int64    |in system at time of death (Boolean)                |
|Tramad                   |5105 non-null: int64    |in system at time of death (Boolean)                |
|Morphone_NotHeroin       |5105 non-null: object   |in system at time of death (Boolean)                |
|Hydromorphone            |5105 non-null: int64    |in system at time of death (Boolean)                |
|OpiateNOS                |5105 non-null: int64    |in system at time of death (Boolean)                |
|AnyOpiod                 |5105 non-null: object   |in system at time of death (Boolean)                |
|MannerofDeath            |5105 non-null: object   |the way in which the individual died                |
|Black                    |5105 non-null: int64    |Race (Boolean)                                      |
|Hispanic                 |5105 non-null: int64    |Race (Boolean)                                      |
|Other                    |5105 non-null: int64    |Race (Boolean)                                      |
|Unknown                  |5105 non-null: int64    |Race (Boolean)                                      |
|White                    |5105 non-null: int64    |Race (Boolean)                                      |


______________________________________________________________________________________________________

## Hypothesis

#### Hypothesis 1: T-Test (continuous vs discrete)
- Null Hypothesis: There is a relationship between Age and White Race drug overdose deaths
- Alternate Hypothesis: There is not a relationship between Age and With Race drug overdose deaths

<br>

#### Hypothesis 2: T-Test (continuous vs discrete)
- Null Hypothesis: There is a relationship between Age and Oxycodone drug overdose deaths
- Alternate Hypothesis: There is not a relationship between Age and Oxycodone drug overdose deaths

<br>

#### Hypothesis 3: T-Test (continuous vs discrete)
- Null Hypothesis: There is a relationship between Age and Heroin drug overdose deaths
- Alternate Hypothesis: There is not a relationship between Age and Heroin drug overdose deaths

<br>

#### Hypothesis 4: $X^2$ Test (discrete vs discrete)
- Null Hypothesis: There is a relationship between Heroin and Oxycodone drug overdose deaths
- Alternate Hypothesis: There is not a relationship between Heroin and Oxycodone drug overdose deaths


______________________________________________________________________________________________________

## Pipeline Steps
 
### --> Plan:
- Use Trello Board to organize thoughts
    - Link is available here: https://trello.com/b/GgCFkLpp/individual-project

<br>

### --> Acquire:
- Data was acquire from: https://www.kaggle.com/ruchi798/drug-overdose-deaths
- Function created to acquire data and return a Pandas DataFrame

<br>

### --> Prepare:
- Created a function (prep_set) that did the following:  
    - dropped several columns with high null value 
        - were not significant if only had ~10% of data
    - filled null values by imputing
        - using mean and most frequent
    - changed data for uniformity in Manner of Death
    - corrected options for 'Race' so that it would not be so vast
    - changed data type in 'Age' from float to integer
    - created dummy columns for race
    
<br>

- Created a function to split data 
    - split data into train, validate, test using Age as the target
    - prints out shape of all three sets

    
<br>

### --> Explore:
- Univariate Exploration
- Bivariate Exploration
- Multivariate Exploration
- Hypothesis Testing

<br>

### --> Model: 
- OLS model performs better than the baseline and other predictive models
- The drop of between train and validate was not significant

### --> Deliver: 
- Final Notebook for peer review
______________________________________________________________________________________________________

## Reproduction

- Read this README.md
- Download the aquire.py, prepare.py, and Final_Notebook.ipynb files into your working directory
- Run the Final_Notebook.ipynb notebook

