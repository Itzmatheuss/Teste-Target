# 3 Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 


import json

# Carregar os dados do JSON
with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)

# Filtrar somente os dias com faturamento > 0
faturamento_valido = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Calcular o menor e maior faturamento
menor = min(faturamento_valido)
maior = max(faturamento_valido)

# Calcular a média mensal (desconsiderando os dias com faturamento 0)
media = sum(faturamento_valido) / len(faturamento_valido)

# Contar os dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media)

# Exibir os resultados
print(f"Menor faturamento: R$ {menor:.2f}")
print(f"Maior faturamento: R$ {maior:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
