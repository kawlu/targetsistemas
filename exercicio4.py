def calculo(valor):
    percentual = (valor/total) * 100
    return percentual

SP = 64836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53
total = SP + RJ + MG + ES + OUTROS

estados = {}
estados.update({"SP": calculo(SP)})
estados.update({"RJ": calculo(RJ)})
estados.update({"MG": calculo(MG)})
estados.update({"ES": calculo(ES)})
estados.update({"OUTROS": calculo(OUTROS)})

print("Percentual do valor mensal de faturamento da distribuidora:\n")

for estado, percentual in estados.items():
    print(f"{estado} - {percentual:.2f}%")