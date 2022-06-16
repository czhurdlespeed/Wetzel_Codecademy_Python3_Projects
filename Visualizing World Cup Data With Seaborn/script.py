import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')

print(df.head())

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

print(df.head())
sns.set_style('whitegrid')
sns.set_context('poster',font_scale = 0.7)
plt.bar(df['Year'], df['Total Goals'], data = df)
#help(plt.bar)
plt.show()

f, ax = plt.subplots(figsize = (12,7))
ax = sns.barplot(x = 'Year', y = 'Total Goals', data = df)
plt.xticks(rotation = 45)
ax.set_title('World Cup Goals 1930-2014')
plt.show()
help(sns.barplot)

df_goals = pd.read_csv('goals.csv')
print(df_goals.head())


f,ax2 = plt.subplots(figsize= (12, 7))
sns.set_context('notebook',font_scale = 1.25)

ax2 = sns.boxplot(x = 'year', y = 'goals', data = df_goals, palette = 'Spectral')
plt.xticks(rotation = 45)
plt.title('World Cup Goal Distributions 1930-2014')


plt.show()
