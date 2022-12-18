# Gender representation in the film industry

Hey, you can check our website by using this [link](https://luluehret.github.io/) ! :smirk: We hope you'll enjoy it!
The code is in Milestone3.ipynb.

## Abstract <a name="Abstract"></a>

Nowadays, gender representation and stereotypes are topics that frequently come up in public debate. As movies reflect society, the different gender stereotypes are probably also depicted in them. For example, among those stereotypes are the fact that male characters are more violent than women, that female characters are in general younger, or that female characters are more loving. It would be interesting to try to evaluate the difference in gender representation in cinema and see if stereotypes propagate in the movie industry. To do so, we will exploit a specific database, namely the CMU movies summary dataset, which gathers various information on the actors, characters, and the pre-processed movies summaries. For example, from these pre-processed summaries, we can gather valuable data on the actions done by characters, and associate these action to male and female characters. More generally, we aim to use the data to study how actors' gender impact their representation in movies. We will see how this representation vary across regions of the world (USA, India, West Europe) and with time (from 1950 to 2010). Finally, we will try to identify if there exist factors that tend to reinforce, or on the contrary reduce, the presence of these stereotypes.



## Research Questions <a name="Research_questions"></a>

1. How does actor's gender impact their representation in the film industry*?
a. Is there a difference in the typical actions male and female actors perform in movie summaries ?
b. Is there a difference in the age at which male and female actors play in movies ?
c. Are males and females equally represented in main roles ? 
d. Does this representation impact the way males and females rate the movie ?

2. How do the above analysis vary with epochs, regions, and movie genres ?

3. Does the gender of directors/writers influence gender representation in their movies ? 

*all analysis are made for movies from 1950 to 2010 in West Europe, India and USA.

## Proposed additional datasets <a name="Proposed_additional_datasets_and_files"></a>

We decided to extend our dataset with the following datasets:
- the IMDb datasets (https://www.imdb.com/interfaces/), as well as 
- Queries from wikidata to retrieve the gender of actors, writers, and producers. 
A complete description of the datasets if provided in the webpage of the datasets.

Why do we use these datasets? 
The IMDb dataset allows us to enrich the information on the movies, giving access to directors and writers, which adds another dimension to the analysis. We use queries to get the gender of people in the IMDb dataset, and also to match IMDb movie IDs to Freebase Movie IDs. We also have access to the ratings divided by gender on IMDb.


## Methods <a name="Methods"></a>

1. Data scraping, pre-processing and dataset construction.

 - CMU Movie Summary Corpus: merge the provided datasets to aggregate desired data, remove the lines that are useless because of missing information
 - IMDB dataset: merge the provided datasets on the movie IDs, to have in a single table the movie identifier, the actors / directors, and movie informations. 
 - Wikidata query: merge with the IMDB dataset with a query to add the gender of each person in the previous dataset. 

2. Preliminary analysis

- Divide the dataset in subsets for each region: US, Europe, India
- Divide the dataset in subsets for some genre such as romance movies, action, thriller, drama...
- Extract and plot data on the age of each actor

3. Analysis of all the character's actions in movie summaries using Stanford CoreNLP 

- From the file corenlp_plot_summaries, we get all the actions of every characters from summaries of every movies, and store them into a dataframe with all  relevant informations to potentialy merge/make links with other dataframes (character_md, movie_md, etc.) later in the analysis. 
- Sorting values of this dataframe by number of occurence of the action, we get the 100 most occurent actions made by actors according to their gender. Then we seen which of these actions are common for both genders (87/100), and which are not. The figures below show the most occurent actions for males that are not in the top 100 female actions and vice-versa.  

<img src="https://github.com/epfl-ada/ada-2022-project-flagada4life/blob/main/data/MovieSummaries/ADA%20P2.png" width="800" />

4. Try to estimate characters importance in movies

- For each movie, we try to sort characters by importance. Because we couldn't find this data on an external dataset*, we decided to determine importance of a character by the number of occurences of its name in the movie summary. 
- To do so, we merge metadata about characters with the movie summaries dataframe, and then perform an apply function on each row to count the number of occurence of the character name on the summary. 

*In the IMDB database, the ordering of the principal cast correspond to the order in which actors appear in the credits. However, depending on the movie, the ordering of credits can be made either by the order of appearance of the actors, or by their popularity, or by alphabteical order, etc. There was a dataset on Kaggle with a ranking of principals actors but it was too small (1000 rows).

5. Investigation on the impact of the producer and writer gender on the stereotypes and the description of the roles
- Separate analysis of movies produced/written by male and females.


6. Investigation on the impact of the movie genre on the stereotypes of the roles


7. Investigation on the impact of the geographical region on gender representation


8. Sentiment analysis to see if the roles are depicted differently depending on the gender of the character


9. Variety of the vocabulary used to describe a character depending on its gender


## Proposed timeline <a name="Proposed_timeline"></a>

21.11.22: steps 4 and 5

28.11.22: steps: 5 and 6

5.12.22: steps 7, 8 and 9

12.12.22: Coding of the website to present the results, starting the storytelling

19.12.22: Finishing the website, adding interactive plots using the plotly library


## Organisation within the team <a name="Organisation"></a>

- Jehan : Task 4, interactive plots
- Théo : Task 5, website coding
- Tanguy : Task 6, story telling
- Lucas : Task 7, 8 website coding
