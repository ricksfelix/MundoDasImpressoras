from tkinter import *
from programs import bin
import sqlite3
import time

config = bin.credits()
a = time.localtime()
date_time = ('Hora: {}:{}\nData: {}/{}/{} '.format(a[3], a[4], a[2], a[1], a[0]))

con = sqlite3.connect('database.db')
c = con.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS Funcionario(user VarChar, passw VarChar, cargo VarChar)
""")


def logon():
    def menu(user):
        gui = Tk()
        gui.title('Software for You (S4U) V:0.1 Bem Vindo "{}"!'.format(user))
        title = LabelFrame(gui, text='Bem vindo "{}"'.format(user))
        cad = LabelFrame(gui, text='Opções de Cadastro')
        #lb_user = Label(title, text='Bem Vindo "{}!"'.format(user))
        lb_time = Label(title, text='{}'.format(date_time))
        bt_regs_clt = Button(cad, text='Cadastrar Clientes (F2) ', command=bin.cadastro)
        bt_regs_eqp = Button(cad, text='Cadastrar Equipamentos (F5) ', command=bin.equipamentos)
        bt_consult_clt = Button(cad, text='Consultar Clientes (F3)', command=bin.consulta)
        bt_edit_clt = Button(cad, text='Editar Dados (F12)', command=bin.edit)
        bt_config = Button(cad, text='Configuração', command=bin.config)
        title.grid(row=0, column=0, sticky=E+W)
        if cargo == 'admin':
            bt_edit_func = Button(cad, text='Editar Permissões de Login')
            bt_edit_func.grid(row=6, column=0)
        cad.grid(row=1, column=0)
        lb_user.grid(row=0, column=0)
        lb_time.grid(row=1, column=0)
        bt_regs_clt.grid(row=2, column=0)
        bt_regs_eqp.grid(row=3, column=0)
        bt_consult_clt.grid(row=4, column=0)
        bt_edit_clt.grid(row=5, column=0)
        bt_config.grid(row=7, column=0)
        gui.geometry('700x450')
        gui.mainloop()

    def register():
        user = et_user.get()
        passw = et_passw.get()
        if (user, passw) == ('', ''):
            lb_result['text'] = 'Preencha os Campos'
            lb_result['fg'] = 'red'

    def login():
        global cargo
        user = et_user.get()
        passw = et_passw.get()
        sql = 'SELECT * FROM Funcionario WHERE cargo = ?'
        print(c.execute(sql, (et_user.get())))
        for auth in c.execute(sql, (et_user.get())):
            print(auth)
            user1 = auth[0]
            passw1 = auth[1]
            cargo = auth[2]
        print(user1, passw1)
        if (user, passw) == ('', ''):
            lb_result['text'] = 'Preencha os Campos'
            lb_result['fg'] = 'red'
        else:
            if (user, passw) == (user1, passw1):
                lb_result['text'] = 'Logado'
                lb_result['fg'] = 'green'
                et_user.delete(0, END)
                et_passw.delete(0, END)
                menu(user)
            else:
                lb_result['text'] = 'Usuario ou Senha errados!'
                lb_result['fg'] = 'red'

    log_menu = Tk()
    gui = LabelFrame(log_menu, text='Login')
    lb_user = Label(gui, text='User: ')
    lb_passw = Label(gui, text='Passw: ')
    lb_result = Label(gui, text='')
    et_user = Entry(gui)
    et_passw = Entry(gui, show='*')
    bt_confirm = Button(gui, text='Login', command=login)
    bt_register = Button(gui, text='Cadastrar', command=register)
    lb_credits = Label(gui, text='S4U® Designed for:\n {}'.format(config[0]), fg='white', bg='silver')
    gui.grid(row=0, column=0)
    lb_user.grid(row=0, column=0)
    lb_passw.grid(row=1, column=0)
    et_user.grid(row=0, column=1)
    et_passw.grid(row=1, column=1)
    lb_result.grid(row=2, columnspan=3)
    bt_confirm.grid(row=3, columnspan=2)
    bt_register.grid(row=4, columnspan=2)
    lb_credits.grid(row=5, columnspan=2, sticky=W+E)

    log_menu.title('Login...')
    log_menu.mainloop()


logon()
