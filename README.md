# ControleDeEstoqueCRUD
 Integrações com SQL Server e Tkinter.  Utilização do Figma.

 Observações sobre comandos, bibliotecas e interações.

 - Para adicionar, preencha os quatro campos.
 - Para deletar, preencha nome e lote.
 - Para registrar uso, preencha nome e quantidade.
 - Para procurar, preencha o nome.


 - Foi utilizado o Figma para fazer a parte visual do sistema e o Proxylight Designer para gerar o código
 - das caixas e botões.
 - Criou-se uma def para cada entrada e com comandos de SQL, poder fazer as interações CRUD com o Banco.
 - Foi utilizado o SQL Server.
 - Através da biblioteca pyodbc, conseguimos fazer a conexão com o servidor de Banco de Dados SQL.
 - O tkinter.messagebox, servirá para apresentar uma informação após adicionar um produto, por exemplo.
 - O commit salva a alteração no banco de dados.
 - O SET na função de uso de insumo, é para alterar a qtde na coluna nome_insumo.
 - cursor.fetchall() gera uma lista em memória, em que cada item da lista é uma linha do banco de dados que ele pegou.
 - MUITO IMPORTANTE !! 
    A variável texto do FOR da def procurar_insumo, os nomes entre chaves, são das colunas da tabela Insumos em nosso BD,
e não variáveis do Pyhton. Esses nomes vieram da integração com o banco de dados através do comando cursor.fetchall().


