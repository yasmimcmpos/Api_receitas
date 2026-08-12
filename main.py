import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey=os.getenv('SPOONACULAR_API_KEY')

url='https://api.spoonacular.com/recipes/findByIngredients'

parametros = {
    'apiKey':apiKey,
    'ingredients':'apples',
    'number':2,
}

resposta = requests.get(url, params=parametros)
if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)
else:
    print("Erro:", resposta.status_code)