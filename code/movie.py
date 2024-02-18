movie_database = {
   'movie1': {'title': 'Movie 1', 'genre': 'Action', 'showtimes': ['3:00 PM', '5:00 PM', '7:00 PM']},
  'movie2': {'title': 'Movie 2', 'genre': 'Comedy', 'showtimes': ['2:00 PM', '4:00 PM', '6:00 PM']},
   ...
}

def add_movie(title, genre, showtimes):
    title = input("State the title of the movie")
    genre = input("State the genre of the movie")
    showtimes = input("Enter the showtimes for the movie (hyphen-seperated): ").split('-')
    movie_database['movie' + str(len(movie_database) + 1)] = {'title': title, 'genre': genre, 'showtimes': [time.strip() for time in showtimes]}

def find_movies_by_genre(genre):
    genre = input("Enter the genre to find movies: ")
    movies_of_genre = [movie_info['title'] for movie_info in movie_database.values() if movie_info['genre'] == genre]
    return movies_of_genre
    
def find_earliest_and_latest_showtime(title):





options = input("What type of genre do you choose: " movie_database.get{genre})