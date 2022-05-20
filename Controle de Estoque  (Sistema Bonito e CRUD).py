#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Observações sobre comandos, bibliotecas e interações.

# Para adicionar, preencha os quatro campos.
# Para deletar, preencha nome e lote.
# Para registrar uso, preencha nome e quantidade.
# Para procurar, preencha o nome.


# Foi utilizado o Figma para fazer a parte visual do sistema e o Proxylight Designer para gerar o código
# das caixas e botões.
# Criou-se uma def para cada entrada e com comandos de SQL, poder fazer as interações CRUD com o Banco.
# Foi utilizado o SQL Server.
# Através da biblioteca pyodbc, conseguimos fazer a conexão com o servidor de Banco de Dados SQL.
# O tkinter.messagebox, servirá para apresentar uma informação após adicionar um produto, por exemplo.
# O commit salva a alteração no banco de dados.
# O SET na função de uso de insumo, é para alterar a qtde na coluna nome_insumo.
# cursor.fetchall() gera uma lista em memória, em que cada item da lista é uma linha do banco de dados que ele pegou.
# MUITO IMPORTANTE !! 
# A variável texto do FOR da def procurar_insumo, os nomes entre chaves, são das colunas da tabela Insumos em nosso BD,
# e não variáveis do Pyhton. Esses nomes vieram da integração com o banco de dados através do comando cursor.fetchall().


from tkinter import *
import pyodbc
import tkinter.messagebox

# integração com o Banco de Dados
dados_conexao = ("Driver={SQL Server};"
                 "Server=LAPTOP;"
                 "Database=ControleEstoque")
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

 
def adicionar_insumo():
    nome_insumo = entry0.get()
    data_validade = entry1.get()
    lote = entry2.get()
    qtde = entry3.get()
    comando = f"""INSERT INTO Insumos(nome_insumo, data_validade, lote, qtde)
    VALUES
        ('{nome_insumo}', '{data_validade}', '{lote}', '{qtde}')"""
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Adicionar Produto",message="Produto Adicionado com Sucesso")
    entry0.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)    
    
       
def deletar_insumo():
    nome_insumo = entry0.get()
    lote = entry2.get()
    comando = f"""DELETE from Insumos
            WHERE nome_insumo = '{nome_insumo}'
            AND lote = '{lote}';
            """
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Uso Excluído",message=f"{nome_insumo} do lote {lote} foi excluído(a) do Banco de Dados")
    entry0.delete(0, END)
    entry2.delete(0, END)
    
      
def registrarUso_insumo():
    nome_insumo = entry0.get()
    qtde_usada = entry3.get()
    comando = f"""UPDATE Insumos
        SET qtde = qtde - {qtde_usada}
        WHERE nome_insumo = '{nome_insumo}';
        """
    cursor.execute(comando)
    cursor.commit()
    tkinter.messagebox.showinfo(title="Aviso Uso Insumo",message=f"{qtde_usada} unidades de {nome_insumo} foram usadas")
    entry0.delete(0, END)
    entry3.delete(0, END)
    
        
def procurar_insumo():
    nome_insumo = entry0.get()   
    comando = f"""SELECT * from Insumos
            WHERE nome_insumo = '{nome_insumo}';
            """
    cursor.execute(comando)
    # entry4.delete("1.0", END) -> se quiser que vá limpando o campo do resultado a cada procura, deixe essa linha ativa.
    for linha in cursor.fetchall():
        texto = f"Item: {linha.nome_insumo}\n Quantidade: {linha.qtde}\n Lote:{linha.lote}\n Validade:{linha.data_validade}\n"
        entry4.insert("1.0", texto)
        entry0.delete(0, END)


window = Tk()

window.geometry("670x700")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 700,
    width = 670,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    371.0, 355.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = adicionar_insumo,
    relief = "flat")

b0.place(
    x = 118, y = 147,
    width = 200,
    height = 35)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = deletar_insumo,
    relief = "flat")

b1.place(
    x = 118, y = 210,
    width = 200,
    height = 35)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = registrarUso_insumo,
    relief = "flat")

b2.place(
    x = 413, y = 147,
    width = 200,
    height = 35)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = procurar_insumo,
    relief = "flat")

b3.place(
    x = 413, y = 210,
    width = 200,
    height = 35)


entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    514.0, 315.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 414, y = 295,
    width = 200,
    height = 38)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    514.0, 368.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 414, y = 348,
    width = 200,
    height = 38)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvas.create_image(
    514.0, 421.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 414, y = 401,
    width = 200,
    height = 38)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    513.0, 474.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry3.place(
    x = 413, y = 454,
    width = 200,
    height = 38)

# TextArea
entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    370.0, 603.5,
    image = entry4_img)

entry4 = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry4.place(
    x = 126, y = 539,
    width = 488,
    height = 127)


window.resizable(False, False)
window.mainloop()


# In[ ]:





# In[ ]:




