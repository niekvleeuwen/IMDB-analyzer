import pandas as pd
import matplotlib.pyplot as plt

# set font and plot size to be larger by default
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})

titleBasics = pd.read_csv('title-basics.tsv', sep='\t', usecols= ['tconst', 'titleType']) 
titleRatings = pd.read_csv('title-ratings.tsv', sep='\t', usecols= ['tconst', 'averageRating', 'numVotes']) 

# merge the titles and ratings on the unique identifier of the title
df = pd.merge(titleBasics, titleRatings, on=['tconst'])

# sort out to data set to only include movies
df = df[df['titleType'] == 'movie']

# convert to numeric
df[['numVotes', 'averageRating']] = df[['numVotes', 'averageRating']].apply(pd.to_numeric)

# only use movies with more than 50 votes
df = df[df['numVotes'] > 50]

# group the data by runtime 
df = df.groupby(['averageRating'], as_index=False).mean()

# plot the data
df.plot(kind='scatter', x='numVotes', y='averageRating')
plt.ylim([0,10])
plt.xscale('log')
plt.xlabel('Number of votes', fontsize=18)
plt.ylabel('Average IMDb rating', fontsize=18)
plt.show()