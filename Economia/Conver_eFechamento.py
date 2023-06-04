
# O usuário poderá fazer a conversão de algumas moedas,
#e fazer pesquisa sobre o fechamento dos ultimos X dias, se solicitado

## Retorna o fechamento dos ultimos dias
## https://economia.awesomeapi.com.br/json/daily/BRL-USD/5

#Lembrete: As vezes o código buga ao pular linha e no tempo (conferir)

import requests
import locale
from datetime import datetime, timedelta

# Configurar o local para o Brasil (pt_BR)
# Usado para converter
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


input_usuario = str(input("Escolha entre Real, Dólar, Euro e BitCoin para a conversão: ")).strip().upper()[0]
input2_usuario = str(input("Escolha entre Real, Dólar, Euro e BitCoin para o valor da conversão: \n")).strip().upper()[0]

# Condição para o caso do segundo input ser BTC
# Porque só possivél fazer conversão de BitCoin para Real, Dólar e Euro
while True:
    if input2_usuario == "B":
        print("Só conversão de BitCoin para Real, Dólar e Euro")
        input2_usuario = \
        str(input("Novamente escolha entre Real, Dólar, Euro e BitCoin para o valor da conversão: \n")).strip().upper()[0]
    else:
        break

print("Digite o dia para ver o fechamento dos ultimos dias")

dia = int(input("Dia: \n"))

if input_usuario in "D":
    moeda = "USD"
elif input_usuario in "R":
    moeda = "BRL"
elif input_usuario in "E":
    moeda = "EUR"
elif input_usuario in "B":
    moeda = "BTC"

if input2_usuario in "D":
    moeda2 = "USD"
elif input2_usuario in "R":
    moeda2 = "BRL"
elif input2_usuario in "E":
    moeda2 = "EUR"
elif input2_usuario in "B":
    moeda2 = "BTC"


site = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-{moeda2}/{dia}"
r = requests.get(site)
json = r.json()

# Manipulando dados da API:
nome = json[0]["name"]

alta = float(json[0]["high"])
convertido = locale.currency(alta, grouping=True) # Para converter a moeda para pt-Br
conversao_cm_format = f"R$ {alta:.4f}".replace(".", ",") # Convertendo com formatação

baixa = float(json[0]["low"])
convertido2 = locale.currency(baixa, grouping=True)
conversao_cm_format2 = f"R$ {baixa:.4f}".replace(".", ",")

taxa_de_cambio = float(json[0]["bid"])
TaxaConv = locale.currency(taxa_de_cambio, grouping=True)
TaxaConvFormat = f"R$ {taxa_de_cambio:.4f}".replace(".", ",")

para_venda = float(json[0]["ask"])
VendaConver = locale.currency(para_venda, grouping=True)
VendaConverFormat = f"R$ {para_venda:.4f}".replace(".", ",")

data_hora = int(json[0]["timestamp"])
data_hora = datetime.fromtimestamp(data_hora)
# Formatação de data e hora, para formatar o dados vindos do .fromtimestamp da lib datetime
formatado = "%d-%m-%Y %H:%M:%S"
data_hora = data_hora.strftime(formatado)

requisicao = json[0]["create_date"]
# converter a string requisicao em um objeto datetime
# OBS: colocar o paremetro no msm formato da requisicao ex:"%Y-%m-%d %H:%M:%S"
re = datetime.strptime(requisicao, "%Y-%m-%d %H:%M:%S")
# Depois d conversão, fazer a formatação de data e hora
requisicao_reformatada = re.strftime(formatado)


# Passando os dados da api no <loop for>
# Quantidade de dados buscados de acordo com a quantidade de dias solicitada
for c in range(0, dia):
    alta = float(json[c]["high"])
    convertido = locale.currency(alta, grouping=True)
    conversao_cm_format = f"R$ {alta:.4f}".replace(".", ",")

    baixa = float(json[c]["low"])
    convertido2 = locale.currency(baixa, grouping=True)
    conversao_cm_format2 = f"R$ {baixa:.4f}".replace(".", ",")

    taxa_de_cambio = float(json[c]["bid"])
    TaxaConv = locale.currency(taxa_de_cambio, grouping=True)
    TaxaConvFormat = f"R$ {taxa_de_cambio:.4f}".replace(".", ",")

    para_venda = float(json[c]["ask"])
    VendaConver = locale.currency(para_venda, grouping=True)
    VendaConverFormat = f"R$ {para_venda:.4f}".replace(".", ",")

    data_hora = int(json[c]["timestamp"])
    data_hora = datetime.fromtimestamp(data_hora)
    formatado = "%d-%m-%Y %H:%M:%S"
    data_hora = data_hora.strftime(formatado)

    print(nome)
    print(f"Referido a data: {data_hora}")
    print(f"Cambio: {convertido}\n")
    print(f"Refeerente a alta: {convertido}. E baixa: {convertido2}. Valor exato: {conversao_cm_format}, {conversao_cm_format2}")
    print(f"Referente a taxa compra: {TaxaConv}. Varlos exato: {TaxaConvFormat}")
    print(f"Referente a taxa venda: {VendaConver}. Valor exato: {VendaConverFormat}")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")