import requests
import os
from dotenv import load_dotenv

load_dotenv()

apiKey=os.getenv('SPOONACULAR_API_KEY')

url='https://api.spoonacular.com/recipes/findByIngredients'

#Colocar aqui minha função : input_ingredientes

parametros = {
    'apiKey':apiKey,
    'ingredients':'flour', #Chamar ela aqui ao invez de um ingrdiente especifico
    'number':2,
}

resposta = requests.get(url, params=parametros)

#seria minha  função buscar_receitas()?
if resposta.status_code == 200:
    dados_lista = resposta.json()
    for dicionario in dados_lista:
        print(f"ID = {dicionario['id']}")
        print(f"RECIPE = {dicionario['title']}")
        print(f"IMAGE = {dicionario['image']}")
else:
    print("Erro:", resposta.status_code)