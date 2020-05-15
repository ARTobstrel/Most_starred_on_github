import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=tetris&sort=stars'


def get_res(link):
    return requests.get(link)


r = get_res(url)
response_dict = r.json()
print("Total repositories: ", response_dict['total_count'])

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print('Number of items:', len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'xlink': repo_dict['html_url'],
        # 'label': repo_dict['description']
    }
    plot_dicts.append(plot_dict)

# Построение визуализации
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Tetris Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
