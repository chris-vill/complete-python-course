PROMPT_MENU = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: \n"
PROMPT_TITLE = "\nEnter the movie title: \n"
PROMPT_DIRECTOR = "\nEnter the movie director: \n"
PROMPT_YEAR = "\nEnter the movie release year: \n"
PROMPT_FIND_MOVIE = "\nFind movies (use title, director or year): \n"
movies = []

def main():
  is_continue = True

  while is_continue:
    selection = input(PROMPT_MENU)

    if selection == "a":
      movie_details = get_movie_inputs()
      add_movie(movie_details)

    elif selection == "l":
      print_movies(movies)

    elif selection == "f":
      query = get_movie_query()
      results = find_movies(query)
      print_movies(results)
      
    elif selection == "q":
      is_continue = False

    else:
      print('\nUnknown command. Please try again.\n')

def get_movie_inputs():
  title = input(PROMPT_TITLE)
  director = input(PROMPT_DIRECTOR)
  year = input(PROMPT_YEAR)

  return (title, director, year)


def add_movie(movie_details):
  title, director, year = movie_details

  movies.append({
    'title': title,
    'director': director,
    'year': year,
  })


def get_movie_query():
  query = input(PROMPT_FIND_MOVIE)

  return query


def find_movies(query):
  return [
    movie
    for movie in movies
    if find_movie(movie, query.lower())
  ]

def find_movie(movie, query):
  director = movie["director"].lower()
  title = movie["title"].lower()
  year = movie["year"].lower()

  return (
    title.find(query) > -1
    or director.find(query) > -1
    or year.find(query) > -1
  )


def print_movies(movies):
  if len(movies) == 0:
    print("No movies")
    return
  
  for movie in movies:
    print(movie)

main()