import tkinter as tk
from tkinter import messagebox
import pickle
import os.path
import datetime
class NFe:
    def __init__(self, numero, data, cliente, listaProd, valorTotal, conteudoNota):
        self.__numero = numero
        self.__cliente = cliente
        self.__data = data
        self.__listaProd = listaProd
        self.__valorTotal = valorTotal
        self.__conteudoNota = conteudoNota

    @property
    def numero(self):
        return self.__numero
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def data(self):
        return self.__data
    
    
    @property
    def listaProd(self):
        return self.__listaProd

    @property
    def valorTotal(self):
        return self.__valorTotal
    
    @property
    def conteudoNota(self):
        return self.__conteudoNota

class LimiteEmiteNFe(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("600x550")
        self.title("Emissão NFe")

        self.frameCPF = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCPF.pack()
        self.frameBotao.pack()

        self.labelCpf = tk.Label(self.frameCPF, text="CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCPF, width=20)
        self.inputCpf.pack(side="left")

        self.labelData = tk.Label(self.frameCPF, text="Data(dd/mm/aaaa): ")
        self.labelData.pack(side="left")
        self.inputData = tk.Entry(self.frameCPF, width=20)
        self.inputData.pack(side="left")

        self.botaoConsultar = tk.Button(self.frameBotao, text="Adicionar cliente")
        self.botaoConsultar.pack(side="left")
        self.botaoConsultar.bind("<Button>", controle.enterCPF)

        self.frameProduto = tk.Frame(self)
        self.frameProduto.pack()

        self.labelCodigo = tk.Label(self.frameProduto, text="Código: ")
        self.labelCodigo.grid(row=0, column=0, padx=5, pady=5)
        self.labelPeso = tk.Label(self.frameProduto, text="Peso em KG: ")
        self.labelPeso.grid(row=0, column=1, padx=5, pady=5)

        self.inputCodigo = tk.Entry(self.frameProduto, width=20)
        self.inputCodigo.grid(row=1, column=0, padx=5, pady=5)
        self.inputPeso = tk.Entry(self.frameProduto, width=20)
        self.inputPeso.grid(row=1, column=1, padx=5, pady=5)

        self.frameBotaoProd = tk.Frame(self)
        self.frameBotaoProd.pack()
        self.botaoProduto = tk.Button(self.frameBotaoProd, text="Adicionar produto")
        self.botaoProduto.pack(side="left")
        self.botaoProduto.bind("<Button>", controle.enterProduto)

        self.botaoEmitir = tk.Button(self.frameBotaoProd, text='Emitir NFe')
        self.botaoEmitir.pack(side="left")
        self.botaoEmitir.bind("<Button>", controle.enterEmitir)
        self.botaoCancela = tk.Button(self.frameBotaoProd, text='Cancelar NFe')
        self.botaoCancela.pack(side="left")
        self.botaoCancela.bind("<Button>", controle.enterCancelaNota)
        self.frameText = tk.Frame(self)
        self.frameText.pack()
        self.textNota = tk.Text(self.frameText, height=70, width=70)
        self.textNota.pack()
        self.textNota.config(state=tk.DISABLED)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaNF(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("200x150")
        self.title("Consulta NFe")

        self.frameNota = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameNota.pack()
        self.frameBotao.pack()

        self.labelNota = tk.Label(self.frameNota, text="Número NFe: ")
        self.labelNota.pack(side="left")

        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side='left')

        self.botaoConsulta = tk.Button(self.frameBotao, text="Consultar")
        self.botaoConsulta.pack(side="left")
        self.botaoConsulta.bind("<Button>", controle.enterConsultaNF)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteBuscaPeriodo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("200x150")
        self.title("Busca Período")

        self.frameDataInicio = tk.Frame(self)
        self.frameDataFim = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameDataInicio.pack()
        self.frameDataFim.pack()
        self.frameBotao.pack()

        self.labelDataInicio = tk.Label(self.frameDataInicio, text="Insira a data inicial: ")
        self.labelDataInicio.pack(side="left")
        self.inputDataInicio = tk.Entry(self.frameDataInicio, width=20)
        self.inputDataInicio.pack(side="left")

        self.labelDataFim = tk.Label(self.frameDataFim, text="Insira a data limite: ")
        self.labelDataFim.pack(side="left")
        self.inputDataFim = tk.Entry(self.frameDataFim, width=20)
        self.inputDataFim.pack(side="left")

        self.botaoConsulta = tk.Button(self.frameBotao, text="Enter")
        self.botaoConsulta.pack(side="left")
        self.botaoConsulta.bind("<Button>", controle.enterPeriodo)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaFaturamentoCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("200x150")
        self.title("Busca Período")

        
        self.frameCPF = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCPF.pack()
        self.frameBotao.pack()

        self.labelCpf = tk.Label(self.frameCPF, text="CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCPF, width=20)
        self.inputCpf.pack(side="left")

        self.botaoConsulta = tk.Button(self.frameBotao, text="Enter")
        self.botaoConsulta.pack(side="left")
        self.botaoConsulta.bind("<Button>", controle.enterConsultaFaturamentoCPF)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteBuscaPeriodoCliente(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("400x200")
        self.title("Busca Período")

        self.frameCPF = tk.Frame(self)
        self.frameDataInicio = tk.Frame(self)
        self.frameDataFim = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCPF.pack()
        self.frameDataInicio.pack()
        self.frameDataFim.pack()
        self.frameBotao.pack()

        self.labelCpf = tk.Label(self.frameCPF, text="CPF: ")
        self.labelCpf.pack(side="left")
        self.inputCpf = tk.Entry(self.frameCPF, width=20)
        self.inputCpf.pack(side="left")
        self.labelDataInicio = tk.Label(self.frameDataInicio, text="Insira a data inicial: ")
        self.labelDataInicio.pack(side="left")
        self.inputDataInicio = tk.Entry(self.frameDataInicio, width=20)
        self.inputDataInicio.pack(side="left")

        self.labelDataFim = tk.Label(self.frameDataFim, text="Insira a data limite: ")
        self.labelDataFim.pack(side="left")
        self.inputDataFim = tk.Entry(self.frameDataFim, width=20)
        self.inputDataFim.pack(side="left")

        self.botaoConsulta = tk.Button(self.frameBotao, text="Enter")
        self.botaoConsulta.pack(side="left")
        self.botaoConsulta.bind("<Button>", controle.enterBuscaPeriodoCliente)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlNotas():
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        self.controleProduto = controlePrincipal.ctrlProduto
        self.controleCliente = controlePrincipal.ctrlCliente
        self.count = 1
        self.total = 0
        self.cliente = None
        self.data = ''
        self.valores = []
        self.pesos = []
        if not os.path.isfile("notas.pickle"):
            self.listaNotas = []
        else:
            with open("notas.pickle", "rb") as f:
                self.listaNotas = pickle.load(f)

    def salvaNotas(self):
        if len(self.listaNotas) != 0:
            with open("notas.pickle", "wb") as f:
                pickle.dump(self.listaNotas, f)

    def emiteNF(self):
        self.limEmiteNF = LimiteEmiteNFe(self)

    def enterCPF(self, event):
        cpf = self.limEmiteNF.inputCpf.get()
        self.data = self.limEmiteNF.inputData.get()
        for cliente in self.controleCliente.listaCliente:
            if cpf == cliente.cpf:
                self.limEmiteNF.textNota.config(state="normal")
                self.limEmiteNF.textNota.delete(1.0, tk.END)  # Limpa o texto atual
                self.limEmiteNF.textNota.insert(tk.END, f"\t\t\t  Nota Fiscal\n\nData de emissão: {self.data}\n\n")
                self.limEmiteNF.textNota.insert(tk.END, f"CPF: {cpf: <35} Nome: {cliente.nome}\nNota nº: {len(self.listaNotas)+1}\n\n")
                self.limEmiteNF.textNota.config(state='disable')
                self.cliente = cliente
                return
        self.limCadCpf = self.controleCliente.cadastraCliente()
    
    def enterProduto(self, event):
        codigo = self.limEmiteNF.inputCodigo.get()
        peso = self.limEmiteNF.inputPeso.get()
        self.listaProdutosSelecionados = []
        for prod in self.controleProduto.listaProdutos:
            if codigo == prod.codigo:
                if self.count <= 10:
                    valor = float(peso) * float(prod.preco)
                    self.limEmiteNF.textNota.config(state="normal")
                    self.limEmiteNF.textNota.insert(tk.END, "Descrição: {: <20}Valor: {:.2f}\n".format(prod.descricao, valor))
                    self.limEmiteNF.textNota.config(state='disable')
                    self.listaProdutosSelecionados.append(prod)
                    self.count+=1
                    self.total += valor
                    self.valores.append(valor)
                    self.pesos.append(float(peso))
                    return
                else:
                    self.limEmiteNF.mostraJanela("Erro", "Limite de produtos atingido")
        self.limEmiteNF.mostraJanela("Erro", "Produto não cadastrado")
                
    def enterEmitir(self, event):
        self.limEmiteNF.textNota.config(state="normal")
        self.limEmiteNF.textNota.insert(tk.END, "\nValor total: {:.2f}".format(self.total))
        self.limEmiteNF.textNota.config(state='disabled')
        nota = NFe(len(self.listaNotas)+1, self.data, self.cliente, self.listaProdutosSelecionados, self.total, self.limEmiteNF.textNota.get("1.0", 'end-1c'))
        self.listaNotas.append(nota)
        for prod in self.controleProduto.listaProdutos:
                    for i, prodSel in enumerate(self.listaProdutosSelecionados):
                        if prodSel.codigo == prod.codigo:
                            self.controleProduto.alteraFaturamentoProduto(prodSel.codigo, self.valores[i], self.pesos[i])       
        self.total = 0
        self.count = 0
        self.data = ''
        self.cliente = None
        self.valores = []
        self.pesos = []
        self.limEmiteNF.mostraJanela("Sucesso", "NFe cadastrada com sucesso!")
        self.limEmiteNF.textNota.config(state="normal")
        self.limEmiteNF.textNota.delete(1.0, tk.END)
        self.limEmiteNF.textNota.config(state='disabled')
        self.limpaEmitir(event)

    def enterCancelaNota(self, event):
        self.total = 0
        self.count = 0
        self.data = ''
        self.cliente = None
        self.valores = []
        self.pesos = []
        self.limEmiteNF.mostraJanela("Sucesso", "NFe cancelada com sucesso!")
        self.limEmiteNF.textNota.config(state="normal")
        self.limEmiteNF.textNota.delete(1.0, tk.END)
        self.limEmiteNF.textNota.config(state='disabled')
        self.limpaEmitir(event)

    def limpaEmitir(self, event):
        self.limEmiteNF.inputCodigo.delete(0, len(self.limEmiteNF.inputCodigo.get()))
        self.limEmiteNF.inputCpf.delete(0, len(self.limEmiteNF.inputCpf.get()))
        self.limEmiteNF.inputPeso.delete(0, len(self.limEmiteNF.inputPeso.get()))
        self.limEmiteNF.inputData.delete(0, len(self.limEmiteNF.inputData.get()))

    def consultaNF(self):
        self.limConsultaNFe = LimiteConsultaNF(self)

    def enterConsultaNF(self, event):
        numero = self.limConsultaNFe.inputNota.get()
        for nf in self.listaNotas:
            if int(nf.numero) == int(numero):
                self.limConsultaNFe.mostraJanela("NFe encontrada", nf.conteudoNota)
                self.limpaConsultaNF(event)
                return
        self.limConsultaNFe.mostraJanela("Erro", "NFe não encontrada")
        self.limpaConsultaNF(event)

    def limpaConsultaNF(self, event):
        self.limConsultaNFe.inputNota.delete(0, len(self.limConsultaNFe.inputNota.get()))
    
    def exibeFaturamento(self):
        self.limBuscaPeriodo= LimiteBuscaPeriodo(self)

    def enterPeriodo(self, event):
        # Converter a string para um objeto de data
        data_Fim = datetime.datetime.strptime(self.limBuscaPeriodo.inputDataFim.get(), "%d/%m/%Y").date()
        data_Inicio = datetime.datetime.strptime(self.limBuscaPeriodo.inputDataInicio.get(), "%d/%m/%Y").date()
        faturamento = 0
        ok = 1
        for nota in self.listaNotas:
            data = datetime.datetime.strptime(nota.data, "%d/%m/%Y").date()
            if data <= data_Fim and data >= data_Inicio:
                faturamento += nota.valorTotal
                ok = 0
        if ok == 0:
            self.limBuscaPeriodo.mostraJanela("Faturamento", f"Faturamento do período:\nR${faturamento}")
            self.limpaPeriodo(event)
        else:
            self.limBuscaPeriodo.mostraJanela("Erro", f"Não houve faturamento do período!!")
            self.limpaPeriodo(event)

    def limpaPeriodo(self, event):
        self.limBuscaPeriodo.inputDataFim.delete(0, len(self.limBuscaPeriodo.inputDataFim.get()))
        self.limBuscaPeriodo.inputDataInicio.delete(0, len(self.limBuscaPeriodo.inputDataInicio.get()))

    def consultaFaturamentoCPF(self):
        self.limConsFaturamentoCliente = LimiteConsultaFaturamentoCliente(self)
    
    def enterConsultaFaturamentoCPF(self, event):
        cpf = self.limConsFaturamentoCliente.inputCpf.get()
        faturamento = 0
        ok = 0
        for cliente in self.controleCliente.listaCliente:
            if cpf == cliente.cpf:
                ok = 1
                nome = cliente.nome
                for nota in self.listaNotas:
                    if nota.cliente.cpf == cpf:
                        faturamento += nota.valorTotal
        if ok == 1:
            self.limConsFaturamentoCliente.mostraJanela("Faturamento Total Cliente", f'Faturamento total do cliente:{nome}\nR$ {faturamento}')
            self.limpaCpfFaturamento(event)
        else:
            self.limConsFaturamentoCliente.mostraJanela("Faturamento Total Cliente",'Cliente não encontrado!!')
            self.limpaCpfFaturamento(event)

    def limpaCpfFaturamento(self, event):
        self.limConsFaturamentoCliente.inputCpf.delete(0, len(self.limConsFaturamentoCliente.inputCpf.get()))
    
    
    def consultaVendasPeriodoCliente(self):
        self.limBuscaPeriodoCliente = LimiteBuscaPeriodoCliente(self)

    def enterBuscaPeriodoCliente(self, event):
        # Converter a string para um objeto de data
        cpf = self.limBuscaPeriodoCliente.inputCpf.get()
        data_Fim = datetime.datetime.strptime(self.limBuscaPeriodoCliente.inputDataFim.get(), "%d/%m/%Y").date()
        data_Inicio = datetime.datetime.strptime(self.limBuscaPeriodoCliente.inputDataInicio.get(), "%d/%m/%Y").date()
        faturamento = 0
        ok = 1
        stringVendas = f'Vendas feitas ao cliente no período {data_Inicio} - {data_Fim} :\n'
        for nota in self.listaNotas:
            data = datetime.datetime.strptime(nota.data, "%d/%m/%Y").date()
            cpfCliente = nota.cliente.cpf
            if cpf == cpfCliente:
                ok = 0
                if data <= data_Fim and data >= data_Inicio:
                    stringVendas += f'nº Nota: {nota.numero} Valor Nota: R$ {nota.valorTotal}\n'
                    
        if ok == 0:
            self.limBuscaPeriodoCliente.mostraJanela("Faturamento Cliente Período", stringVendas)
            self.limpaPeriodoCliente(event)
        else:
            self.limBuscaPeriodoCliente.mostraJanela("Erro", f"Cliente não encontrado!!")
            self.limpaPeriodoCliente(event)

    def limpaPeriodoCliente(self, event):
        self.limBuscaPeriodoCliente.inputCpf.delete(0, len(self.limBuscaPeriodoCliente.inputCpf.get()))
        self.limBuscaPeriodoCliente.inputDataFim.delete(0, len(self.limBuscaPeriodoCliente.inputDataFim.get()))
        self.limBuscaPeriodoCliente.inputDataInicio.delete(0, len(self.limBuscaPeriodoCliente.inputDataInicio.get()))


    