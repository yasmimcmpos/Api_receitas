dados_lista = [
        {"id": 673463, "title": "Slow Cooker Apple Pork Tenderloin"},
        {"id":660261,"title":"Slow Cooked Applesauce"}
]

parametros_pesq = input("Digite seus ingredientes:")
x = parametros_pesq.split(",")
print(x)

#Função buscar_receitas()
for dicionario in dados_lista:
        print(f"ID = {dicionario['id']}")
        print(f"RECIPE = {dicionario['title']}")


