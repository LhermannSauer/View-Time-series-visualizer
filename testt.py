from datetime import date, datetime
import calendar
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df = pd.read_csv("fcc-forum-pageviews.csv", dtype={"date":np.str, "value":np.int32})

# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(0.975)) &
            (df['value'] >= df['value'].quantile(.025))]

# Prepare data for box plots (this part is done!)
df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['date'] = pd.to_datetime(df_box['date'], format='%Y-%m-%d')


# df_box['month'] = df_box['month']
# df_box['year'] = df_box['date'].dt.to_period('Y')

df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%m') for d in df_box.date]
df_box.sort_values(axis=1, by='month')
print(df_box.head())
fig, (ax1, ax2) = plt.subplots(1,2)
fig.set_figwidth(20)
fig.set_figheight(5)

#Draw box plots (using Seaborn)
sns.boxplot(ax=ax1, data=df_box, x='year', y='value', hue='year', width=1.0)
sns.boxplot(ax=ax2, data=df_box, x='month', y='value', hue='month',width=1.0)

ax1.set_title('Year-wise Box Plot (Trend)')
ax2.set_title('Month-wise Box Plot (Trend)')

# Save image and return fig (don't change this part)
fig.savefig('box_plot.png')