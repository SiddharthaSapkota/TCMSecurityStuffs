movies = ["Harry Met Sally", "Hangover", "How To Train Your Dragon", "The Alchemist"]
print(movies[0])
print(movies[0:3])
print(movies[1:])
print(movies[-1:])
movies.append("Humour")   # adds items at the end of the list
print(movies)
movies.insert(3, "Life of pi") # inserts items at the given     
print(movies)
movies.pop()   #removes the last item
print(movies)
movies.pop(0)
print(movies)

her_movies = ["TMKOC", "Girlfriend"]
our_movies = movies + her_movies
print(our_movies)

nested_list = [[1,2,3], [4,5,6],[7,8,9]]
print(nested_list[2][2])