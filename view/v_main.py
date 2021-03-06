from tkinter import *
from tkinter import ttk
from functools import partial
from view.v_crud import CRUDWindow
from controller.controller_usu import ControllerLogin


class MainWindow:
    def OpenMain(self):
        controller = ControllerLogin()
        window = Tk()

        # - Funções -
        def btn_login():
           resul = controller.verifica(ed1.get(), ed2.get())
           if resul == True:
              telacrud = CRUDWindow()
              window.destroy()
              telacrud.OpenCRUD()

        def btn_cadastra():
            controller = ControllerLogin()
            if ed4.get() == ed5.get():  # senha / confirma senha
                testaUsuario = ControllerLogin()
                verifica = testaUsuario.verifica(ed3.get())  # login
                if verifica == 0:
                    controller.insere(ed3.get(), ed4.get())  # login / senha
                    print("cadastro realizado")
                    ed3.delete(0, END)  # login
                    ed4.delete(0, END)  # senha
                    ed5.delete(0, END)  # confirma senha
                    ed3.focus()  # nome
                else:
                    print("Usuario já existe")
            else:
                print("senhas diferentes")

        # - __TELA__ -
        # Criando as Abas da Main
        abas = ttk.Notebook(window)

        # fonte dos textos
        fonte = ('Arial', '16', 'bold')

        # Colocando a Aba (1) na tela
        aba_login = ttk.Frame(abas)

        # -- Aba Login (1) -- ==========================================================================================
        abas.add(aba_login, text='  LOGIN  ')

        # Logo Pizzaria Top
        img1 = PhotoImage(file="../assets/img/logo.png")
        logo1 = img1.subsample(2, 2)
        label1 = Label(aba_login, image=logo1) ; label1.place(x=0, y=0)

        # Titulo da janela
        lb0 = Label(aba_login, text="LOGIN") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=140)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # Login
        lb1 = Label(aba_login, text="Login: ") ; lb1.grid(row=1, column=1) ; lb1.place(x=10, y=175)
        lb1.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed1 = Entry(aba_login, font=fonte, width=30) ; ed1.grid(row=1, column=2) ; ed1.place(x=10, y=205)

        # Senha
        lb2 = Label(aba_login, text="Senha: ") ; lb2.grid(row=2, column=1) ; lb2.place(x=10, y=235)
        lb2.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed2 = Entry(aba_login, font=fonte, show="*", width=30) ; ed2.grid(row=2, column=2) ; ed2.place(x=10, y=265)

        # Botão Confirmar (1)
        bt1 = Button(aba_login, font=fonte, text="Confirmar", fg="#000000",
                     activebackground="#000000", activeforeground="#FFFFFF", width=20, borderwidth=2, relief="solid")
        bt1.grid(row=3, column=3) ; bt1.place(x=65, y=320)
        bt1["command"] = partial(btn_login)

        # Colocando a Aba (2) na tela
        aba_cadastro = ttk.Frame(abas)

        # -- Aba Cadastro (2) -- =======================================================================================
        abas.add(aba_cadastro, text='  CADASTRO  ')

        # Logo Pizzaria Top
        img2 = PhotoImage(file="../assets/img/logo.png")
        logo2 = img2.subsample(2, 2)
        label2 = Label(aba_cadastro, image=logo2) ; label2.place(x=0, y=0)

        # Titulo da janela
        lb0 = Label(aba_cadastro, text="CADASTRO") ; lb0.grid(row=0, column=0) ; lb0.place(x=0, y=140)
        lb0.configure(font=fonte, foreground="#FFFFFF", background="#000000", width=30)

        # -- FORMULARIO DE CADASTRO --
        # Login
        lb3 = Label(aba_cadastro, text="Login: ") ; lb3.grid(row=1, column=1) ; lb3.place(x=10, y=175)
        lb3.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed3 = Entry(aba_cadastro, font=fonte, width=30) ; ed3.grid(row=2, column=1) ; ed3.place(x=10, y=205)

        # Senha
        lb4 = Label(aba_cadastro, text="Senha: ") ; lb4.grid(row=3, column=1) ; lb4.place(x=10, y=235)
        lb4.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed4 = Entry(aba_cadastro, font=fonte, width=30) ; ed4.grid(row=4, column=1) ; ed4.place(x=10, y=265)

        # Confirmar Senha
        lb5 = Label(aba_cadastro, text="Confirmar Senha: ") ; lb5.grid(row=5, column=1) ; lb5.place(x=10, y=295)
        lb5.configure(font=fonte, foreground="#000000", background="#CCCCCC")
        ed5 = Entry(aba_cadastro, font=fonte, show="*", width=30) ; ed5.grid(row=6, column=1) ; ed5.place(x=10, y=325)

        # Botão Cadastrar (2)
        bt2 = Button(aba_cadastro, font=fonte, text="Cadastrar", fg="#000000",
                     activebackground="#000000", activeforeground="#FFFFFF", width=20, borderwidth=2, relief="solid")
        bt2.grid(row=9, column=1) ; bt2.place(x=65, y=370)
        bt2["command"] = partial(btn_cadastra)

        # Exibe o notebook na tela usando pack e configura para redimencionar com a janela
        abas.pack(expand=1, fill='both')

        # __ CONFIGURAÇÕES DA TELA __
        window.geometry("390x480+450+100")  # largura * altura + x + y
        window.resizable(width=False, height=False)
        window.iconbitmap("../assets/img/icone.ico")  # icone do cabeçalho da janela
        window.title(" Pizzaria Top - Main ")  # texto do cabeçalho da janela
        window.mainloop()


Main = MainWindow()
Main.OpenMain()
