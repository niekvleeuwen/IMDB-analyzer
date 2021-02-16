import pandas as pd
import matplotlib.pyplot as plt

 # set font and plot size to be larger by default
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})

titleBasics = pd.read_csv('title-basics.tsv', sep='\t', usecols= ['tconst', 'titleType', 'runtimeMinutes']) 
titleRatings = pd.read_csv('title-ratings.tsv', sep='\t', usecols= ['tconst', 'averageRating']) 

# merge the titles and ratings on the unique identifier of the title
df = pd.merge(titleBasics, titleRatings, on=['tconst'])

# sort out to data set to only include movies
df = df[df['titleType'] == 'movie']

# remove titles with no run time or rating available
df = df.replace(r'\\N',' ', regex=True) 
df = df[df['runtimeMinutes'] != ' ']

# convert to numeric
df[['runtimeMinutes', 'averageRating']] = df[['runtimeMinutes', 'averageRating']].apply(pd.to_numeric)

# limit run time between 40 minutes and 3 hours
df = df[df['runtimeMinutes'].between(40, 180)]

# group the data by runtime 
df = df.groupby(['runtimeMinutes'], as_index=False).mean()

# plot the data
df.plot(kind='scatter', x='runtimeMinutes', y='averageRating')
plt.ylim([5.5,7.5])
plt.xlabel('Movie duration in minutes', fontsize=18)
plt.ylabel('Average IMDb rating', fontsize=18)
plt.show()