from tkinter import *
from tkinter import ttk
import sqlite3
con = sqlite3.connect('database.db')
c = con.cursor()
c.execute('CREATE TABLE IF NOT EXISTS Cliente(name text, tipo text, cel text, tel text, email text, ender text, '
          'num text)')
c.execute('CREATE TABLE IF NOT EXISTS Equipamentos(user text,date text,equipamento text,modelo text,cor text,ns text,'
          'acessorios text,defeito text,os text'
          ')')
c.execute('CREATE TABLE IF NOT EXISTS Configs(logo VarChat)')

def edit():
    gui = Tk()
    Label(gui, text='EM DESENVOLVIMENTO').pack()
    gui.title("EM DESENVOLVIMENTO")
    gui.mainloop()

def equipamentos():

    gui = Tk()
    gui.title("EM DESENVOLVIMENTO")
    fm_equipamento = LabelFrame(gui, text='Equipamento')    
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

    # Declarando Posição de Widgets de Equipamento

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

def config():
    def creditos():
        edit = et_credits.get()
        if et_credits.get() == '':
            lb_result['text'] = 'Preencha o Campo!'
            lb_result['fg'] = 'red'
        else:
            c.execute("""
            UPDATE Configs SET logo = ?;
            """, edit)
            con.commit()
            lb_result['text'] = 'Alterado Com Sucesso!'
            lb_result['fg'] = 'green'
    gui = Tk()
    gui.title('Config')
    lb_credits = Label(gui, text='Creditos:')
    et_credits = Entry(gui)
    bt_confirm = Button(gui, text='Confirmar', command=creditos)
    lb_result = Label(gui, text='')
    c.execute("""
    SELECT * FROM Configs;
    """)
    for credits in c.fetchall():
        et_credits.insert(0, credits[0])
    lb_credits.grid(row=0, column=0)
    et_credits.grid(row=0, column=1)
    lb_result.grid(row=1, columnspan=2)
    bt_confirm.grid(row=2, columnspan=2)
    gui.mainloop()


def credits():
    c.execute("""
    SELECT * FROM Configs;
    """)
    for cnf in c.fetchall():
        return cnf

def cadastro():
    gui = Tk()
    gui.title('EM DESENVOLVIMENTO')

    fm_cliente = LabelFrame(gui, text='Cliente')
    fm_equipamento = LabelFrame(gui, text='Equipamento')

    # Declarando Widgets de Cadastro de Clientes

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
    # Demarcando Posições dos Widgets Clientes

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

    # Declarando Widget De Cadastro de Equipamento

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

    # Declarando Posição de Widgets de Equipamento

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


def consulta():
    c = Tk()
    consult = Listbox(c)
    consult.insert(0, 'Hu3hu3hu3')
    c.execute("""
    SELECT * FROM Equipamentos;
    """)
    for result in c.fetchall():
        print(result)
    consult.insert(0, 'teste{}'.format(result))
    consult.grid(row=0, column=0)
    c.mainloop()

def login(user,passw):
    pass
