n1 = int(input('1º Numero >>> '))
n2 = int(input('2º Numero >>> '))
cont = 0
while cont < n2:
    n3 = n1*n2
    print(n3)
print(n3)


"""
import os
from tkinter import *
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
"""