import csv

class Genre:
    '''
    Use get_final_rating() to get custom rating for songs depending on user input
    Use instance variable songlist to get all songs associated with that genre

    Use instance variable avg_bpm, avg_pos, avg_nrgy to get average ratings for these vars
    '''
    bpmBool = None
    posBool = None
    nrgyBool = None

    def __init__(self, genre, song, rating, bpm, pos, nrgy):
        self.genre_name = genre
        self.songlist = [song]

        self.total_rating = rating
        self.total_bpm = bpm
        self.total_pos = pos
        self.total_nrgy = nrgy
    
    def process_final_rating(self):
        l = len(self.songlist)
        average_rating = (self.total_rating * .1) / l
        self.avg_bpm = self.total_bpm / l
        self.avg_pos= self.total_pos / l
        self.avg_nrgy = self.total_nrgy / l

        final_rating = (average_rating ** 2) / (average_rating * 1.1 - 1)
        final_rating += (1 if Genre.bpmBool else -1) * (self.avg_bpm-115) / 50
        final_rating += (1 if Genre.posBool else -1) * (self.avg_pos-70) / 50
        final_rating += (1 if Genre.nrgyBool else -1) * (self.avg_nrgy-77) / 50
        self.final_rating = final_rating

    
    def update(self, song, rating, bpm, pos, nrgy):
        self.songlist.append(song)
        self.total_rating += rating
        self.total_bpm += bpm
        self.total_pos += pos
        self.total_nrgy += nrgy

    @staticmethod
    def update_params(bBool, pBool, nBool):
        Genre.bpmBool = bBool
        Genre.posBool = pBool
        Genre.nrgyBool = nBool

    @staticmethod
    def sort_by_rating(g):
        g.process_final_rating()
        return g.final_rating

    def __repr__(self):
        return f"\n{self.genre_name}-{self.get_final_rating()}"

def process_data(bpmBool, posBool, nrgyBool):
    '''
        Returns a sorted Genre list of the top three best genres
        based on three boolean values

        bpm - T is Fast, F is Slow
        pos - T is Happy, F is Sad
        nrgy - T is Upbeat, F is Chill
    '''

    Genre.update_params(bpmBool, posBool, nrgyBool)

    #Read rating data
    genre_dict = {} # GenreName : GenreClass
    f = open('data/spotify_ratings.csv', 'r')
    spotify_ratings = csv.reader(f, delimiter=',')
    line = 0
    for row in spotify_ratings:
        line += 1
        if(line == 1): continue
        song, genre, rating =f"{row[1]} - {row[2]}", row[3], int(row[14])
        bpm, positivity, energy = int(row[5]), int(row[10]), int(row[6])
        if genre not in genre_dict: 
            genre_dict[genre] = Genre(genre, song, rating, bpm, positivity, energy)
        else: 
            genre_dict[genre].update(song, rating, bpm, positivity, energy)
        
    
    #Convert dict into list of Genre classes
    top_genres = list(genre_dict.values())

    #Sorts genre based on user-defined parameters and total rating
    top_genres.sort(key=Genre.sort_by_rating, reverse=True)
    top_genres = top_genres[:min(len(top_genres), 10)]

    return top_genres





