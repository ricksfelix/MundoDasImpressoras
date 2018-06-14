from tkinter import *
import os
import time

def menu_list(user):
    gui = Tk()
    img = PhotoImage(file="teste.gif")
    img1 = Label(gui)
    img1['image'] = img

    gui.title('Menu List')
    lb_user = Label(gui, text='Bem Vindo "{}!"'.format(user))
    lb_time = Label(gui, text='{}'.format(time.asctime()))
    bt_regs_clt = Button(gui, text='Cadastrar Clientes', command=cadastro)
    lb_user.grid(row=0, column=0)
    lb_time.grid(row=1, column=0)
    bt_regs_clt.grid(row=2, column=0)
    img1.grid(row=3, column=0)
    gui.mainloop()

def cadastro():
    g = Tk()
    g.title('Cadastrar Cliente')
    lb_client = Label(g, text='Nome do Cliente: ')
    lb_email = Label(g, text='E-Mail: ')
    lb_cel = Label(g, text='Celular: ')
    lb_tel = Label(g, text='Telefone: ')
    lb_rua = Label(g, text='Rua: ')
    lb_num = Label(g, text='Numero: ')
    lb_cep = Label(g, text='Cep: ')
    et_rua = Entry(g)
    et_num = Entry(g)
    et_cep = Entry(g)
    et_email = Entry(g)
    et_client = Entry(g)
    et_cel = Entry(g)
    et_tel = Entry(g)
    bt_register = Button(g, text='Cadastrar Equipamento', command=equipamento)
    lb_client.grid(row=0, column=0)
    lb_email.grid(row=1, column=0)
    lb_cel.grid(row=2, column=0)
    lb_tel.grid(row=3, column=0)
    lb_rua.grid(row=4, column=0)
    lb_num.grid(row=5, column=0)
    lb_cep.grid(row=6, column=0)
    et_client.grid(row=0, column=1)
    et_cel.grid(row=1, column=1)
    et_tel.grid(row=2, column=1)
    et_rua.grid(row=3, column=1)
    et_num.grid(row=4, column=1)
    et_cep.grid(row=5, column=1)
    et_email.grid(row=6, column=1)
    bt_register.grid(row=7, columnspan=2)
    g.mainloop()

def equipamento():
    gui = Tk()

    def teste():
        link = 'localhost'
        name = et_name.get()
        tell = et_tel.get()
        eqp = et_eqp.get()
        gen = '''
    <html>
    <head>
        <title>Equipamento: "{}"</title>
        <meta charset="UTF-8"/>
    </head>
    <body>
        <h1>Nome</h1>
        <h2>{}</h2>
        <h1>Telefone</h1>
        <h2>{}</h2>
        <h1>Equipamento</h1>
        <h2>{}</h2>
        <p> QR CODE.</p>
        <img src="QR_LIST/{}.png">
    </body>
    </html>
    '''.format(eqp, name, tell, eqp, eqp)
        os.system('cd /home/haise/Servidor/QR_LIST && qr {}/{}.html >> {}.png'.format(link, eqp, eqp))
        os.system('cd /home/haise/Servidor && echo "{}" >> {}.html'.format(gen, eqp))

    lb_name = Label(gui, text='Name: ')
    lb_tel = Label(gui, text='Telefone: ')
    lb_eqp = Label(gui, text='Equipamento: ')
    et_name = Entry(gui)
    et_tel = Entry(gui)
    et_eqp = Entry(gui)
    bt_confirm = Button(gui, text='Confirm', command=teste)
    lb_name.grid(row=0, column=0)
    lb_tel.grid(row=1, column=0)
    lb_eqp.grid(row=2, column=0)
    et_name.grid(row=0, column=1)
    et_tel.grid(row=1, column=1)
    et_eqp.grid(row=2, column=1)
    bt_confirm.grid(row=3, columnspan=2)
    gui.mainloop()
