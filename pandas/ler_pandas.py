import pandas as pd
import sqlalchemy 
from sqlalchemy import create_engine

con_string = 'postgresql+psycopg2://postgres:1234@localhost:5432/Loja_Gamer'

engine = create_engine(con_string)

query = """
    SELECT *
    FROM vendas
    ORDER BY cliente_id ASC
"""

df_ler_sql = pd.read_sql(query,engine)

print(df_ler_sql)

