import pickle
with open('movie_titles_metadata.txt', 'r', encoding = "ISO-8859-1") as movies:
	rom_movies = []
	for movie in movies:
		parsed_movie = movie.split('+++$+++')
		if 'romance' in parsed_movie[-1]:
			rom_movies.append(parsed_movie[0].strip())
print(rom_movies)
with open('movie_lines.txt', 'r', encoding = "ISO-8859-1") as lines:
	rom_parsed_lines = []
	other_parsed_lines = []
	for line in lines:
		parsed_line = line.split('+++$+++')
		if parsed_line[2].strip() in rom_movies:
			rom_parsed_lines.append(parsed_line[-1].strip())
		else:
			other_parsed_lines.append(parsed_line[-1].strip())
print(other_parsed_lines)
with open('rom.pickle', 'wb') as rom:
	pickle.dump(rom_parsed_lines, rom)
with open('other.pickle', 'wb') as other:
	pickle.dump(other_parsed_lines, other)