from tkinter import *
import os
import time
a = time.localtime()
b = ('Hora: {}:{}\nData: {}/{}/{} '.format(a[3], a[4], a[2], a[1], a[0]))
data = ('Hora: {}:{} Data: {}/{}/{} '.format(a[3], a[4], a[2], a[1], a[0]))
def menu_list(user):
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

        def cad_eqp():
            link = 'localhost'
            equipamento = et_equipamento.get()
            modelo = et_modelo.get()
            cor = et_cor.get()
            ns = et_ns.get()
            acessorios = et_acessorios.get()
            defeito = et_defeito.get()
            gen = '''
        <html>
        <head>
            <title>Equipamento: "{}"</title>
            <meta charset="UTF-8"/>
        </head>
        <body>
            <h1>{}</h1>
            <h1>Equipamento: {}</h1>
            <h2>Modelo: {}</h2>
            <h2>Cor: {}</h2>
            <h2>Numero de Serie: {}</h2>
            <h2>Acessorios: {}</h2>
            <h2>Defeito: {}</h2>
            <h1>QRCODE</h1>
            <img src="QR_LIST/{}{}.png">
        </body>
        </html>
        '''.format(equipamento, data, equipamento, modelo, cor, ns, acessorios, defeito, equipamento, modelo)
            os.system('cd /home/haise/Servidor/QR_LIST && qr {}.html >> {}{}.png'.format(link, equipamento, modelo))
            os.system('cd /home/haise/Servidor && echo "{}" >> {}.html'.format(gen, equipamento))

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

        bt_cadastrar.grid(row=6, columnspan=2)

        gui.mainloop()

    def consulta():
        print('OK')

    gui = Tk()
    gui.title('Software for You (S4U) V:0.1 Bem Vindo "{}"!'.format(user))
    lb_user = Label(gui, text='Bem Vindo "{}!"'.format(user))
    lb_time = Label(gui, text='{}'.format(b))
    bt_regs_clt = Button(gui, text='Cadastrar Clientes (F2) ', command=cadastro)
    bt_consult_clt = Button(gui, text='Consultar Clientes (F3)', command=consulta)
    lb_user.grid(row=0, column=0)
    lb_time.grid(row=1, column=0)
    bt_regs_clt.grid(row=2, column=0)
    bt_consult_clt.grid(row=3, column=0)
    gui.geometry('700x450')
    gui.mainloop()
