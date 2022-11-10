#criação de funções

preço= 1990.90

#calcular imposto
imposto = preço * 0.05
print(imposto)

preço1= 3000
imposto=preço1*0.07
print(imposto)

#declaracao da funcao
def calcular_imposto(preço_produto):
  imposto=preço_produto * 0.05
  return imposto

#uso da funcao
preco = 299
imposto = calcular_imposto(preco)
print(imposto) 