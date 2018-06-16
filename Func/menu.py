from tkinter import *
import os
import time
gen = '''
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
'''

a = time.localtime()
title = ('Hora: {}:{}\nData: {}/{}/{} '.format(a[3], a[4], a[2], a[1], a[0]))
data = ('Hora: {}:{} Data: {}/{}/{} '.format(a[3], a[4], a[2], a[1], a[0]))


def menu_list(user):


    def cadastro():


        def cadastrar():
            cliente = et_client.get()
            email = et_email.get()
            cel = et_cel.get()
            tel = et_tel.get()
            rua = et_rua.get()
            num = et_num.get()
            cep = et_cep.get()
            if cliente == '':
                lb_rest['text'] = 'Obrigatorio Preencher o *Cliente*'
                lb_rest['fg'] = 'red'
            else:
                if cel == '':
                    cel = 'Nao Cadastrado!'
                    if tel == '':
                        tel = 'Nao Cadastrado!'
                        if email == '':
                            email = 'Nao Cadastrado!'
                            if rua == '':
                                rua = 'Nao Cadastrado!'
                                if num == '':
                                    num = 'Nao Cadastrado!'
                                    if cep == '':
                                        cep = 'Nao Cadastrado!'
                                        lb_rest['text'] = 'Cadastrado com Sucesso!'
                                        lb_rest['fg'] = 'green'
                                        cl = (cliente, cel, tel, email, rua, num, cep)
                                        equipamento()

        g = Tk()
        g.title('Cadastrar Cliente')
        lb_client = Label(g, text='Nome do Cliente: ')
        lb_email = Label(g, text='E-Mail: ')
        lb_cel = Label(g, text='Celular: ')
        lb_tel = Label(g, text='Telefone: ')
        lb_rua = Label(g, text='Rua: ')
        lb_num = Label(g, text='Numero: ')
        lb_cep = Label(g, text='Cep: ')
        et_client = Entry(g)
        et_email = Entry(g)
        et_cel = Entry(g)
        et_tel = Entry(g)
        et_rua = Entry(g)
        et_num = Entry(g)
        et_cep = Entry(g)
        lb_rest = Label(g, text='')
        bt_register = Button(g, text='Cadastrar Equipamento', command=cadastrar)
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
        lb_rest.grid(row=7, columnspan=2)
        bt_register.grid(row=8, columnspan=2)
        g.mainloop()

    def equipamento():
        def cad_eqp():
            link = 'localhost'
            equipamento = et_equipamento.get()
            modelo = et_modelo.get()
            cor = et_cor.get()
            ns = et_ns.get()
            acessorios = et_acessorios.get()
            defeito = et_defeito.get()
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
                                    gen.format(equipamento, data, equipamento, modelo, cor, ns, acessorios, defeito,
                                               equipamento, modelo)
                                    os.system('cd /home/haise/Servidor/os/QR_LIST && qr {}.html >> {}{}.png'.format(link, equipamento, modelo))
                                    os.system('cd /home/haise/Servidor/os && echo "{}" >> {}.html'.format(gen, equipamento))

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

    def consulta():
        pass

    def os():
        pass

    gui = Tk()
    gui.title('Software for You (S4U) V:0.1 Bem Vindo "{}"!'.format(user))
    lb_user = Label(gui, text='Bem Vindo "{}!"'.format(user))
    lb_time = Label(gui, text='{}'.format(title))
    bt_regs_clt = Button(gui, text='Cadastrar Clientes (F2) ', command=cadastro)
    bt_consult_clt = Button(gui, text='Consultar Clientes (F3)', command=consulta)
    lb_user.grid(row=0, column=0)
    lb_time.grid(row=1, column=0)
    bt_regs_clt.grid(row=2, column=0)
    bt_consult_clt.grid(row=3, column=0)
    gui.geometry('700x450')
    gui.mainloop()
menu_list('rick')
