from spotify_processing import *




def space_out(words):
    new_word = ""
    for word in words.split(" "):
        new_word += word + "\n"
    return new_word

def get_graph_url(genre_list):
    '''
    Genre List contains a list of genres in sorted descending order based on UT Rating

    Each genre has these attributes and methods:
    genre.get_final_rating() returns the UT rating of the genre
    genre.average_pos, genre.average_bpm, genre.average_nrgy gets average ratings for bpm, pos, and nrgy

    This function will save a graph in the images folder and return the filepath of which this url is stored
    '''
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from random import randint



    genres = [space_out(genre_list[i].genre_name) for i in range(5)]
    ratings = [genre_list[i].final_rating for i in range(5)]
    colors = ["red", "orange", "yellow", "green", "blue"]
    filepath = f"static/images/g{randint(100000,999999)}.png"


    plt.bar(genres, ratings, color=colors)
    axes = plt.gca()
    axes.set_ylim([7,9])

    plt.title('UT Ratings')
    plt.xlabel('Genres')
    plt.ylabel('UT Ratings')
    plt.savefig(filepath)

    return filepath