                                            #Aplicativo Financeiro
#Bibliotecas:
import os
import sqlite3 as lite
import pandas as pd
from Projeto02 import con

#Conexões:
pasta_do_view = os.path.dirname(os.path.abspath(__file__))
caminho_db = os.path.join(pasta_do_view, "Dados.db")
con = lite.connect(caminho_db)

#Adicionando Categorias:
def Adicionar_Categorias(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categorias (nome) VALUES (?)"
        cur.execute(query, i)

#Adicionando Receita:
def Adicionar_Receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

#Adicionando Gastos:
def Adicionar_Gastos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)"
        cur.execute(query, i)

#Função Delete:
def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receitas Where id=?"
        cur.execute(query, i)

def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Gastos Where id=?"
        cur.execute(query, i)

#Visualização de Dados:
def ver_categoria():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categorias")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

def ver_receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Gastos")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)
    return lista_itens

#Dados da Tabela:
def tabela():
    Gastos = ver_gastos()
    Receitas = ver_receitas()
    tabela_lista = []
    for i in Gastos:
        tabela_lista.append(i)
    for i in Receitas:
        tabela_lista.append(i)
    return tabela_lista

#Grafico Barra (Ganhos):
def Grafico_Barra():
    Receitas_dados = ver_receitas()
    Receitas_lista = []
    for i in Receitas_dados:
        Receitas_lista.append(i[3])
    Receita_total = sum(float(str(i).replace(",", ".")) for i in Receitas_lista)
#Grafico Barra (Gastos):
    Despesas_dados = ver_gastos()
    Despesas_lista = []
    for i in Despesas_dados:
        Despesas_lista.append(i[3])
    Despesa_total = sum(float(str(i).replace(",", ".")) for i in Despesas_lista)

#Grafico Barra (Saldo):
    Saldo_total = Receita_total - Despesa_total
    return [Receita_total, Despesa_total, Saldo_total]

#Grafico Pizza (Função):
def Pizza_valores():
    Gastos = ver_gastos()
    Tabela_lista = []
    for i in Gastos:
        Tabela_lista.append(i)
    DataFrame = pd.DataFrame(Tabela_lista, columns = ["id","categoria", "data", "valor"])
    DataFrame['valor'] = DataFrame['valor'].astype(str).str.replace(',', '.')
    DataFrame['valor'] = pd.to_numeric(DataFrame['valor'], errors='coerce').fillna(0)
    DataFrame = DataFrame.groupby("categoria")["valor"].sum()
    Lista_valor = DataFrame.values.tolist()
    Lista_categorias = []
    for i in DataFrame.index:
        Lista_categorias.append(i)
    return([Lista_categorias, Lista_valor])

#Porcentagem Barra (Ganhos):
def Porcentagem_Barra():
    Receitas_dados = ver_receitas()
    Receitas_lista = []
    for i in Receitas_dados:
        Receitas_lista.append(i[3])
    Receita_total = sum(float(str(i).replace(",", ".")) for i in Receitas_lista)

#PPorcentagem Barra (Gastos):
    Despesas_dados = ver_gastos()
    Despesas_lista = []
    for i in Despesas_dados:
        Despesas_lista.append(i[3])
    Despesa_total = sum(float(str(i).replace(",", ".")) for i in Despesas_lista)

#Porcentagem Barra (Função):
    if Receita_total != 0:
        Porcentagem_total = ((Receita_total - Despesa_total) / Receita_total) * 100
    else:
        Porcentagem_total = 0
    return [Porcentagem_total]

#Formatando Moeda:
def formatar_moeda(valor):
    try:
        if isinstance(valor, str):
            valor_limpo = valor.upper().replace("R$", "").strip()
            valor_limpo = valor_limpo.replace(".", "").replace(",", ".")
            numero_float = float(valor_limpo)
        else:
            numero_float = float(valor)
        valor_formatado = f"{numero_float:,.2f}"
        valor_br = valor_formatado.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {valor_br}"
    except ValueError:
        return "R$ 0,00"