import json
import urllib.error
import urllib.parse
import urllib.request

from tmdb_helpers import get_user_api_key, make_tmdb_api_request


def load_movies(user_api_key, movies_amount=1000):
    all_movies = []
    for movie_id in range(movies_amount):
        try:
            all_movies.append(
                make_tmdb_api_request(
                    method=f'/movie/{movie_id:d}',
                    api_key=user_api_key
                )
            )
        except urllib.error.HTTPError as err:
            if err.code == 404:  # if no movie on this id
                continue
            else:
                raise
        finally:
            print(f'{movie_id * 100 / movies_amount} percent complete')
    return all_movies


def main():
    user_api_key = get_user_api_key()
    if not user_api_key:
        print('Invalid api key')
        raise SystemExit
    movies_amount = 1000
    print('Please, wait, this operation may take smth like 15-20 minutes')
    all_movies = load_movies(user_api_key, movies_amount)
    with open(file='MyMoviesDB.json', mode='w', encoding='utf-8') as my_file:
        json.dump(all_movies, my_file)


if __name__ == '__main__':
    main()
