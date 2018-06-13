from tkinter import *
from Teste import funcao
import time

def menu_list(user):
    gui = Tk()
    gui.title('Menu List')
    lb_user = Label(gui, text='Bem Vindo "{}!"'.format(user))
    lb_time = Label(gui, text='{}'.format(time.asctime()))
    bt_regs_clt = Button(gui, text='Cadastrar Clientes', command=funcao.cadastro)
    lb_user.grid(row=0, column=0)
    lb_time.grid(row=1, column=0)
    bt_regs_clt.grid(row=2, column=0)
    gui.mainloop()
