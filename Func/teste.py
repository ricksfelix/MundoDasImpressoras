from tkinter import *
from tkinter import ttk
gui = Tk()
gui.title('Cadastrar Equipamento')

fm_cliente = LabelFrame(gui, text='Cliente')
fm_equipamento = LabelFrame(gui, text='Equipamento')

#Declarando Widgets de Cadastro de Clientes

lb_cliente = Label(fm_cliente, text='Razão Social/Nome: ', padx=0)
lb_tipo = Label(fm_cliente, text='Tipo:')
lb_cel = Label(fm_cliente, text='Celular: ', padx=0)
lb_tel = Label(fm_cliente, text='Telefone: ', padx=0)
lb_email = Label(fm_cliente, text='E-mail: ', padx=0)
lb_ender = Label(fm_cliente, text='Endereço: ', padx=0)
lb_num = Label(fm_cliente, text='Nº: ', padx=0)
lb_os = Label(fm_cliente, text='Numero de OS')

cb_tipo = ttk.Combobox(fm_cliente)
cb_tipo['values'] = ('Fisica', 'Juridica')

et_cliente = Entry(fm_cliente)
et_cel = Entry(fm_cliente)
et_tel = Entry(fm_cliente)
et_email = Entry(fm_cliente)
et_ender = Entry(fm_cliente, width=18)
et_num = Entry(fm_cliente, width=5)
et_os = Entry(fm_cliente, width=11, fg='red', bg='black')
et_os.insert(0, '*415*')
#Demarcando Posições dos Widgets Clientes

fm_cliente.grid(row=0, column=0)
lb_cliente.grid(row=0, column=0)
lb_tipo.grid(row=0, column=2)
cb_tipo.grid(row=0, column=3)
lb_cel.grid(row=1, column=0, sticky=W)
lb_tel.grid(row=2, column=0, sticky=W)
lb_email.grid(row=3, column=0, sticky=W)
lb_ender.grid(row=4, column=0, sticky=W)
lb_num.grid(row=5, column=0, sticky=W)
et_cliente.grid(row=0, column=1, sticky=W)
et_cel.grid(row=1, column=1, sticky=W)
et_tel.grid(row=2, column=1, sticky=W)
et_email.grid(row=3, column=1, sticky=W)
et_ender.grid(row=4, column=1, sticky=W)
et_num.grid(row=5, column=1, sticky=W)
lb_os.grid(row=4, column=3, sticky=E)
et_os.grid(row=5, column=3, sticky=E)

#Declarando Widget De Cadastro de Equipamento

lb_equipamento = Label(fm_equipamento, text='Equipamento:')
lb_modelo = Label(fm_equipamento, text='Modelo:')
lb_cor = Label(fm_equipamento, text='Cor:')
lb_ns = Label(fm_equipamento, text='Numero de Serie:')
lb_acessorios = Label(fm_equipamento, text='Acessorios:')
lb_defeito = Label(fm_equipamento, text='Defeito:')

et_equipamento = Entry(fm_equipamento)
et_modelo = Entry(fm_equipamento)
et_cor = Entry(fm_equipamento)
et_ns = Entry(fm_equipamento)
et_acessorios = Entry(fm_equipamento)
et_defeito = Entry(fm_equipamento)

#Declarando Posição de Widgets de Equipamento

fm_equipamento.grid(row=1, column=0)
lb_equipamento.grid(row=0, column=0)
lb_modelo.grid(row=1, column=0)
lb_cor.grid(row=2, column=0)
lb_ns.grid(row=3, column=0)
lb_acessorios.grid(row=4, column=0)
lb_defeito.grid(row=5, column=0)

et_equipamento.grid(row=0, column=1)
et_modelo.grid(row=1, column=1)
et_cor.grid(row=2, column=1)
et_ns.grid(row=3, column=1)
et_acessorios.grid(row=4, column=1)
et_defeito.grid(row=5, column=1)
lb_result = Label(gui, text='')
bt_cadastrar = Button(gui, text='Cadastrar')
lb_result.grid(row=11, columnspan=2)
bt_cadastrar.grid(row=12, columnspan=2)
gui.mainloop()






































"""
from tkinter import *
import os
import time
a = time.localtime()
data = ('Hora: {}:{} Data: {}/{}/{} '.format(a[3], a[4], a[2], a[1], a[0]))

def cad_eqp():
    link = 'localhost'
    equipamento = et_equipamento.get()
    modelo = et_modelo.get()
    cor = et_cor.get()
    ns = et_ns.get()
    acessorios = et_acessorios.get()
    defeito = et_defeito.get()
    html = '''
<!DOCTYPE html>
    <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <title>Dados Do Equipamento: {}</title>
            <meta name="author" content="Henrique Félix">
            <meta name="description" content="Mundo das Impressoras">
            <link rel="stylesheet" href="../css/equipamentos.css">
        </head>
        <body>
            <div class="principal">
                <header>
                    <img src="../imagens/logo2.jpg">
                </header>
                <nav>
                    <a HREF="localhost/index.html" TARGET="_blank" > Home</a> 
                    <a HREF="/os/Laserjet.html" TARGET="_blank" > Laserjet</a> 
                    <a HREF="/os/teste.html" TARGET="_blank" > teste</a> 
                    <a HREF="/os" TARGET="_blank" > Lista</a> 
                </nav>
                <section>
                    <h1>Dados Do Equipamento</h1>
                    <br>
                    <h1>{}</h1>
                    <br>
                    <h1>Equipamento: {}</h1>
                    <br>
                    <h2>Modelo: {}</h2>
                    <br>
                    <h2>Cor: {}</h2>
                    <br>
                    <h2>Numero de Serie: {}</h2>
                    <br>
                    <h2>Acessorios: {}</h2>
                    <br>
                    <h2>Defeito: {}</h2>
                    <br>
                    <h1>QRCODE</h1><img src=QR_LIST/{}{}.png> 
                </section>
                <aside>Conteudo relacionado</aside>
                <footer><img src=../imagens/rodape.jpg></footer>
        </body>
    </html>
'''.format(equipamento, data, equipamento, modelo, cor, ns, acessorios, defeito, equipamento, modelo)
    os.system('cd /home/haise/Servidor/os/QR_LIST && qr {}.html >> {}{}.png'.format(link, equipamento,modelo))
    os.system('cd /home/haise/Servidor/os && echo "{}" >> {}.html'.format(html, equipamento))


gui = Tk()
gui.title('Cadastrar Equipamento')
lb_equipamento = Label(gui, text='Equipamento:')
lb_modelo = Label(gui, text='Modelo:')
lb_cor = Label(gui, text='Cor:')
lb_ns = Label(gui, text='Numero de Serie:')
lb_acessorios = Label(gui, text='Acessorios:')
lb_defeito = Label(gui, text='Defeito:')

et_equipamento = Entry(gui)
et_modelo = Entry(gui)
et_cor = Entry(gui)
et_ns = Entry(gui)
et_acessorios = Entry(gui)
et_defeito = Entry(gui)
lb_result = Label(gui, text='')

bt_cadastrar = Button(gui, text='Cadastrar', command=cad_eqp)

lb_equipamento.grid(row=0, column=0)
lb_modelo.grid(row=1, column=0)
lb_cor.grid(row=2, column=0)
lb_ns.grid(row=3, column=0)
lb_acessorios.grid(row=4, column=0)
lb_defeito.grid(row=5, column=0)

et_equipamento.grid(row=0, column=1)
et_modelo.grid(row=1, column=1)
et_cor.grid(row=2, column=1)
et_ns.grid(row=3, column=1)
et_acessorios.grid(row=4, column=1)
et_defeito.grid(row=5, column=1)
lb_result.grid(row=6, columnspan=2)
bt_cadastrar.grid(row=7, columnspan=2)

gui.mainloop()

"""

"""
    if equipamento == '':
        lb_result['text'] = 'É Obrigatorio Preencher o *Equipamento*'
        lb_result['fg'] = 'red'
    else:
        if modelo == '':
            lb_result['text'] = 'É Obrigatorio Preencher o *Modelo*'
            lb_result['fg'] = 'red'
        else:
            if cor == '':
                lb_result['text'] = 'É Obrigatorio Preencher a *Cor*'
                lb_result['fg'] = 'red'
            else:
                if ns == '':
                    lb_result['text'] = 'É Obrigatorio Preencher o *Numero de Serie*'
                    lb_result['fg'] = 'red'
                else:
                    if defeito == '':
                        lb_result['text'] = 'É Obrigatorio Especificar o Defeito!'
                        lb_result['fg'] = 'red'
                    else:
                        lb_result['text'] = 'Cadastrado com Sucesso'
                        lb_result['fg'] = 'green'
                        if acessorios == '':
                            acessorios = 'Sem Acessorios'
"""