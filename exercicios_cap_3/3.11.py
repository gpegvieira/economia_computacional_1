# Exercício 3.11
preco_i = float(input("Preço original da mercadoria: R$"))
desconto_rel = float(input("Desconto em %:"))

desconto_abs = preco_i * desconto_rel/100
preco_f = preco_i * (1 - desconto_rel/100)

print("Valor do desconto: R$ %.2f" % desconto_abs)
print("Preço a pagar: R$ %.2f" % preco_f)