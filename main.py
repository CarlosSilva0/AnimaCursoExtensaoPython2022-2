#AULA 2
#permite que o usuário digite algo
nome = input('Digite seu nome: ') 

idade = int(input('Digite a sua idade: '))
genero = input('Qual é o seu gênero M:Masculino, F:Feminino, O=Outro: ')
dobro = idade *2
print ('O dobro da idade informada {}'.format(dobro))

#estrutura condicional (IF) 
if idade>=18:
  print('Você é maior de idade já pode dirigir') 
else:
  print("você é menor de idade melhor tomar leitinho")
if idade >=18 and genero == "M":
  print("Você precisa servir o exercito")
  