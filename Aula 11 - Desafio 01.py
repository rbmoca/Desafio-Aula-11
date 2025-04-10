import tkinter as tk
from   tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from   tkinter import ttk
from   tkinter import messagebox
from   matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def carregar_dados():
    df = pd.read_csv('dados.csv')
    df = df.dropna() # Remover valores vazios
    df = df.drop_duplicates() # Remover valores duplicados
    return df

def mostrar_estatistica():
    limpar_display()

    if dados.empty:
        messagebox.showwarning('Atenção!!!','Não existe dados')
        return
    
    texto = Text(display_frame, wrap=NONE)
    texto.pack(fill='both',expand = True)
    texto.insert(END, 'ESTATISTICA')
    texto.insert(END, dados.describe(include='all').to_string())

def mostrar_grafico_barras():
    limpar_display()

    if dados.empty:
         messagebox.showwarning('Atenção!!!','Não existe dados')
         return
    
    print ('Entrei aqui')

    fig, ax = plt.subplots(figsize=(8,5))

  
    if 'vendas' in dados.columns and 'vendedor' in dados.columns:
         
        print ('Entrei aqui!!!!!')
        
        valor_vendas = dados.groupby('vendedor')['vendas'].sum()
        valor_vendas.plot(kind='bar',ax=ax,color='green') 
        ax.set_title('Vendas por Vendedores')
        ax.set_ylabel('Vendedores')
        ax.tick_params(axis = 'x', rotation = 45)

    else:
       print('Erro')

    canvas = FigureCanvasTkAgg(fig, master= display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


def mostrar_grafico_plot():
    limpar_display()

    if dados.empty:
         messagebox.showwarning('Atenção!!!','Não existe dados')
         return
    
    print ('Entrei aqui')

    fig, ax = plt.subplots(figsize=(8,5))

    if 'vendas' in dados.columns and 'vendedor' in dados.columns:
         
        print ('Entrei aqui!!!!!')
        vendas   = dados['vendas']
        vendedor = dados['vendedor']

        ax.plot(vendedor, vendas, marker='o', linestyle='-', color='b')

        # add as labels
        ax.set_title('Vendas por Vendedores')
        ax.set_ylabel('Valores de Vendas')
        ax.tick_params(axis = 'x', rotation = 45)

    else:
       print('Erro')

    canvas = FigureCanvasTkAgg(fig, master= display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


def mostrar_grafico_histograma():
    limpar_display()

    if dados.empty:
         messagebox.showwarning('Atenção!!!','Não existe dados')
         return
    
    print ('Entrei aqui')

    fig, ax = plt.subplots(figsize=(8,5))

    if 'vendas' in dados.columns and 'vendedor' in dados.columns:
         
        print ('Entrei aqui!!!!!')
        vendas   = dados['vendas']
        vendedor = dados['vendedor']

        ax.hist(vendas,bins=7, edgecolor='blue')
        # add as labels
        ax.set_title('Frequencia Vendas')
        ax.set_ylabel('Qtde de Vendas')
        ax.tick_params(axis = 'x', rotation = 45)

    else:
       print('Erro')

    canvas = FigureCanvasTkAgg(fig, master= display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def mostrar_grafico_pizza():
    limpar_display()

    if dados.empty:
         messagebox.showwarning('Atenção!!!','Não existe dados')
         return
    
    print ('Entrei aqui')

    fig, ax = plt.subplots(figsize=(8,5))

    if 'vendas' in dados.columns and 'vendedor' in dados.columns:
         
        print ('Entrei aqui!!!!!')
        vendas   = dados['vendas']
        vendedor = dados['vendedor']

        # PIZZA***
        ax.pie(vendas, labels=vendedor, autopct='%.1f%%')

        # add as labels
        ax.set_title('Participação em Vendas')
        # ax.set_ylabel('Qtde de Vendas')
        # ax.tick_params(axis = 'x', rotation = 45)

    else:
       print('Erro')

    canvas = FigureCanvasTkAgg(fig, master= display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)

def mostrar_grafico_scatter():
    limpar_display()

    if dados.empty:
         messagebox.showwarning('Atenção!!!','Não existe dados')
         return
    
    print ('Entrei aqui')

    fig, ax = plt.subplots(figsize=(8,5))

    if 'vendas' in dados.columns and 'vendedor' in dados.columns:
         
        print ('Entrei aqui!!!!!')
        vendas   = dados['vendas']
        vendedor = dados['vendedor']

        # DISPERSÃO***
        ax.scatter(vendedor, vendas, color='red')
        # ax.pie(vendas, labels=vendedor, autopct='%.1f%%')

        # add as labels
        ax.set_title('Distribuição em Vendas')
        # ax.set_ylabel('Qtde de Vendas')
        # ax.tick_params(axis = 'x', rotation = 45)

    else:
       print('Erro')

    canvas = FigureCanvasTkAgg(fig, master= display_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


def limpar_display():
    for widget in display_frame.winfo_children():
        widget.destroy()

dados = carregar_dados()


# TKINTER

root = tk.Tk()
root.title('ANÁLISE DE DADOS')
root.geometry('800x600')

main_frame = ttk.Frame(root,padding = 10)
main_frame.pack(fill='both',expand=True)

ttk.Label(main_frame, text = 'ANALISE', font=('Arial', 16)).pack()

btn_frame = ttk.Frame(main_frame)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text='Gráfico de Barras',command = mostrar_grafico_barras).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Gráfico de Linha',command = mostrar_grafico_plot).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Gerar Histograma',command = mostrar_grafico_histograma).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Gerar Pizza',command = mostrar_grafico_pizza).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Gerar Scatter',command = mostrar_grafico_scatter).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Gerar estatística',command = mostrar_estatistica).pack(side='left', padx=5)
ttk.Button(btn_frame, text='Limpar dados',command = limpar_display).pack(side='left', padx=5)

display_frame = ttk.Frame(main_frame)
display_frame.pack(fill='both',expand=True)

root.mainloop()

