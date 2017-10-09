import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ipl_df = pd.read_csv('../data/ipl_dataset.csv', index_col=None)

def plot_matches_by_team():
    grouped = ipl_df.groupby(['batting_team'])
    df = grouped.agg({'match_code':'nunique'}).reset_index()
    x_len = len(df['batting_team'])
    plt.bar(np.arange(0,x_len), df['match_code'])
    plt.xticks(np.arange(0,x_len), df['batting_team'], rotation=45)
    plt.show()

# Solution
