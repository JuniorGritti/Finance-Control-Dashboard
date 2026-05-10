                                            #Aplicativo Financeiro
#Bibliotecas:
import os
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar, DateEntry
from datetime import date
from datetime import datetime
from Projeto02_View import tabela, Grafico_Barra, Pizza_valores, Porcentagem_Barra, Adicionar_Categorias, ver_categoria, Adicionar_Receita, Adicionar_Gastos, deletar_gastos, deletar_receitas, formatar_moeda

#Cores:
co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555', '#2f4b7c', '#61a5c2', '#a8dadc', '#457b9d', '#1d3557', '#e63946', '#f4a261', '#e76f51', '#2a9d8f', '#8ab17d', '#b5838d', '#6d597a', '#3d5a80', '#98c1d9']

#Menu:
Menu = Tk()
Menu.title(" ◈ Finance Control | Dashboard ◈")
Menu.geometry("900x650")
Menu.configure(background=co9)
Menu.resizable(width=FALSE, height=FALSE)
pasta_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_ico = os.path.join(pasta_do_script, "assets", "Logo.ico")
Menu.iconbitmap(caminho_ico)
style = ttk.Style(Menu)
style.theme_use("clam")

#Divisão:
frameCima = Frame(Menu, width = 1043, height = 50, bg = co1, relief = "flat")
frameCima.grid(row = 0, column = 0)

frameMeio = Frame(Menu, width = 1043, height = 361, bg = co1, pady = 15, relief = "raised")
frameMeio.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW)

coluna_esquerda = Frame(frameMeio, width=350, height=360, bg=co1)
coluna_esquerda.place(x = 0, y = 0)

coluna_centro = Frame(frameMeio, width=200, height=360, bg=co1)
coluna_centro.place(x = 350, y = 0)

coluna_direita = Frame(frameMeio, width=350, height=360, bg=co1)
coluna_direita.place(x = 550, y = 0)

frameBaixo = Frame(Menu, width = 1043, height = 300, bg = co1, pady = 0, relief = "flat")
frameBaixo.grid(row = 2, column = 0, pady = 1, padx = 0, sticky = NSEW)

frameDados = Frame(frameBaixo, width = 350, height = 250, bg = co1)
frameDados.place(x = 0, y = 0)

frameConfiguracoes = Frame(frameBaixo, width = 220, height = 250, bg = co1)
frameConfiguracoes.place(x = 360, y = 0)

frameInsercoes = Frame(frameBaixo, width = 260, height = 250, bg = co1)
frameInsercoes.place(x = 610, y = 0)

#Imagens:
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
pasta_assets = os.path.join(diretorio_atual, "assets")
caminho_ico = os.path.join(pasta_assets, "Logo.ico")
caminho_logo = os.path.join(pasta_assets, "Logo.png")
caminho_add = os.path.join(pasta_assets, "Adicionar.png")
caminho_del = os.path.join(pasta_assets, "Deletar.png")

#Variáveis (frameCima):
Logo = caminho_logo
fonte_titulo = ("Segoe UI Bold", 12)
fonte_porcentagem = ("Segoe UI", 10, "italic")
fonte_data = ("Segoe UI Bold", 12)

#Saldo Restante (Barra Porcentagem):
l_Porcentagem = Label(frameCima, text = "Saldo Restante (%)", anchor = NW, font = fonte_titulo, bg = co1, fg = co4)
l_Porcentagem.place(x = 10, y = 13)

style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar",
                background = co2,
                troughcolor='#f0f2f5',
                bordercolor=co1,
                lightcolor=co2,
                darkcolor=co2)
style.configure("TProgressbar", thickness = 25)
Barra = Progressbar(frameCima, length = 550, style = "black.Horizontal.TProgressbar")
Barra.place(x = 180, y = 12)
Barra["value"] = Porcentagem_Barra()[0]
valor = Porcentagem_Barra()[0]
l_Porcentagem2 = Label(frameCima, text = "{:.2f}%".format(valor), anchor = NW, font = fonte_porcentagem, bg = co1, fg = co0)
l_Porcentagem2.place(x = 735, y = 13)

#Data:
Hoje = datetime.now().strftime('%d/%m/%Y')
l_Hoje = Label(frameCima, text = Hoje, anchor = NW, font = fonte_data, bg = co1, fg = co4)
l_Hoje.place(x=805, y=13)

#Definições (Tree):
global tree

#Inserindo Categorias (Tempo Real):
def Inserindo_Categorias():
    nome = e_CategoriasGanhos.get()
    lista_inserir = [nome]
    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Preencha novamente...")
            return

#Importando para Função Inserir            
    Adicionar_Categorias(lista_inserir)
    messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    e_CategoriasGanhos.delete(0,"end")

#Função para Categorias:
    Categorias_funcao = ver_categoria()
    Categorias = []
    for i in Categorias_funcao:
        Categorias.append(i[1])

#Atualizando Lista de Categorias:
    Box_Categorias["values"] = (Categorias)
    Atualizando_funcoes()

#Inserindo Ganhos (Função):
def Inserindo_Ganhos():
    nome = "Receita"
    data = e_DataGanhos.get()
    quantia = e_Ganhos.get()
    try:
        if "," in quantia:
            quantia = quantia.replace(".", "")
            quantia = quantia.replace(",", ".")
        quantia = float(quantia)
    except ValueError:
        messagebox.showerror("Erro", "Insira um valor numérico válido.")
        return
    lista_inserir = [nome, data, quantia]
    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Preencha novamente...")
            return
        
 #Inserindo Ganhos (Função):
    Adicionar_Receita(lista_inserir)
    messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    e_DataGanhos.delete(0,"end")
    e_Ganhos.delete(0,"end")
    Atualizando_funcoes()

#Inserindo Gastos (Função):
def Inserindo_Gastos():
    nome = Box_Categorias.get()
    data = e_DataGastos.get()
    quantia = e_Gastos.get()
    try:
        if "," in quantia:
            quantia = quantia.replace(".", "")
            quantia = quantia.replace(",", ".")
        quantia = float(quantia)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")
        return
    lista_inserir = [nome, data, quantia]
    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Preencha novamente...")
            return
        
 #Inserindo Gastos (Função):
    Adicionar_Gastos(lista_inserir)
    messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
    Box_Categorias.delete(0, "end")
    e_DataGastos.delete(0,"end")
    e_Gastos.delete(0,"end")
    Atualizando_funcoes()

#Deletar (Função):
def Deletar_dados():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista =  treev_dicionario["values"]
        valor = treev_lista[0]
        nome = treev_lista[1]
        if nome == "Receita":
            deletar_receitas([valor])
            messagebox.showinfo("Sucesso", "Dados deletados com sucesso!")
        else:
            deletar_gastos([valor])
            messagebox.showinfo("Sucesso", "Dados deletados com sucesso!")
        Atualizando_funcoes()
    except IndexError: 
        messagebox.showerror("Erro", "Selecione algo na tabela...")
    return

#Graficos:
def graficos_bar():
    for widget in coluna_esquerda.winfo_children():
        widget.destroy()
    lista_de_categorias = ["Ganhos", "Gastos", "Saldo"]
    lista_de_valores = Grafico_Barra()
    figura = plt.Figure(figsize = (3.5, 3.5), dpi = 90)
    figura.subplots_adjust(top = 0.90, bottom = 0.15)
    ax = figura.add_subplot(111)
    cor_ganhos = '#2e7d32'
    cor_gastos = '#0a58ca'
    cor_saldo = '#4fa882' if lista_de_valores[2] >= 0 else '#c62828'
    cores_barras = [cor_ganhos, cor_gastos, cor_saldo]
    posicoes_x = [0.25, 1.0, 1.75]
    ax.autoscale(enable = True, axis = 'both', tight = None)
    ax.bar(posicoes_x, lista_de_valores, color = cores_barras, width = 0.69)
    c = 0
    for c, i in enumerate(ax.patches):
        valor = lista_de_valores[c]
        meio_da_barra = i.get_x() + (i.get_width() / 2)
        valor_texto = "{:,.0f}".format(valor).replace(",", ".")
        if valor >= 0:
            ax.annotate(valor_texto, xy = (meio_da_barra, valor), xytext = (0, -5), textcoords = "offset points", fontsize = 10, fontfamily = 'Segoe UI', fontweight = 'bold', horizontalalignment = 'center', verticalalignment = 'top', color = '#ffffff')
        else:
            ax.annotate(valor_texto, xy = (meio_da_barra, valor), xytext = (0, 5), textcoords = "offset points", fontsize = 10, fontfamily = 'Segoe UI', fontweight = 'bold', horizontalalignment = 'center', verticalalignment = 'bottom', color = '#ffffff')
    valor_maximo = max(lista_de_valores)
    valor_minimo = min(lista_de_valores)
    maior_valor = max(abs(valor_maximo), abs(valor_minimo))
    if maior_valor > 100000000:
        Escala = 50000000
    elif maior_valor > 50000000:
        Escala = 20000000
    elif maior_valor > 10000000:
        Escala = 5000000
    elif maior_valor > 1000000:
        Escala = 500000
    elif maior_valor > 500000:
        Escala = 200000
    elif maior_valor > 100000:
        Escala = 50000
    elif maior_valor > 50000:
        Escala = 20000
    elif maior_valor > 10000:
        Escala = 5000
    elif maior_valor > 5000:
        Escala = 1000
    elif maior_valor > 1000:
        Escala = 500
    elif maior_valor > 500:
        Escala = 200
    else:
        Escala = 100
    limite_superior = ((int(valor_maximo) // Escala) + 2) * Escala
    if valor_minimo < 0:
        limite_inferior = ((int(valor_minimo) // Escala) - 1) * Escala
    else:
        limite_inferior = 0
    ax.set_ylim(limite_inferior, limite_superior)
    ax.set_yticks(list(range(int(limite_inferior), int(limite_superior) + 1, Escala)))
    ax.set_xticks(posicoes_x)
    textos_x = ax.set_xticklabels(lista_de_categorias, fontsize = 12, fontweight = 'bold')
    textos_x[0].set_color(cor_ganhos)
    textos_x[1].set_color(cor_gastos)
    textos_x[2].set_color(cor_saldo)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#888888')
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom = False, left = False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color = '#CCCCCC', alpha = 0.4)
    ax.xaxis.grid(False)
    canva = FigureCanvasTkAgg(figura, coluna_esquerda)
    canva.get_tk_widget().place(x = 15, y = -25)

#Resumos:
def resumos():
    for widget in coluna_centro.winfo_children():
        widget.destroy()
    valores = Grafico_Barra()
    container_texto = Frame(coluna_centro, bg = co1)
    container_texto.place(x = 120, y = 130, anchor = CENTER)
    cor_renda = "#2e7d32"
    cor_despesa = "#0a58ca"
    cor_saldo = "#4fa882" if valores[2] >= 0 else "#c62828"
    l_resumo = Label(container_texto, text = "Renda Mensal", font = ("Verdana", 12, "bold"), bg = co1, fg = "#545454").pack(pady = (0, 0))
    l_linhas = Frame(container_texto, width = 170, height = 2, bg = "#000000").pack(pady = (0, 0))
    l_resumo = Label(container_texto, text = formatar_moeda(valores[0]), font = ("Segoe UI", 15, "bold"), bg = co1, fg = cor_renda).pack(pady = (0, 15))

    l_resumo = Label(container_texto, text = "Despesa Mensal", font = ("Verdana", 12, "bold"), bg = co1, fg = "#545454").pack(pady = (0, 0))
    l_linhas = Frame(container_texto, width = 170, height = 2, bg = "#000000").pack(pady = (0, 0))
    l_resumo = Label(container_texto, text = formatar_moeda(valores[1]), font = ("Segoe UI", 15, "bold"), bg = co1, fg = cor_despesa).pack(pady = (0, 15))

    l_resumo = Label(container_texto, text = "Saldo Mensal", font = ("Verdana", 12, "bold"), bg = co1, fg = "#545454").pack(pady = (0, 0))
    l_linhas = Frame(container_texto, width = 170, height = 2, bg = "#000000").pack(pady = (0, 0))
    l_resumo = Label(container_texto, text = formatar_moeda(valores[2]), font = ("Segoe UI", 15, "bold"), bg = co1, fg = cor_saldo).pack(pady = (0, 0))

#Grafico Pizza:
def GraficoPizza():
    for widget in coluna_direita.winfo_children():
        widget.destroy()
    figura = plt.Figure(figsize = (3.5, 3.5), dpi = 90)
    figura.subplots_adjust(left = 0.05, right = 0.95, top = 0.95, bottom = 0.05)
    ax = figura.add_subplot(111)
    try:
        dados = Pizza_valores()
        lista_de_valores = dados[1]
        lista_categorias = dados[0] 
        explode = [0.05] * len(lista_categorias)
        ax.pie(lista_de_valores, wedgeprops = dict(width = 0.3, edgecolor = "#545454", linewidth = 1.0), autopct = '%1.1f%%', colors = colors, shadow = True, startangle = 90, radius = 1.02, pctdistance = 0.85, textprops = {'fontsize': 9, 'color': '#ffffff', 'fontfamily': 'Segoe UI', 'fontweight': 'bold'})
    except Exception as e:
        pass
    canva_categoria = FigureCanvasTkAgg(figura, coluna_direita)
    canva_categoria.get_tk_widget().place(x = 45, y = -30)

#Grafico Pizza (Índice):
def desenhar_legenda():
    for widget in frameMeio.winfo_children():
        if widget.winfo_name() == "legenda_frame":
            widget.destroy()
    frame_legenda = Frame(frameMeio, name = "legenda_frame", bg = co1, width = 880, height = 50)
    frame_legenda.place(x = 10, y = 265)
    frame_legenda.grid_propagate(False)
    for c in range(8):
        frame_legenda.grid_columnconfigure(c, weight = 1, uniform = "colunas")
    try:
        dados = Pizza_valores()
        lista_categorias = dados[0] 
        for i, categoria in enumerate(lista_categorias):
            linha = i // 8
            coluna = 7 - (i % 8)
            cor_fatia = colors[i % len(colors)] 
            f_item = Frame(frame_legenda, bg = co1)
            f_item.grid(row = linha, column = coluna, pady = 2, sticky = E)
            quadradinho = Canvas(f_item, width = 10, height = 10, bg = cor_fatia, bd = 0, highlightthickness = 0)
            quadradinho.pack(side = LEFT, anchor = CENTER)
            Label(f_item, text = categoria, fg = "#545454", bg = co1, font = ("Segoe UI", 9, "bold")).pack(side = LEFT, anchor = CENTER, padx = (4, 0))
    except Exception as e:
        pass

#Registros:
Tabela = Label(frameMeio, text = "Registro de Entradas", anchor = NW, font = ("Verdana", 11, "bold underline"), bg = co1, fg = co4)
Tabela.place(x = 5, y = 325)

#Tabela:
def Registros():
    for widget in frameDados.winfo_children():
        widget.destroy()
    tabela_head = ['#ID','Categorias','Data','Valores (R$)']
    lista_itens = tabela()
    global tree
    tree = ttk.Treeview(frameDados, selectmode="extended",columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frameDados, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDados, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0
    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1
    for item in lista_itens:
        linha_formatada = list(item)
        linha_formatada[3] = formatar_moeda(linha_formatada[3])
        tree.insert('', 'end', values=linha_formatada)

#Registro de Gastos:
l_Descricao = Label(frameInsercoes, text = "Registrar Despesas", height = 1, anchor = NW, font = ("Verdana 10 bold underline"), bg = co1, fg = co4)
l_Descricao.place(x = 75, y = 0)

l_Categorias = Label(frameInsercoes, text = "Categorias:", height = 1, anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_Categorias.place(x = 65, y = 90)

#Categorias:
Categorias_funcao = ver_categoria() 
Categorias = []

for i in Categorias_funcao:
    Categorias.append(i[1])

Box_Categorias = ttk.Combobox(frameInsercoes, width = 10, font = "Ivy 10")
Box_Categorias["values"] = (Categorias)
Box_Categorias.place(x = 140, y = 91)

#Data Valores:
l_DataGastos = Label(frameInsercoes, text = "Data:", height = 1, anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_DataGastos.place(x = 84, y = 30)
e_DataGastos = DateEntry(frameInsercoes, width = 12, background = "darkblue", foreground = "white", borderwidth = 2, year = 2026)
e_DataGastos.place(x = 123, y = 31)

#Valores:
l_Gastos = Label(frameInsercoes, text = "Valor (R$):", height = 1, anchor = NW, font = "Ivy 10", bg = co1, fg = co4)
l_Gastos.place(x = 67, y = 60)
e_Gastos = Entry(frameInsercoes, width = 14, justify = "left", relief = "solid")
e_Gastos.place(x = 138, y = 61)

#Inserir (Botão):
Imagem_InserirGastos = Image.open(caminho_add)
Imagem_InserirGastos = Imagem_InserirGastos.resize((17,17))
Imagem_InserirGastos = ImageTk.PhotoImage(Imagem_InserirGastos)

BotaoInserirGastos = Button(frameInsercoes, command = Inserindo_Gastos, image = Imagem_InserirGastos, text = "Adicionar".upper(), width = 80, compound = LEFT, anchor = NW, font = ("Ivy 7 bold"), bg = co1, fg = co0, overrelief = RIDGE)
BotaoInserirGastos.place(x = 103, y = 121)

#Deletar:
l_Deletar = Label(frameConfiguracoes, text = "Excluir", height = 1, anchor = NW, font = ("Verdana 10 bold underline"), bg = co1, fg = co4)
l_Deletar.place(x = 85, y = 178)

#Deletar (Botão):
Imagem_Deletar = Image.open(caminho_del)
Imagem_Deletar = Imagem_Deletar.resize((17,17))
Imagem_Deletar = ImageTk.PhotoImage(Imagem_Deletar)

BotaoDeletar = Button(frameConfiguracoes, command = Deletar_dados, image = Imagem_Deletar, text = "Deletar".upper(), width = 80, compound = LEFT, anchor = NW, font = ("Ivy 7 bold"), bg = co1, fg = co0, overrelief = RIDGE)
BotaoDeletar.place(x = 67.5, y = 198.5)

#Registrar Ganhos:
l_DescricaoGanhos = Label(frameConfiguracoes, text = "Registrar Ganhos", height = 1, anchor = NW, font = ("Verdana 10 bold underline"), bg = co1, fg = co4)
l_DescricaoGanhos.place(x = 45, y = 0)

#Data Ganhos:
l_DataGanhos = Label(frameConfiguracoes, text = "Data:", height = 1, anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_DataGanhos.place(x = 45, y = 30)
e_DataGanhos = DateEntry(frameConfiguracoes, width = 12, background = "darkblue", foreground = "white", borderwidth = 2, year = 2026)
e_DataGanhos.place(x = 85, y = 31)

#Valores:
l_Ganhos = Label(frameConfiguracoes, text = "Valor (R$):", height = 1, anchor = NW, font = "Ivy 10", bg = co1, fg = co4)
l_Ganhos.place(x = 31, y = 60)
e_Ganhos = Entry(frameConfiguracoes, width = 14, justify = "left", relief = "solid")
e_Ganhos.place(x = 102, y = 61)

#Inserir Ganhos (Botão):
Imagem_InserirGanhos = Image.open(caminho_add)
Imagem_InserirGanhos = Imagem_InserirGanhos.resize((17,17))
Imagem_InserirGanhos = ImageTk.PhotoImage(Imagem_InserirGanhos)

BotaoInserirGanhos = Button(frameConfiguracoes, command = Inserindo_Ganhos, image = Imagem_InserirGanhos, text = "Adicionar".upper(), width = 80, compound = LEFT, anchor = NW, font = ("Ivy 7 bold"), bg = co1, fg = co0, overrelief = RIDGE)
BotaoInserirGanhos.place(x = 70, y = 91)

#Categorias de Ganhos:
l_CategoriasGanhos = Label(frameInsercoes, text = "Registrar Categorias", height = 1, anchor = NW, font = ("Verdana 10 bold underline"), bg = co1, fg = co4)
l_CategoriasGanhos.place(x = 67.5, y = 178)
e_CategoriasGanhos = Entry(frameInsercoes, width = 14, justify = "left", relief = "solid")
e_CategoriasGanhos.place(x = 55, y = 203)

#Inserir Categorias (Botão):
Imagem_InserirCategoriasGanhos = Image.open(caminho_add)
Imagem_InserirCategoriasGanhos = Imagem_InserirCategoriasGanhos.resize((17,17))
Imagem_InserirCategoriasGanhos = ImageTk.PhotoImage(Imagem_InserirCategoriasGanhos)

BotaoInserirCategorias = Button(frameInsercoes, command = Inserindo_Categorias, image = Imagem_InserirCategoriasGanhos, text = "Adicionar".upper(), width = 80, compound = LEFT, anchor = NW, font = ("Ivy 7 bold underline"), bg = co1, fg = co0, overrelief = RIDGE)
BotaoInserirCategorias.place(x = 150, y = 198.5)

#Atualizando Funções:
def Atualizando_funcoes():
    graficos_bar()
    resumos()
    GraficoPizza()
    desenhar_legenda()
    Registros()
    V_porcentagem = Porcentagem_Barra()[0]
    Barra["value"] = V_porcentagem
    l_Porcentagem2.config(text="{:.2f}%".format(V_porcentagem))
Atualizando_funcoes()

Menu.mainloop()