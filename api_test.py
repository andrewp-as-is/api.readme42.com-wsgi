import requests

headers = {'Authorization': 'Token 12abf43bafa8fae7f0a28a82adb84dcf'}
data = dict(settings='GITHUB_OAUTH_CLIENT_ID=XXX',examples='examples ...')
url='https://api.readme42.com/requires'
url='http://127.0.0.1:8000/templates/andrewp-as-is/python-github-readme'
r = requests.post(url,headers=headers,data=data)
print(r)
print(r.text)
open('README.md','w').write(r.text)
