import json

def results(fields, original_query):
	'''
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
	'''
	url = 'http://www.foodpro.huds.harvard.edu/foodpro/menu_items.asp?type=05&meal=1'
	return {
		"title": "HUDS Menu",
        "html": "<script>window.location=%s</script>" % json.dumps(url),
        "webview_user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53",
        "webview_links_open_in_browser": True,
        "run_args": [url]
	}

def run(url):
    import os
    os.system('open "{0}"'.format(url))