import json

# Lê o arquivo JSON com os dados de faturamento diário
with open('faturamento.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Extrai os valores de faturamento diário do JSON
faturamento_diario = dados['faturamento_diario']

# Calcula o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcula a média mensal de faturamento diário, ignorando dias sem faturamento
dias_com_faturamento = [valor for valor in faturamento_diario if valor != 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias com faturamento diário acima da média mensal
dias_acima_da_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

# Exibe os resultados
print(f"Menor valor de faturamento diário: R${menor_valor:.2f}")
print(f"Maior valor de faturamento diário: R${maior_valor:.2f}")
print(f"Número de dias com faturamento diário acima da média mensal: {dias_acima_da_media}")
