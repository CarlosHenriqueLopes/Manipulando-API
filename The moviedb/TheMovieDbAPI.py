
## Exemplo simples de como manipular uma API

import requests
import pprint # Lib para vizualizar melhor a API

cliente = str(input("Digite o nome do filme:  "))
url = f"https://api.themoviedb.org/3/search/movie?query={cliente}&include_adult=true&language=pr-bt&page=1"

# headers necessário para acessar a AIP do movie db
headers = {
  "accept":
  "application/json",
  "Authorization":
  "Bearer xxxx"
}

response = requests.get(url, headers=headers)

# print(response.json())
# print()
# print(response.text)

json = response.json()

# pprint.pprint(json) # Para ver o json de forma organizada

Film_adulto = json["results"][0]["adult"]
if Film_adulto == False:
  print("\nFilme para todas as idades")
else:
  print("Para maiores")
print("-----------------------\n")

linguagem = json["results"][0]["original_language"]
if linguagem == "en":
  print("Linguagem: Inglês")
  print("-----------------------\n")
elif linguagem == "br":
  print("Linguagem: Português")
  print("-----------------------\n")

titulo = json["results"][0]["original_title"]
sinopse = json["results"][0]["overview"]
populariodade = json["results"][0]["popularity"]

print(f"Titulo: {titulo}")
print("-----------------------\n")

print(f"Sinopse: {sinopse}")
print("-----------------------\n")

print(f"Populariodade: {populariodade}")
