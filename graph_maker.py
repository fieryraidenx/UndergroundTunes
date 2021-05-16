from spotify_processing import *

def get_graph_url(genre_list):
    '''
    Genre List contains a list of genres in sorted descending order based on UT Rating

    Each genre has these attributes and methods:
    genre.get_final_rating() returns the UT rating of the genre
    genre.average_pos, genre.average_bpm, genre.average_nrgy gets average ratings for bpm, pos, and nrgy

    This function will save a graph in the images folder and return the filepath of which this url is stored
    '''
    filepath = "static/images/test.png" #CHANGE THIS TO "" WHEN STARTING TO CODE

    #write code here

    return filepath