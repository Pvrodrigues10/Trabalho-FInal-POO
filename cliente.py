import tkinter as tk
from tkinter import messagebox
import pickle
import os.path

class Cliente:
    def __init__(self, nome, cpf, email, endereco):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def email(self):
        return self.__email

    @property
    def endereco(self):
        return self.__endereco
    
class LimiteCadastraCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("450x180")
        self.title("Cadastra Cliente")

        self.frameNome = tk.Frame(self)
        self.frameCpf = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameEndereco = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameNome.pack()
        self.frameCpf.pack()
        self.frameEmail.pack()
        self.frameEndereco.pack()
        self.frameBotao.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCpf = tk.Label(self.frameCpf, text="CPF: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelEndereco = tk.Label(self.frameEndereco, text="Endereço: ")
        self.labelNome.pack(side="left")
        self.labelCpf.pack(side="left")
        self.labelEmail.pack(side="left")
        self.labelEndereco.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=60)
        self.inputCpf = tk.Entry(self.frameCpf, width=60)
        self.inputEmail = tk.Entry(self.frameEmail, width=60)
        self.inputEndereco = tk.Entry(self.frameEndereco, width=60)
        self.inputNome.pack(side="left")
        self.inputCpf.pack(side="left")
        self.inputEmail.pack(side="left")
        self.inputEndereco.pack(side="left")

        self.botaoCadastra = tk.Button(self.frameBotao, text="Cadastrar")
        self.botaoCadastra.pack(side="left")
        self.botaoCadastra.bind("<Button>", controle.enterCadastra)

        self.botaoClear = tk.Button(self.frameBotao, text="Limpar")
        self.botaoClear.pack(side="left")
        self.botaoClear.bind("<Button>", controle.limpaCadastro)

        self.botaoFechar = tk.Button(self.frameBotao, text="Fechar")
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", controle.fechaCadastro)       


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("200x180")
        self.title("Consulta Cliente")

        self.frameCpf = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCpf.pack()
        self.frameBotao.pack()

        self.labelCpf = tk.Label(self.frameCpf, text="CPF: ")
        self.labelCpf.pack(side="left")

        self.inputCpf = tk.Entry(self.frameCpf, width=20)
        self.inputCpf.pack(side="left")

        self.botaoConsultar = tk.Button(self.frameBotao, text="Consultar")
        self.botaoConsultar.pack(side="left")
        self.botaoConsultar.bind("<Button>", controle.enterConsulta)        

        self.botaoClear = tk.Button(self.frameBotao, text="Limpar")
        self.botaoClear.pack(side="left")
        self.botaoClear.bind("<Button>", controle.limpaConsulta)

        self.botaoFechar = tk.Button(self.frameBotao, text="Fechar")
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", controle.fechaConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlCliente():
    def __init__(self):
        if not os.path.isfile("cliente.pickle"):
            self.listaCliente = []
        else:
            with open("cliente.pickle", "rb") as f:
                self.listaCliente = pickle.load(f)
    
    def salvaCliente(self):
        if len(self.listaCliente) != 0:
            with open("cliente.pickle", "wb") as f:
                pickle.dump(self.listaCliente, f)


    def cadastraCliente(self):
        self.limCadCliente = LimiteCadastraCliente(self)

    def enterCadastra(self, event):
        nome = self.limCadCliente.inputNome.get()
        cpf = self.limCadCliente.inputCpf.get()
        email = self.limCadCliente.inputEmail.get()
        endereco = self.limCadCliente.inputEndereco.get()

        for cliente in self.listaCliente:
            if cliente.cpf == cpf:
                self.limCadCliente.mostraJanela("Erro", "Cliente já cadastrado")
                return
        
        self.listaCliente.append(Cliente(nome, cpf, email, endereco))
        self.limCadCliente.mostraJanela("Sucesso", "Cliente cadastrado com sucesso")
        self.limpaCadastro(event)
    
    def limpaCadastro(self, event):
        self.limCadCliente.inputNome.delete(0, len(self.limCadCliente.inputNome.get()))
        self.limCadCliente.inputCpf.delete(0, len(self.limCadCliente.inputCpf.get()))
        self.limCadCliente.inputEmail.delete(0, len(self.limCadCliente.inputEmail.get()))
        self.limCadCliente.inputEndereco.delete(0, len(self.limCadCliente.inputEndereco.get()))
    
    def fechaCadastro(self, event):
        self.limCadCliente.destroy()

    def consultaCliente(self):
        self.limConCliente = LimiteConsultaCliente(self)

    def enterConsulta(self, event):
        cpf = self.limConCliente.inputCpf.get()

        for cliente in self.listaCliente:
            if cliente.cpf == cpf:
                self.limConCliente.mostraJanela("Cliente encontrado", f"Nome: {cliente.nome}\nCPF: {cliente.cpf}\nEmail: {cliente.email}\nEndereço: {cliente.endereco} ")
                self.limpaConsulta(event)
                return
        
        self.limConCliente.mostraJanela("Erro", "Cliente não encontrado")
        self.limpaConsulta(event)

    def limpaConsulta(self, event):
        self.limConCliente.inputCpf.delete(0, len(self.limConCliente.inputCpf.get()))

    def fechaConsulta(self, event):
        self.limConCliente.destroy()

    