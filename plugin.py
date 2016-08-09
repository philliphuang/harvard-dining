def results(fields, original_query):
	
	# request data from API
	import requests
	params = {
		'key': '06bc0ceef35adbd17e8955ad198209c5',
		'output': 'json',
		'sdt': '2011-03-21'
	}
	r = requests.get('http://api.cs50.net/food/3/menus', params=params)

	# format for only names
	items = []
	for item in r.json():
		items.append(item['name'])
		
	html = "<ul>"
	for item in items:
		html = html + "<li>" + item + "</li>"
	html = html + "</ul>"

	return {
		"title": "HUDS Menu",
		"html": html
	}

def run(message):
	import os
	os.system("open http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp")