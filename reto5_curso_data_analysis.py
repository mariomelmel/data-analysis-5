import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    years_extended = np.arange(1880, 2050, 1)
    line = [slope * xi + intercept for xi in years_extended]
    plt.plot(years_extended, line, color='orange')

    # Create second line of best fit
    current_years = df.iloc[120:135, 0]
    current_sea_levels = df.iloc[120:135, 1]
    slope, intercept, r_value, p_value, std_err = linregress(x=current_years, y=current_sea_levels)
    plt.scatter(x=current_years, y=current_sea_levels)
    years_extended = np.arange(2000, 2050, 1)
    line = [slope * xi + intercept for xi in years_extended]
    plt.plot(years_extended, line, color='red')

    # plt.show()
    plt.xticks(range(1880, 2051, 10))

    # Add labels and title
    plt.gca().update(dict(title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)'))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
