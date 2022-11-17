import aula4c as bd
conexao,cursor=bd.conectar()

nome=input('Informe o nome do herói/vilão')
nome_civil=input('Informe o nome civil do herói/vilão')
tipo_numerico=input('Tecle 1 para Herói(na) ou Tecle 2 para Vilã(o)')

sql="SELECT MAX(pessoa_id)+1 from pessoas"
cursor.execute(sql)
numero = curso.fetchone()[0]

if tipo_numerico=='1':
  tipo= "Herói(na)"
else:
  tipo='Vilã(o)'

sql = f"INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES ({pessoa_id}, '{nome}', '{nome_civil}', '{tipo}')" 
cursor.execute(sql)
cursor.commit()
cursor.close()


