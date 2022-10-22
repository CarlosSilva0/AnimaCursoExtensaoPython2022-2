# Meu primeiro projeto Python!!!
#print () = comando de saída
print ('Hello World!') 
#quando quiser guardar uma String!(frase)
nome = 'Carlos Eduardo Pereira da Silva'
#quando eu quiser guardar um número inteiro
idade = 22
#exibir meu nome(que está dentro da váriavel nome)
print(nome)
#quando eu quiser exibir a frase 'Minha idade é' completando com a váriavel idade
print(f'Minha idade é {idade} anos')
#quando eu quiser exibir 'Meu nome é... e tenho... anos, trocando pelas variáveis nome e idade
print ('Meu nome é {} e tenho {} anos'.format(nome, idade)) 

palavra = 'Banana Naninca'
contagem = 0 
for letter in palavra:
  if letter == 'a':
    contagem = contagem + 1
    print (contagem)   

word= 'Calma'
print (word) 

fruta = 'Morango'
print (fruta[:3])

indice = 0
while indice < len(fruta):
  letra = fruta [indice]
  print(letra)
  indice = indice + 1

for char in fruta:
  print (char)

l = 'Santos Futebol'
print (l[0:6])
print (l[7:14])
