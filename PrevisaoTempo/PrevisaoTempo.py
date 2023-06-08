# Lembrete: Programa funcional,
#mais terminar de colocar as definições de funções para deixar o código limpo

## O programa vai mostrar a temperatura atual e outras infoemações legais
## (As informações não são exadas. Creditos para api do openweathermap.org)

import requests, pprint # A lib pprint serve para vizualizar melhor a API
from emoji import emojize
from datetime import datetime

api = "APIKey"

# Dicionários de emojis
emojis = {
    "sol": "\u2600",
    "lua": "\u263D",
    "nuvem": "\u2601",
    "parcial_nubla": "\u26C5",
    "sol_nuvens_trovao": "\u26C8",
    "chuva": "\u2614",
    "nuvem_chuva": emojize(":cloud_with_rain:"),
    "nuvens_trovao_chuva": "\u26C8",
    "guarda_chuva": "\u2602",
    "flocos_neve": "\u2744",
    "nevoa": emojize(":foggy:"),
    "calor_inteso": emojize(":fire:")} #OBS: Unicode do fogo não está funcionando

# link1 por localizasão: latitude e longitude = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
# link2 por localizasão: cidade = "https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}"

# Função com o input do usuário
def escolha_usuario(um_dois):
    while True:
        input_usuaio = input("Digite [1] para o nome da cidade, ou [2] para latitude e longitude: ").strip()

        if input_usuaio.isnumeric():
            input_usuaio = int(input_usuaio) # Convertendo para inteiro, para usar if
            # Como a está definição de função sempre vai retornara um valor 1 ou 2 (True), nunca retornará 0 (False),
            #fazendo a saida ficar True ou seja, sempre vai ficar retornando 1, e preciso de dois valores
            # Então coloquei mais uma condição para adicionar os dois valores
            if input_usuaio == 1 or input_usuaio == 2:
                um_dois = input_usuaio
                break
        else:
            print("Por favor digite o numeral 1 ou 2: ")
            continue
    return um_dois


# O None foi adicionado na função pq ela precisa de uma paremetro para ser chamada
#e o parametro já é adicionado no imput dentro dela
escolha = escolha_usuario(None)

if escolha == 1:
    cidade = str(input("Qual cidade gostaria de saber sobre o clima atual: "))
    link_cidade = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api}&lang=pt_br"
    global r # Colocando a variável global para usar fora da condição
    r = requests.get(link_cidade)

elif escolha == 2:
    lat = input("Digite a latitude: ").strip()
    lon = input("Digite a longitude: ").strip()
    link_LatLon = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&lang=pt_br"
    r = requests.get(link_LatLon)


json = r.json()
# pprint.pprint(json)

# Pegando dados da API:
sensacao = json["main"]["feels_like"]
# Kelvin para Celsius
sensacao_convertida = round(sensacao - 273.15, 2) # round(valor - 273.15, casas decimais depois da virgula)

umidade = json["main"]["humidity"]

temperatura = json["main"]["temp"]
temperatura_conver = round(temperatura - 273.15, 2)

temp_maxima = json["main"]["temp_max"]
temp_maxima_conv = round(temp_maxima - 273.15, 2)

temp_minima = json["main"]["temp_min"]
temp_minima_conv = round(temp_minima - 273.15, 2)

nome = json["name"]

pais = json["sys"]["country"]

nascer_sol = json["sys"]["sunrise"]
nascer_sol = datetime.fromtimestamp(nascer_sol) # formatando o valor com a lib datetime
nascer_sol = nascer_sol.strftime('%H:%M:%S') # pegado só as horas e formatando com .strftime

por_sol = json["sys"]["sunset"]
por_sol = datetime.fromtimestamp(por_sol) # formatando o valor com a lib datetime
por_sol = por_sol.strftime('%H:%M:%S') # pegado só as horas e formatando com .strftime

clima = json["weather"][0]["description"]


# Condições para usar os emojis:
# Noite (ex:01n)
icon = json["weather"][0]["icon"]
if icon == "01n":
    icon = emojis["lua"]
elif icon == "02n":
    icon = emojis["nuvem"] + emojis["lua"]
if icon == "03n":
    icon = emojis["nuvem"]
elif icon == "04n":
    icon = emojis["nuvem"] + emojis["nuvem"]
if icon == "09n":
    icon = emojis["nuvem_chuva"]
elif icon == "10n":
    icon = emojis["nuvem_chuva"] + emojis["lua"]
if icon == "11n":
    icon = emojis["nuvens_trovao_chuva"]
elif icon == "13n":
    icon = emojis["flocos_neve"]
if icon == "50n":
    icon = emojis["nevoa"]

# Dia (ex:01d)
elif icon == "01d":
    icon = emojis["sol"]
if icon == "02d":
    icon = emojis["parcial_nubla"]
elif icon == "03d":
    icon = emojis["nuvem"]
if icon == "04d":
    icon = emojis["nuvem"] + emojis["nuvem"]
elif icon == "09d":
    icon = emojis["nuvem_chuva"]
if icon == "10d":
    icon = emojis["nuvem_chuva"] + emojis["sol"]
elif icon == "11d":
    icon = emojis["nuvens_trovao_chuva"]
if icon == "13d":
    icon = emojis["flocos_neve"]
elif icon == "50d":
    icon = emojis["nevoa"]


print(f"\n{nome} - País {pais} - Nacer do sol: {nascer_sol} - Por do sol: {por_sol}")
print(f"Temperatura {temperatura_conver}")
print(f"Máxima de {temp_maxima_conv} e Minima de {temp_minima_conv} - Sensação terminca {sensacao_convertida}")
print(clima, icon)
print(f"Umidde atual: {umidade}")
