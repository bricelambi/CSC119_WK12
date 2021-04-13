
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

sns.set(rc={'figure.figsize':(18.1, 8.27)}, font_scale = 0.7)

"""
STUDENT: Write a function that will take a parameter dataframe and the column to plot
         Set the default value of the parameter to tmax, return the axis object
"""

"""
STUDENT: Write a function that takes a begin and end index, dataframe, column name and new column name
         that will create a new column that is a substring using the begin and end index on the column
         name provided as a parameter.  Return the dataframe with the new column
"""

def main():
    df = pd.read_csv("cheyenne.csv")

    """
    STUDENT: Use your new functions to create a plot of annual average temperature
    """

    # ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    plt.savefig('daily_max.png')


if __name__ == "__main__": #need this to call main() function
    main()
