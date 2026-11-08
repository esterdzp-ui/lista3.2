# EXERCÍCIO 13: Operador de Resto (%)
# Enunciado: Use o operador % para verificar se o número de moedas do jogador é par (moedas % 2 == 0)

# ENTRADA
moedas = int(input("Digite a quantidade de moedas: "))

# PROCESSAMENTO + SAÍDA
eh_par = moedas % 2 == 0
print(f"A quantidade de moedas é par? {eh_par}")

