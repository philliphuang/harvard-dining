def results(fields, original_query):
	
	import requests

	params = {
		'key': '06bc0ceef35adbd17e8955ad198209c5',
		'output': 'json',
		'sdt': '2011-03-21'
	}

	r = requests.get('http://api.cs50.net/food/3/menus', params=params)

	items = []

	for item in r.json():
		items.append(item['name'])

	return {
		"title": "HUDS Menu",
		"html": "<p style='font-family: sans-serif; padding: 2em'>{0}</p>".format(items)
	}

def run(message):
	import os
	os.system('open "http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp"')