import requests
url = 'http://quotes.toscrape.com'
response = requests.get(url)
if response.ok:
    print(response.text[:500])
