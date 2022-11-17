# Title : Gender representation in the film industry

## Abstract <a name="Abstract"></a>

(Draft)

mots clés: stereotype / 

Nowadays, gender representation is a topic that frequently comes up in public debate. One could recentre the question on the film industry. As movies reflect society, the different gender stereotypes are probably also depicted in them. Thus, it would be interesting to evaluate and quantify this difference. To do so, we will exploit a specific database, namely the CMU movies summary dataset, which gathers various information on the actors, characters, and the pre-processed movies summaries. We aim to compare the data for different geographical regions and time periods, to visualize the evolution if any. Then, we will try to identify if there exist some mechanisms that tend to reinforce, or on the contrary reduce, the presence or impact of these stereotypes. 



Our definition of women's role in movie industry include the following quantities :

- Importance of the role : Is the actor/actress playing a main character in the movie ? 
  This metric can be used to assess if men regularly get more important roles in movies.
- Age of the role : At what (actor/actress) age is played the role ? 
  This quantity is used to see if women and men age influence differently the roles they obtain.
- Qualitative aspect of women role 
  Assess how women characters are described differently than men characters.
- Importance of women in public opinion on movies
  Assess if public opinion is biased towards men opinions or women opinions. Who judges the quality of a movie?

We want to explore these characteristics accross time (from 1950 to 2010), in different movie industries (Europe, Bollywood, and Holywood, and also trhoughout the different movie genres.


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

We decide to use the IMDb datasets to enrich our data : https://www.imdb.com/interfaces/

- Can scrape the ratings per gender from imdb : https://help.imdb.com/article/imdb/track-movies-tv/how-can-i-view-the-breakdown-of-ratings/GZ9RAH4MHBYJWF42?ref_=helpart_nav_14#

- https://datasets.imdbws.com/ main actors also, review

Why do we use this dataset? 

First, it has much more movies than ours, so we can generalize findings more easily.

We are also able to match 62 000 out of 81 000 movies between the CMU database and the IMDb database. This can allow to fullfil missing data on these movies and give acces to much more information, such as writers and producers. Also, we are able to get their gender using a request on wikidata query service.

Using IMDb, we get access to the cast in credits order (https://help.imdb.com/article/contribution/filmography-credits/cast-acting-credits-guidelines/GH3JZC74FVYKKFMD?ref_=helpart_nav_5#) which can, for certain movies, give an idea of how important is the actor/actress role. However, if the director decides to put the cast in alphabetical order or in order of appearance, main actors may be buried in the credits. Credits may be listed in alphabetical order or according to appearance or popularity which makes it hard to track whichs actors are the most important.

One key aspect is that imdb gives access to demographics of data reviews, we get the number of voters and the grades attributed to movies by men and women of different ages. We can thus provide an analysis of the difference in the way men and women grade movies and if more men or women review movies on IMDb. A preliminary analysis have shown that when we focus on the 250 best graded movies of IMDb, only 17% of the grades are coming from women and no film among the 250 has recieved more positive grades from women than from men. So we can ask ourselves : do IMDb grades mostly showcase male opinion on movies ? 

We have also access to the writers and the directors, which can add a dimension to our analysis. 





ARGUMENT ON FEASIBILITY OR CHANGE THE QUESTIONS

1) Do women receive more important movie roles currently than in the past?

2) Are feminine characters described differently as the ones played by men ? (adjectives, action verbs, ...)

3) Is the gender gap (assuming there is one) bigger in some genres than in others?

4) Are there more disparities between women and men actors in different regions of the world (Hollywood, Bolywood, Europe) ?

5) Does the gender of the writer/producer have impact on how women are integrated to movies ?

5) Are imdb ratings biased towards male or female opinion ?





-







LIST USEFUL

Note: There are tools like "gender guesser" which give the gender based on a name. Seems reliable, maybe not for specific persons. 

Probably not use but maybe:

- https://www.kaggle.com/danielgrijalvas/movies Have main actor
- https://github.com/taubergm/HollywoodGenderData Have director gender

## Methods <a name="Methods"></a>

## Proposed timeline <a name="Proposed_timeline"></a>

## Organisation within the team <a name="Organisation"></a>

## Questions for TAs (optional) <a name="Questions"></a>

