# (1) Generate a program to make API Calls
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

## Define the API call url path
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

## Make the API call using the request get() method and print response
r = requests.get(url)
print('Status code: {}'.format(r.status_code))

## Store the API call response to variable
response_dict = r.json()
print('Total repositories: '.format(response_dict['total_count']))

## Display the results by converting the json to Python dictionary
# print(response_dict.keys())

## Explore the infro about the repositories
repo_dicts = response_dict['items']
# print('Repositories returned: ', len(repo_dicts))

## Examine the first repo
# repo_dict = repo_dicts[0]
# print('\nKeys: ', len(repo_dict))
# for key in repo_dict.keys():
# 	print(key)

## Print out values for single repo
# print('\nSelected information about first repository: ')
# print('Name: ', repo_dict['name'])
# print('Owner: ', repo_dict['owner']['login'])
# print('Stars: ', repo_dict['stargazers_count'])
# print('Repository: ', repo_dict['html_url'])
# print('Created: ', repo_dict['created_at'])
# print('Updated: ', repo_dict['updated_at'])
# print('Description: ', repo_dict['description'])

## Summarize the top information
# print('\nSelected information about each repository: ')
# for repo_dict in repo_dicts:
# 	print('\nName: ', repo_dict['name'])
# 	print('Owner: ', repo_dict['owner']['login'])
# 	print('Stars: ', repo_dict['stargazers_count'])
# 	print('Repository: ', repo_dict['html_url'])
# 	try:
# 		print('Description: ', repo_dict['description'].encode('ascii', 'ignore'))
# 	except AttributeError:
# 		continue

## Create lists to store date for visualization
names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

## Define the style to make the visualization
my_style = LS('#333366', base_style=LCS)

## Configure the chart for visualization
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.major_label_font_size = 18
my_config.trncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style = my_style)
chart.title ='Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_respos.svg')



