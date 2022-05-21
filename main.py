import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#importing data, merging into one csv
observations = pd.read_csv('observations.csv', skipinitialspace=True)
species = pd.read_csv('species_info.csv', skipinitialspace=True)

observations = observations.sort_values('observations', ascending=True).drop_duplicates(['scientific_name', 'park_name'], keep= 'first').sort_index()
species_names_temp = species.groupby(['scientific_name'])['common_names'].apply(', '.join).reset_index()

species_names = pd.merge(species, species_names_temp, on= 'scientific_name', how= 'left')
species_names= species_names.drop(columns= 'common_names_x')

species_names.rename(columns= {'common_names_y': 'common_names'}, errors="raise", inplace= True)

species_names['common_names'] = species_names['common_names'].str.replace(' ,', ',')
species_names['common_names'] = species_names['common_names'].str.replace(', ', ',')
species_names['common_names'] = species_names['common_names'].str.split(',').apply(lambda x : ', '.join(set(x)))

species_names['conservation_status'] = species_names['conservation_status'].replace(np.nan, 'No Danger')
species_names['conservation_group'] = pd.Categorical(species_names['conservation_status'], ordered=True, categories=['No Danger', 'In Recovery', 'Species of Concern', 'Threatened', 'Endangered'])

species_names = species_names.sort_values('conservation_group', ascending=True).drop_duplicates(['scientific_name'], keep= 'last')

species_names = species_names.drop('conservation_group', 1)
merged = pd.merge(species_names, observations, on= 'scientific_name', how= 'left')
#merged.to_csv('merged.csv')

#observation by park
observations_by_park = merged.groupby('park_name')[['observations']].sum()
indices = ['Bryce National Park', 'Great Smoky Mountains National Park', 'Yellowstone National Park', 'Yosemite National Park']
sns.set(rc={'figure.figsize':(12,7)})
ax = sns.barplot(data= observations_by_park, x=indices, y= 'observations')
plt.title('Total observations by park')
plt.yticks(range(0,2000000,500000))
ax.ticklabel_format(axis = 'y', useOffset=False, style = 'plain')
ax.set_xlabel('Park name')
ax.set_ylabel('Total observations')
plt.show()

#overall percent of each species endangered
category_status_count = merged.groupby(['category', 'conservation_status'])[['scientific_name']].nunique().unstack('conservation_status')
category_status_count = category_status_count.droplevel(0, axis=1).fillna(value=0)
percentages = [a+b+c+d+e for a,b,c,d,e in zip(category_status_count['No Danger'],
                                              category_status_count['Species of Concern'],
                                              category_status_count['In Recovery'],
                                              category_status_count['Threatened'],
                                              category_status_count['Endangered'])]
ndbar = [i / j * 100 for i,j in zip(category_status_count['No Danger'], percentages)]
scbar = [i / j * 100 for i,j in zip(category_status_count['Species of Concern'], percentages)]
irbar = [i / j * 100 for i,j in zip(category_status_count['In Recovery'], percentages)]
tbar = [i / j * 100 for i,j in zip(category_status_count['Threatened'], percentages)]
ebar = [i / j * 100 for i,j in zip(category_status_count['Endangered'], percentages)]

barWidth = 0.3
species_name = category_status_count.columns.tolist()
fig, ax = plt.subplots(figsize=(12, 7))
plt.title('Percntage of endangerment by category', fontsize=18, y=1.025);
plt.bar(category_status_count.index, ndbar, color= 'green', edgecolor= 'white', width=barWidth, label= 'No Danger');
plt.bar(category_status_count.index, irbar, bottom= ndbar, color= 'yellow', edgecolor='white', width=barWidth, label= 'In Recovery');
plt.bar(category_status_count.index, scbar, bottom= [i+j for i,j in zip(ndbar, irbar)], color= 'sandybrown', edgecolor= 'white', width=barWidth, label= 'Species of Concern');
plt.bar(category_status_count.index, tbar, bottom= [i+j+k for i,j,k in zip(ndbar, irbar, scbar)], color= 'darkorange', edgecolor= 'white', width= barWidth, label= 'Threatened');
plt.bar(category_status_count.index, ebar, bottom=[i+j+k+l for i,j,k,l in zip(ndbar, irbar, scbar, tbar)], color= 'crimson', edgecolor= 'white', width= barWidth, label= 'Endangered');
ax.set_xlabel('Species')
ax.set_ylabel('Percentages')
plt.legend(title='Status',bbox_to_anchor=(1,1),fontsize = 'x-small')
plt.show()

ax = category_status_count.plot(kind='bar', stacked=True,figsize = (12,7))
ax.set_xlabel('Species')
plt.legend(title='Status')
ax.set_ylabel('Total conservation statuses')
plt.xticks(rotation = 0)
plt.show()
#categorical distribution of observations by park
ax1 = sns.boxplot(x="park_name", y="observations", hue="category", data=merged, linewidth=2.5)
ax1.set_xlabel('Park name')
plt.legend(title='Category')
ax1.set_ylabel('Total observations')
plt.title('Categorical distribution of observations by park')
plt.show()
