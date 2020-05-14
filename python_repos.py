import requests
import pygal


url = 'https://api.github.com/search/repositories?q=tetris&sort=stars'

r = requests.get(url)
print("Status code: ", r.status_code)

response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName: ', repo_dict['name'])
    print('Owner: ', repo_dict['owner']['login'])
    print('Stars: ', repo_dict['stargazers_count'])
    print('Repository: ', repo_dict['html_url'])
    print('Created: ', repo_dict['created_at'])
    print('Updated: ', repo_dict['updated_at'])
    print('Description: ', repo_dict['description'])
