                                            #Aplicativo Financeiro
#Bibliotecas:
import sqlite3 as lite

#Conexões:
con = lite.connect("Dados.db")

#Categorias:
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categorias(Id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

#Receita:
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receitas(Id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

#Despesas:
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Gastos(Id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)")