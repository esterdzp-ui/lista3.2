# EXERCÍCIO 17: Sistema de Compra
# Enunciado: Uma espada custa 100 moedas. O jogador tem 120.
# Escreva uma expressão que retorne True se o jogador tiver dinheiro suficiente para comprar.

# ENTRADA
preco_espada = 100
dinheiro_jogador = 120

# PROCESSAMENTO
pode_comprar = dinheiro_jogador >= preco_espada

# SAÍDA
print(f"Tem dinheiro para comprar a espada? {pode_comprar}")
