# Main file
import requests

params = {
    'access_key': '8ec20aa6048dcdc117c84dcfd9cf1ef2',
    'query': 'Warsaw'
}


params['query'] = 'Paris'

respose = requests.get('http://api.weatherstack.com/current', params)
j = respose.json()
print(j['current']['weather_descriptions'])