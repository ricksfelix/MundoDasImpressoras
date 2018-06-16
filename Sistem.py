from tkinter import *
from Func import menu


def register():
    user = et_user.get()
    passw = et_passw.get()
    if (user, passw) == ('', ''):
        lb_result['text'] = 'Preencha os Campos'
        lb_result['fg'] = 'red'


def login():
    user = et_user.get()
    passw = et_passw.get()
    if (user, passw) == ('', ''):
        lb_result['text'] = 'Preencha os Campos'
        lb_result['fg'] = 'red'
    else:
        if (user, passw) == ('rick', '123'):
            lb_result['text'] = 'Logado'
            lb_result['fg'] = 'green'
            et_user.delete(0, END)
            et_passw.delete(0, END)
            menu.menu_list(user)
        else:
            lb_result['text'] = 'Usuario ou Senha errados!'
            lb_result['fg'] = 'red'


gui = Tk()
lb_user = Label(gui, text='User: ')
lb_passw = Label(gui, text='Passw: ')
lb_result = Label(gui, text='')
et_user = Entry(gui)
et_passw = Entry(gui, show='*')
bt_confirm = Button(gui, text='Login', command=login)
bt_register = Button(gui, text='Cadastrar', command=register)
lb_user.grid(row=0, column=0)
lb_passw.grid(row=1, column=0)
et_user.grid(row=0, column=1)
et_passw.grid(row=1, column=1)
lb_result.grid(row=2, columnspan=3)
bt_confirm.grid(row=3, columnspan=2)
bt_register.grid(row=4, columnspan=2)
gui.title('Login...')
gui.mainloop()
