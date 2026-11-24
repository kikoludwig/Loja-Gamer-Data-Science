






import psycopg2
import pandas as pd

conexao = psycopg2.connect(
    host="localhost",
    database="Loja_Gamer",
    user="postgres",
    password="1234",
    port="5432"
)


cursor = conexao.cursor()


query = """
   SELECT *
   FROM clientes
"""

cursor.execute(query)

resultado = []
for i, data in enumerate(cursor):
    resultado.append(data)
    

    
df = pd.DataFrame(resultado)
df.columns = ['id','Nome','Idade','Cidade','Estado','Sexo','Data Compra']
print(df)

conexao.close()
cursor.close()