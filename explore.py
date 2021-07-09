
import matplotlib.pyplot as plt
import seaborn as sns


############################## PLOT Target vs Variables ##############################

def plot_against_target(df, target, var_list, figsize = (12,6), hue = None):
    '''
    This function takes in dataframe, target and variable list, 
    and plots those variables against target. 
    '''
    for var in var_list:
        plt.figure(figsize = (figsize))
        sns.regplot(data = df, x = var, y = target, 
                    line_kws={'color': 'orange'})
        plt.show()