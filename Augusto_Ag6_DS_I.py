# Programa de desconto progressivo

#Solicita o valor da compra
valor = float(input("Digite o valor total da compra:"))

#Verifica o desconto
if valor < 200:
    desconto = valor * 0.05

elif valor > 300:
    desconto = valor * 0.10

else:
    desconto = valor * 0.15

#Calcula o valor final
valor_final = valor - desconto

# Exibe os resultados
print(f"Valor da compra : R$ {valor:.2f}")
print(f"Desconto : R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_final:.2f}")