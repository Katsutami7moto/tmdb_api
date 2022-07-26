from own_db_helpers import load_data


def search_for_movie(keyword, movies_data):
    movies_found = set()
    for movie in movies_data:
        if keyword.lower() in movie['original_title'].lower():
            movies_found.add(movie['original_title'])
    return movies_found


def main():
    path = input('Enter path to DataBase:')
    movies_data = load_data(path)
    if not movies_data:
        print('File not found, sorry...')
        raise SystemExit
    keyword = input('Enter movie to search for:')
    result = search_for_movie(keyword, movies_data)
    for movie in sorted(result):
        print(movie)


if __name__ == '__main__':
    main()
