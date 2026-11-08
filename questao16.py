# EXERCÍCIO 16: Verificação de Inventário
# Enunciado: O limite de peso de um inventário é 50kg. O jogador está carregando 48kg e tenta pegar um item de 3kg.
# Use operadores para verificar se o novo peso será menor ou igual ao limite.
# ENTRADA
peso_atual = 48
peso_item = 3
limite = 50
# PROCESSAMENTO
novo_peso = peso_atual + peso_item
pode_pegar = novo_peso <= limite
# SAÍDA
print(f"Novo peso: {novo_peso}")
print(f"Pode pegar o item? {pode_pegar}")

