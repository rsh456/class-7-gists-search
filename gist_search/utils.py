import requests

BASE_URL = 'https://api.github.com/users/{username}/gists'


def get_gists(username):
    url = BASE_URL.format(username=username)
    resp = requests.get(url, params={'per_page': 100})
    if not resp.ok:
        return None
    return resp.json()

gists = get_gists("santiagobasulto")
first_gist = gists[0]
first_3 = gists[:3]
#print(first_gist)
for gist in first_3:
    print("{:<40} | {}".format(gist['id'],gist['description']))