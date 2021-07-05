import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")

print(df.head())


# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(0.975)) &
            (df['value'] >= df['value'].quantile(.025))]


def draw_line_plot():
    fig, ax = plt.subplots(1,1,figsize=(40,10))
    ax.plot(df)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily FCC forum page views 5/16 to 12/19")
    ax.set_facecolor('#95d2a5')
    ax.set_xticks(np.linspace(*ax.get_xbound(), 10))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot

    fig, ax = plt.figure()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)




    fig, ax = plt.figure()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
