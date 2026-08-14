import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey=os.getenv('SPOONACULAR_API_KEY')

url='https://api.spoonacular.com/recipes/findByIngredients'

parametros = {
    'apiKey':apiKey,
    'ingredients':'flour',
    'number':1,
}

resposta = requests.get(url, params=parametros)

if resposta.status_code == 200:
    dados_lista = resposta.json()
    for dicionario in dados_lista:
        for chave in dicionario.keys():
            print(f'{chave} = {dicionario[chave]}')
        #print(dicionario.items())
        #print(dicionario["title"])
        #print(dicionario["image"])
else:
    print("Erro:", resposta.status_code)

