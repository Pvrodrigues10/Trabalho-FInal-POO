import tkinter as tk
from tkinter import messagebox
import produto
import cliente
import notas

class LimitePrincipal():
    def __init__(self, raiz, controle):
        self.raiz = raiz
        self.raiz.geometry("350x250")
        self.raiz.title("Sistema Açougue")
        self.controle = controle

        self.menuBar = tk.Menu(self.raiz)
        self.menuProduto = tk.Menu(self.menuBar)
        self.menuVendas = tk.Menu(self.menuBar)
        self.menuClientes = tk.Menu(self.menuBar)
        self.menuSair = tk.Menu(self.menuBar)

        self.menuProduto.add_command(label="Cadastrar produto", command=self.controle.CadastraProduto)
        self.menuProduto.add_command(label="Alterar produto", command=self.controle.alterarProduto)
        self.menuProduto.add_command(label="Remover produto", command=self.controle.removeProduto)
        self.menuProduto.add_command(label="Consultar Produto", command=self.controle.consultaProduto)
        self.menuBar.add_cascade(label="Produto", menu=self.menuProduto)

        self.menuVendas.add_command(label="Emitir NFe", command=self.controle.emiteNF)
        self.menuVendas.add_command(label="Consultar faturamento por período", command=self.controle.consultaPeriodo)
        self.menuVendas.add_command(label="Consultar Nfe", command=self.controle.consultarNF)
        self.menuVendas.add_command(label="Consultar Faturamento Cliente", command=self.controle.consultaFaturamentoCliente)
        self.menuVendas.add_command(label="Consultar Vendas p/ Cliente Período", command=self.controle.consultaVendasClientePeriodo)
        self.menuVendas.add_command(label="Produtos mais vendidos", command=self.controle.consultaMelhores)
        self.menuVendas.add_command(label="Consultar Faturamento Produto", command=self.controle.consultaFaturametoProduto)
        self.menuBar.add_cascade(label="Vendas", menu=self.menuVendas)

        self.menuClientes.add_command(label="Cadastrar cliente", command=self.controle.cadastraCliente)
        self.menuClientes.add_command(label="Consultar cliente", command=self.controle.consultaCliente)
        self.menuBar.add_cascade(label="Cliente", menu=self.menuClientes)

        self.menuSair.add_command(label="Salvar", command=self.controle.salvar)
        self.menuBar.add_cascade(label="Sair", menu=self.menuSair)

        self.raiz.config(menu=self.menuBar)

class ControlePrincipal():
    def __init__(self):
        self.raiz = tk.Tk()

        self.limite = LimitePrincipal(self.raiz, self)
        self.ctrlProduto = produto.ControleProduto()
        self.ctrlCliente = cliente.CtrlCliente()
        self.ctrlNotas = notas.CtrlNotas(self)

        self.raiz.mainloop()

    def CadastraProduto(self):
        self.ctrlProduto.cadastraProduto()
    
    def salvar(self):
        self.ctrlProduto.salvaProduto()
        self.ctrlCliente.salvaCliente()
        self.ctrlNotas.salvaNotas()
        self.raiz.destroy()
    
    def consultaMelhores(self):
        self.ctrlProduto.maisVendidos()
        
    def consultaPeriodo(self):
        self.ctrlNotas.exibeFaturamento()

    def consultaFaturamentoCliente(self):
        self.ctrlNotas.consultaFaturamentoCPF()
    
    def alterarProduto(self):
        self.ctrlProduto.alteraProduto()
    
    def removeProduto(self):
        self.ctrlProduto.removeProduto()
    
    def consultaProduto(self):
        self.ctrlProduto.consultaPoduto()

    def cadastraCliente(self):
        self.ctrlCliente.cadastraCliente()
    
    def consultaCliente(self):
        self.ctrlCliente.consultaCliente()
    
    def emiteNF(self):
        self.ctrlNotas.emiteNF()
    
    def consultarNF(self):
        self.ctrlNotas.consultaNF()

    def consultaVendasClientePeriodo(self):
        self.ctrlNotas.consultaVendasPeriodoCliente()
    
    def consultaFaturametoProduto(self):
        self.ctrlProduto.consultaFaturamentoProduto()
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

if __name__ == "__main__":
    c = ControlePrincipal()