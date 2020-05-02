import requests

# url = 'http://data.fixer.io/api/latest'
url = 'https://api.exchangeratesapi.io/latest?base=USD'
# access_key = '641023efced8da60d927ce4476b80783'

# payload = {
#     'access_key': access_key,
#     'base': 'USD',
#     'symbols': ['GBP','JPY','EUR']
# }
res = requests.get(url)

json = res.json()

print(json['rates']['TRY'])