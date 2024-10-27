import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data =pd.read_csv('../datasets/processed.csv')

data['date'] = pd.to_datetime(data['date'], errors='coerce')
data.dropna(subset=['date'], inplace=True)
data['month_year'] = data['date'].dt.to_period('M').astype(str)
data['year'] = data['date'].dt.to_period('Y').astype(str)


plt.figure(figsize=(10, 6))
port_values = data.groupby('port_name')['value'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=port_values.values, y=port_values.index, color='skyblue')
plt.title('Top 10 Ports by Total Entries')
plt.xlabel('Total Entries')
plt.ylabel('Port Name')
plt.show()


monthly_data = data.groupby(['month_year', 'port_name'])['value'].sum().unstack().fillna(0)
yearly_data = data.groupby(['year', 'port_name'])['value'].sum().unstack().fillna(0)

# Line plot of entries over time (year)
plt.figure(figsize=(10, 6))
sns.lineplot(data=data, x='year', y='value', hue='border', marker=" ")
plt.title('Entries Over Time by Border (Year)')
plt.xlabel('Year')
plt.ylabel('Number of Entries')
plt.xticks(rotation=90)
plt.legend(title='Border')
plt.show()


# Heatmap: Entries by Year and Port
yearly_sums = data.groupby('year')['value'].sum()
yearly_sums_df = yearly_sums.reset_index()
heatmap_data = yearly_sums_df.pivot_table(values='value', index='year')
plt.figure(figsize=(10, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.0f', cbar_kws={'label': 'Total Entries'})
plt.title('Entries by Year and Port')
plt.xlabel('Port Name')
plt.ylabel('Year')
plt.xticks(rotation=45)
plt.show()

