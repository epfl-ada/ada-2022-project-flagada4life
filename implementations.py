import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import pandas as pd
import numpy as np
import xml.etree
from xml.etree import cElementTree as ElementTree
from gzip import *
import gzip

def load_character_md():
    CHARACTER_MD = "MovieSummaries/character.metadata.tsv"
    character_md = pd.read_csv(CHARACTER_MD, sep="\t", header=None, names = ['Wikipedia movie ID', 'Freebase movie ID', 'Movie release date', 'Character name', 'Actor date of birth', 'Actor gender','Actor height (in meters)','Actor ethnicity (Freebase ID)','Actor name', 'Actor age at movie release', 'Freebase character/actor map ID','Freebase character ID','Freebase actor ID'])
    
    return character_md

def load_tvtropes_clusters():
    TVTROPES_CLUSTERS = "MovieSummaries/tvtropes.clusters.txt"
    tvtropes_clusters = pd.read_csv(TVTROPES_CLUSTERS, sep="\t", header=None, names = ['char types', 'char', 'movie', 'ID', 'actor'])
    dic = tvtropes_clusters.to_dict()
    for idx in range(tvtropes_clusters.shape[0]):
        serie = json.loads(dic['char'][idx])
        tvtropes_clusters.at[idx, 'char'] = serie['char']
        tvtropes_clusters.at[idx, 'movie'] = serie['movie']
        tvtropes_clusters.at[idx, 'ID'] = serie['id']
        tvtropes_clusters.at[idx, 'actor'] = serie['actor']
    return tvtropes_clusters
    
def load_movie_md():
    MOVIE_MD = "MovieSummaries/movie.metadata.tsv"
    movie_md = pd.read_csv(MOVIE_MD, sep="\t", header=None, names = ['Wikipedia movie ID','Freebase movie ID','Movie name','Movie release date','Movie box office revenue','Movie runtime','Movie languages','Movie countries','Movie genres'])
    movie_md['Movie countries'] = movie_md['Movie countries'].apply(lambda x: json.loads(x)) # Converts to dictionnary
    movie_md['Movie countries'] = movie_md['Movie countries'].apply(lambda x: list(x.values()))
    movie_md['Movie genres'] = movie_md['Movie genres'].apply(lambda x: json.loads(x)) # Converts to dictionnary
    movie_md['Movie genres'] = movie_md['Movie genres'].apply(lambda x: list(x.values()))
    movie_md['Movie languages'] = movie_md['Movie languages'].apply(lambda x: json.loads(x)) # Converts to dictionnary
    movie_md['Movie languages'] = movie_md['Movie languages'].apply(lambda x: list(x.values()))
    
    movie_md.query("`Movie release date` > '1915'", inplace = True)
    movie_md["Movie release date"] = pd.to_datetime(movie_md["Movie release date"])
    movie_md["Movie release date"] = movie_md["Movie release date"].dt.year
    
    return movie_md


def load_name_clusters():
    NAME_CLUSTERS = 'MovieSummaries/name.clusters.txt'
    name_clusters = pd.read_csv(NAME_CLUSTERS, sep="\t", header=None, names = ['character name','ID in character_metadata'])
    
    return name_clusters

def load_plot_summaries():
    PLOT_SUMMARIES = 'MovieSummaries/plot_summaries.txt'
    plot_summaries = pd.read_csv(PLOT_SUMMARIES, sep="\t", header=None, names = ['Wikipedia movie ID','summary'])
    
    return plot_summaries
