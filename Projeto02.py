                                            #Aplicativo Financeiro
#Bibliotecas:
import os
import sqlite3 as lite
import pandas as pd

#Conexões:
pasta_raiz = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(pasta_raiz, "Dados.db")
con = lite.connect(caminho_db)

#Categorias:
def iniciar_banco():
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Categorias(Id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

#Receita:
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Receitas(Id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

#Despesas:
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Gastos(Id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")

iniciar_banco()
