def calcular_conversao(valor_em_reais):
    conversao = {
        'Dólar Americano': valor_em_reais / 4.91,
        'Peso Argentino': valor_em_reais / 0.02,
        'Dólar Australiano': valor_em_reais / 3.18,
        'Dólar Canadense': valor_em_reais / 3.64,
        'Franco Suiço': valor_em_reais / 0.42,
        'Euro': valor_em_reais / 5.36,
        'Libra esterlina': valor_em_reais / 6.21
    }
    return conversao


valor_em_reais = float(input("Digite o valor em reais: "))
resultado = calcular_conversao(valor_em_reais)
for moeda, valor in resultado.items():
    print(f'Com R$ {valor_em_reais:.2f}, você pode comprar {valor:.2f} {moeda}')
