import requests
import json

# Lista de entradas (30 documentos)
entradas = [
    "mazda", "nissan", "toyota", "warcraft", "suzuki",
    "bentley", "monster", "starcraft", "lotus", "bugatti",
    "audi", "mercedes-benz", "volkswagen", "ford", "chevrolet",
    "honda", "hyundai", "subaru", "volvo", "lamborghini",
    "kia", "jaguar", "bmw", "vikings", "fiat",
    "jeep", "cadillac", "chevy", "ram", "subaru"
]
url = "https://en.wikipedia.org/w/api.php"
i = 1
for entrada in entradas:
    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'explaintext': '',
        'redirects': 1,
        'titles': entrada
    }

    req = requests.get(
        url,
        params=params
    ).json()

    n_page = list(req['query']['pages'].keys())[0]
    texto = req['query']['pages'][n_page]['extract']
    texto = '{}<splittername>{}'.format(i, json.dumps(texto))

    if i <= 15:
        with open(f'../carpeta1/{entrada}.txt', 'w') as f:
            f.write(texto)
    else:
        with open(f'../carpeta2/{entrada}.txt', 'w') as f:
            f.write(texto)
    i = i + 1