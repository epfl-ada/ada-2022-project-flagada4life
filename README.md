# Gender representation in the film industry

## Abstract <a name="Abstract"></a>
Nowadays, gender representation is a topic that frequently comes up in public debate. One could recentre the question on the film industry. As movies reflect society, the different gender stereotypes are probably also depicted in them. Thus, it would be interesting to evaluate and quantify this difference. To do so, we will exploit a specific database, namely the CMU movies summary dataset, which gathers various information on the actors, characters, and the pre-processed movies summaries. We aim to compare the data for different geographical regions and time periods, to visualize the evolution if any. Then, we will try to identify if there exist some mechanisms that tend to reinforce, or on the contrary reduce, the presence or impact of these stereotypes. 


## Research Questions <a name="Research_questions"></a>

1. How does actors' gender impact their representation in the film industry*?
a. Is there a difference in the typical actions male and female actors do in movie summaries ?
b. Is there a difference in the age at which male and female actors play in movies ?
c. Are males and females equally represented in main roles ? 
d. Does this representation impact the way males and females rate the movie ?

2. How do the above analysis vary with epochs*, regions**, and movie genres ? 

3. Does the gender of directors/writers influence gender representation in their movies ? 

*all analysis are made for movies from 1950 to 2010 in West Europe, India and USA.

## Proposed additional datasets <a name="Proposed_additional_datasets_and_files"></a>

We decided to extend our dataset with the following datasets:
- the IMDb datasets (https://www.imdb.com/interfaces/), as well as 
- A query from wikidata to retrieve the gender of actors, writers, and producers. 
A complete description of the datasets if provided in the webpage of the datasets.

Why do we use these datasets? 
The IMDb dataset allows us to enrich the information on the movies, giving access to directors and writers, which adds another dimension to the analysis. The wikidata query was merged to the IMDb dataset on the name of the people. Then, we merged the two datasets on the name of the movies. Using these additionnal data, we were able to match 62 000 out of 81 000 movies between the CMU database and the IMDb database.



## Methods <a name="Methods"></a>

1. Data scraping, pre-processing and dataset construction.

 - CMU Movie Summary Corpus: merge the provided datasets to aggregate desired data, remove the lines that are useless because of missing information
 - IMDB dataset: merge the provided datasets on the movie names, to have in a single table the movie identifier, the actors / directors, and movie informations. 
 - Wikidata query: merge with the IMDB dataset to add the gender of each person in the previous dataset. 

2. Preliminary analysis

- Divide the dataset in subsets for each region: US, Europe, India
- Divide the dataset in subsets for some genre such as romance movies, action, thriller, drama...
- Extract and plot data on the age of each actor

3. NLP analysis of all the character's actions in movie summaries

- From the file corenlp_plot_summaries, we get all the actions of every characters from summaries of every movies, and store them into a dataframe with all  relevant informations to potentialy merge/make links with other dataframes (character_md, movie_md, etc.) later in the analysis. 
- Sorting values this dataframe, we get the 100 most occurent actions made by actors according to their gender. Then we seen which of these actions are common for both genders (87/100), and which are not.

![plot](./directory_1/directory_2/.../directory_n/plot.png)

4. Investigation on the impact of the producer gender on the stereotypes and the description of the roles


5. Investigation on the impact of the movie genre on the stereotypes and the description of the roles


6. Investigation on the impact of the geographical region on the stereotypes and the description of the roles


7. Sentiment analysis to see if the roles are depicted differently depending on the genre of the character


8. Variety of the vocabulary used to describe a character depending on its genre


## Proposed timeline <a name="Proposed_timeline"></a>

21.11.22: steps 4 and 5

28.11.22: steps: 5 and 6

5.12.22: steps 7 and 8

12.12.22: Coding of the website to present the results, starting the storytelling

19.12.22: Finishing the website, adding interactive plots using the plotly library


## Organisation within the team <a name="Organisation"></a>

![Capture d’écran (11)](https://user-images.githubusercontent.com/114073595/202502824-14ff22ea-4fa7-419b-a066-b2ed7c8b0d50.png)
