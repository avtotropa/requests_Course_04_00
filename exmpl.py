import requests

response = requests.get('https://api.github.com')
print(response)
print(dir(response))
print(response.status_code)
print(response.content)
print(response.text)
print(response.json())

print(response.json()['current_user_url'], response.json()['user_search_url'])


url = 'https://api.github.com/search/repositories'
params = {'q': 'python', 'sort': 'stars'}
response2 = requests.get(url, params=params)