
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

############################## Plot Univariate ##############################


def explore_univariate(train, cat_vars, quant_vars):
    for var in cat_vars:
        explore_univariate_categorical(train, var)
        print('_________________________________________________________________')
    for col in quant_vars:
        p, descriptive_stats = explore_univariate_quant(train, col)
        plt.show(p)
        print(descriptive_stats)

############################## Plot Bivariate ##############################

def explore_bivariate(train, target, cat_vars, quant_vars):
    for cat in cat_vars:
        explore_bivariate_categorical(train, target, cat)
    for quant in quant_vars:
        explore_bivariate_quant(train, target, quant)
