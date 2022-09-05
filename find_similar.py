from collections import OrderedDict

from own_db_helpers import load_data


def find_my_movie(keyword, movies_data):
    for movie in movies_data:
        if keyword == movie['original_title']:
            return movie
    return None


def get_rating(my_movie, movies_data, num_to_recommend=8):
    params = {
        'belongs_to_collection': 1000,
        'original_language': 300,
        'budget': 100,
        'genres': 500
    }
    rating = {}
    for movie in movies_data:
        movie_rate = 0
        for parameter in params:
            if movie[parameter] == my_movie[parameter]:
                movie_rate += params[parameter]
        rating[movie['original_title']] = movie_rate
    del rating[my_movie['original_title']]
    rating = OrderedDict(
        sorted(
            rating.items(),
            key=lambda t: t[1],
            reverse=True
        )
    )
    final_recommendation = []
    for movie in rating:
        final_recommendation.append(movie)
        if len(final_recommendation) == num_to_recommend:
            break
    return final_recommendation


def main():
    path = input('Enter path to DataBase:')
    movies_data = load_data(path)
    if not movies_data:
        print('File not found, sorry...')
        raise SystemExit
    keyword = input('Enter movie title to search for:')
    my_movie = find_my_movie(keyword, movies_data)
    if not my_movie:
        print('No such movie in MoviesDB')
        raise SystemExit
    recommendation = get_rating(my_movie, movies_data)
    for movie in sorted(recommendation):
        print(movie)


if __name__ == '__main__':
    main()
