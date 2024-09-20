import json

with open("dados.json", "r") as file:
    dados = json.load(file)

total = maior = menor = contador = 0
menor = 9999
totalDias = len(dados)

for relatorio in dados:
    
    if relatorio["valor"] > maior:
        maior = relatorio["valor"]
        diaMaior = relatorio["dia"]
        
    if relatorio["valor"] < menor:
        menor = relatorio["valor"]
        diaMenor = relatorio["dia"]
        
    total += relatorio["valor"]
    if relatorio["valor"] > total/totalDias:
        contador+= 1
        
print(f"O maior valor foi de {maior} no {diaMaior}° dia do mês")
print(f"O menor valor foi de {menor} no {diaMenor}° dia do mês")
print(f"Houveram {contador} dias que ultrapassaram a média mensal")