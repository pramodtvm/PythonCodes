
import requests

"""
API for GITHUB
https://api.github.com/

Documentation about API
https://developer.github.com/v3/


"""

r = requests.get('https://api.github.com/user', auth=('pramodtvm', '******'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
#print(r.text)
print(r.json())
