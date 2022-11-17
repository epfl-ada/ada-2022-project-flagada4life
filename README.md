# Gender representation in the film industry

## Abstract <a name="Abstract"></a>
Nowadays, gender representation is a topic that frequently comes up in public debate. One could recentre the question on the film industry. As movies reflect society, the different gender stereotypes are probably also depicted in them. Thus, it would be interesting to evaluate and quantify this difference. To do so, we will exploit a specific database, namely the CMU movies summary dataset, which gathers various information on the actors, characters, and the pre-processed movies summaries. We aim to compare the data for different geographical regions and time periods, to visualize the evolution if any. Then, we will try to identify if there exist some mechanisms that tend to reinforce, or on the contrary reduce, the presence or impact of these stereotypes. 


## Research Questions <a name="Research_questions"></a>
The analysis will be performed to answer the following questions:
1.	What is the difference between women and men actors in different regions of the world (Hollywood, Bollywood, Europe)?
2.	Are feminine characters described differently as the ones played by men? (Adjectives, action verbs, ...)
3.	Is the gender gap (assuming there is one) bigger in some movie genres than in others?
4.	Does the gender of the writer/producer have impact on how women are integrated to movies ?

These questions imply that we need to define :
- comparison criteria in terms of how women and men are described
- all metrics for defining the size of the gender gap


## Proposed additional datasets <a name="Proposed_additional_datasets_and_files"></a>

We decided to use the IMDb datasets to enrich our data : https://www.imdb.com/interfaces/, as well as data from wikidata, to retrieve the genre of the desired people. 

Why do we use this dataset? 
This dataset allows us to get data for the movies directors and movie crews, which adds another dimension to the analysis. We were able to match the two datasets by knowing the name of the movies. 


!!!!!!!!!!!!!!!!!!!!!!!We are also able to match 62 000 out of 81 000 movies between the CMU database and the IMDb database.

One key aspect is that imdb gives access to demographics of data reviews, we get the number of voters and the grades attributed to movies by men and women of different ages. We can thus provide an analysis of the difference in the way men and women grade movies and if more men or women review movies on IMDb. A preliminary analysis have shown that when we focus on the 250 best graded movies of IMDb, only 17% of the grades are coming from women and no film among the 250 has recieved more positive grades from women than from men. So we can ask ourselves : do IMDb grades mostly showcase male opinion on movies ? 

We have also access to the writers and the directors, which can add a dimension to our analysis. 



Probably not use but maybe:

- https://www.kaggle.com/danielgrijalvas/movies Have main actor
- https://github.com/taubergm/HollywoodGenderData Have director gender

## Methods <a name="Methods"></a>

1. Data scraping, pre-processing and dataset construction.

 - CMU Movie Summary Corpus: merge the provided datasets to aggregate desired data, remove the lines that are useless because of missing information
 - IMDB dataset: merge the provided datasets on the movie names, to have in a single table the movie identifier, the actors / directors, and movie informations. 
 - Wikidata query: merge with the IMDB dataset to add the genre of each person in the previous dataset. 

2. Preliminary analysis

- Divide the dataset in subsets for each region: US, Europe, India
- Divide the dataset in subsets for some genre such as romance movies, action, thriller, drama...
- Extract and plot data on the age of each actor

3. NLP analysis

- !!!!!!!!!!!!!! A REMPLIR PAR JEHAN !!!!!!!!!!!!!

4. Investigation on the impact of the producer gender on the stereotypes and the description of the roles


5. Investigation on the impact of the movie genre on the stereotypes and the description of the roles


6. Investigation on the impact of the geographical region on the stereotypes and the description of the roles


7. Sentiment analysis to see if the roles are depicted differently depending on the genre of the character


8. Variety of the vocabulary used to describe a character depending on its genre


## Proposed timeline <a name="Proposed_timeline"></a>

Step 4: 21.11.22

Step 5: 28.11.22

Step 6: 5.12.22

Step 7: 12.12.22

Step 8: 19.12.22


## Organisation within the team <a name="Organisation"></a>

![Capture d’écran (11)](https://user-images.githubusercontent.com/114073595/202502824-14ff22ea-4fa7-419b-a066-b2ed7c8b0d50.png)


## Questions for TAs (optional) <a name="Questions"></a>

