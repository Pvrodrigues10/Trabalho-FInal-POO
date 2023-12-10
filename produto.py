import tkinter as tk
from tkinter import messagebox
import pickle
import os.path

class Produto:
    def __init__(self, codigo, descricao, preco, montanteValor, montantePeso, numVendas):
        self.__codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.montanteValor = montanteValor
        self.montantePeso = montantePeso
        self.numVendas = numVendas

    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def montanteValor(self):
        return self.__montanteValor
    
    @property
    def montantePeso(self):
        return self.__montantePeso
    
    @property
    def numVendas(self):
        return self.__numVendas

    # Setters
    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
    
    @preco.setter
    def preco(self, preco):
        self.__preco = preco
    
    @montanteValor.setter
    def montanteValor(self, montanteValor):
        self.__montanteValor = montanteValor
    
    @montantePeso.setter
    def montantePeso(self, montantePeso):
        self.__montantePeso = montantePeso
    
    @numVendas.setter
    def numVendas(self, numVendas):
        self.__numVendas = numVendas

        

class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("250x200")
        self.title("Cadastra produto")

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.framePreco.pack()
        self.frameBotao.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descrição: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preço: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao.pack(side="left")
        self.inputPreco.pack(side="left")

        self.botaoCadastra = tk.Button(self.frameBotao, text="Cadastrar")
        self.botaoCadastra.pack(side="left")
        self.botaoCadastra.bind("<Button>", controle.enterProduto)

        self.botaoClear = tk.Button(self.frameBotao, text="Limpar")
        self.botaoClear.pack(side="left")
        self.botaoClear.bind("<Button>", controle.limpaProduto)

        self.botaoFechar = tk.Button(self.frameBotao, text="Fechar")
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", controle.fechaProduto)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAlteraProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("250x200")
        self.title("Altera produto")

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.framePreco.pack()
        self.frameBotao.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descrição: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preço: ")
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao.pack(side="left")
        self.inputPreco.pack(side="left")

        self.botaoCadastra = tk.Button(self.frameBotao, text="Alterar")
        self.botaoCadastra.pack(side="left")
        self.botaoCadastra.bind("<Button>", controle.enterAlteraProd)

        self.botaoClear = tk.Button(self.frameBotao, text="Limpar")
        self.botaoClear.pack(side="left")
        self.botaoClear.bind("<Button>", controle.limpaAltera)

        self.botaoFechar = tk.Button(self.frameBotao, text="Fechar")
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", controle.fechaAltera)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteRemoveProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("250x200")
        self.title("Remove produto")

        self.frameCodigo = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameBotao.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.botaoCadastra = tk.Button(self.frameBotao, text="Remover")
        self.botaoCadastra.pack(side="left")
        self.botaoCadastra.bind("<Button>", controle.enterRemoveProd)

        self.botaoClear = tk.Button(self.frameBotao, text="Limpar")
        self.botaoClear.pack(side="left")
        self.botaoClear.bind("<Button>", controle.limpaRemove)

        self.botaoFechar = tk.Button(self.frameBotao, text="Fechar")
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", controle.fechaRemove)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("250x200")
        self.title("Consulta produto")

        self.frameCodigo = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameBotao.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.botaoConsulta = tk.Button(self.frameBotao, text="Consultar")
        self.botaoConsulta.pack(side="left")
        self.botaoConsulta.bind("<Button>", controle.enterConsulta)

        self.botaoClear = tk.Button(self.frameBotao, text="Limpar")
        self.botaoClear.pack(side="left")
        self.botaoClear.bind("<Button>", controle.limpaConsulta)

        self.botaoFechar = tk.Button(self.frameBotao, text="Fechar")
        self.botaoFechar.pack(side="left")
        self.botaoFechar.bind("<Button>", controle.fechaConsulta)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaFaturamentoProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.controle = controle
        self.geometry("250x200")
        self.title("Consulta produto")

        self.frameCodigo = tk.Frame(self)
        self.frameBotao = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameBotao.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.botaoConsulta = tk.Button(self.frameBotao, text="Consultar")
        self.botaoConsulta.pack(side="left")
        self.botaoConsulta.bind("<Button>", controle.enterConsultaFaturamento)


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ControleProduto():
    def __init__(self):
        if not os.path.isfile("produto.pickle"):
            self.listaProdutos = []
        else:
            with open("produto.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)

    def salvaProduto(self):
        if len(self.listaProdutos) != 0:
            with open("produto.pickle", "wb") as f:
                pickle.dump(self.listaProdutos, f)
    
    def cadastraProduto(self):
        self.limCadastraProd = LimiteCadastraProduto(self)

    def enterProduto(self, event):
        codigo = self.limCadastraProd.inputCodigo.get()
        descricao = self.limCadastraProd.inputDescricao.get()
        preco = self.limCadastraProd.inputPreco.get()
        for prod in self.listaProdutos:
            if prod.codigo == codigo:
                self.limCadastraProd.mostraJanela("Erro", "Produto já cadastrado")
                return
            if prod.descricao == descricao:
                self.limCadastraProd.mostraJanela("Erro", "Produto já cadastrado")
                return
        self.listaProdutos.append(Produto(codigo, descricao, preco, 0, 0, 0))
        self.limCadastraProd.mostraJanela("Sucesso!", f"Produto: {codigo} - {descricao} - R$ {preco} cadastrado com sucesso")
        self.limpaProduto(event)

    def limpaProduto(self, event):
        self.limCadastraProd.inputCodigo.delete(0, len(self.limCadastraProd.inputCodigo.get()))
        self.limCadastraProd.inputDescricao.delete(0, len(self.limCadastraProd.inputDescricao.get()))
        self.limCadastraProd.inputPreco.delete(0, len(self.limCadastraProd.inputPreco.get()))
    
    def limpaAltera(self, event):
        self.limAlteraProd.inputCodigo.delete(0, len(self.limAlteraProd.inputCodigo.get()))
        self.limAlteraProd.inputDescricao.delete(0, len(self.limAlteraProd.inputDescricao.get()))
        self.limAlteraProd.inputPreco.delete(0, len(self.limAlteraProd.inputPreco.get()))

    def limpaRemove(self, event):
        self.limRemoveProd.inputCodigo.delete(0, len(self.limRemoveProd.inputCodigo.get()))

    def fechaProduto(self, event):
        self.limCadastraProd.destroy()

    def fechaAltera(self, event):
        self.limAlteraProd.destroy()

    def fechaRemove(self, event): 
        self.limRemoveProd.destroy()


    def alteraProduto(self): 
        self.limAlteraProd = LimiteAlteraProduto(self)

    def enterAlteraProd(self, event): # Método para alterar os dados de Nome e preço de um produto
        codigo = self.limAlteraProd.inputCodigo.get()
        descricao = self.limAlteraProd.inputDescricao.get()
        preco = self.limAlteraProd.inputPreco.get()
        
        for prod in self.listaProdutos:
            if prod.codigo == codigo:
                prod.descricao = descricao
                prod.preco = preco
                self.limAlteraProd.mostraJanela("Sucesso!!", f"Produto {codigo} alterado com sucesso")
                self.limpaAltera(event)
                return

        self.limAlteraProd.mostraJanela("Erro", f"Produto {codigo} não encontrado")
        self.limpaAltera(event)

    def removeProduto(self): # metódo que "chama" a classe de remover produto
        self.limRemoveProd = LimiteRemoveProduto(self)

    def enterRemoveProd(self, event): # Método para remover um produto a partir do código
        codigo = self.limRemoveProd.inputCodigo.get()

        for prod in self.listaProdutos:
            if prod.codigo == codigo:
                self.limRemoveProd.mostraJanela("Sucesso!!", f"Produto: {prod.codigo} - {prod.descricao} - R$ {prod.preco} removido")
                self.listaProdutos.remove(prod)
                self.limpaRemove(event)
                return
        self.limRemoveProd.mostraJanela("Erro", f"Produto {codigo} não encontrado")
        self.limpaRemove(event)

    def consultaPoduto(self):
        self.limConsultaProduto = LimiteConsultaProduto(self)

    def consultaFaturamentoProduto(self):
        self.limConsultaFaturamentoProduto = LimiteConsultaFaturamentoProduto(self)

    def enterConsultaFaturamento(self, event):
        codigo = self.limConsultaFaturamentoProduto.inputCodigo.get()

        for prod in self.listaProdutos:
            if prod.codigo == codigo:
                self.limConsultaFaturamentoProduto.mostraJanela("Faturamento Produto", f"Faturamento {prod.descricao}\nR$ {prod.montanteValor}")
                self.limConsultaFaturamentoProduto.inputCodigo.delete(0, len(self.limConsultaFaturamentoProduto.inputCodigo.get()))
                return
        
        self.limConsultaProduto.mostraJanela("Erro", "Produto não encontrado")
        self.limConsultaFaturamentoProduto.inputCodigo.delete(0, len(self.limConsultaFaturamentoProduto.inputCodigo.get()))
    

    def enterConsulta(self, event):
        codigo = self.limConsultaProduto.inputCodigo.get()

        for prod in self.listaProdutos:
            if prod.codigo == codigo:
                self.limConsultaProduto.mostraJanela("Sucesso!!", f"Produto: {prod.codigo} - {prod.descricao} - R${prod.preco}")
                self.limpaConsulta(event)
                return
        
        self.limConsultaProduto.mostraJanela("Erro", "Produto não encontrado")
        self.limpaConsulta(event)

    
    def limpaConsulta(self, event):
        self.limConsultaProduto.inputCodigo.delete(0, len(self.limConsultaProduto.inputCodigo.get()))

    def fechaConsulta(self, event):
        self.limConsultaProduto.destroy()

    def alteraFaturamentoProduto(self, codigoProduto, valor, peso):
        for prod in self.listaProdutos:
            if codigoProduto == prod.codigo:
                prod.montanteValor += valor
                prod.montantePeso += peso
                prod.numVendas += 1
    
    def maisVendidos(self):
        produtos_ordenados = sorted(self.listaProdutos, key=lambda prod: prod.numVendas, reverse=True)
        mensagem = ''
        if len(produtos_ordenados) >= 5:
            for i in range(5):
                mensagem += f"{i+1}.     Código: {produtos_ordenados[i].codigo} -- Descrição: {produtos_ordenados[i].descricao}\nPreço por KG: R${produtos_ordenados[i].preco}\nTotal vendido em KG: {produtos_ordenados[i].montantePeso} -- Total em R$: {produtos_ordenados[i].montanteValor}\nNúmero de vendas: {produtos_ordenados[i].numVendas}\n ------------------------\n"
            messagebox.showinfo("Produtos mais vendidos", mensagem)
        else:
            messagebox.showinfo("Produtos mais vendidos", "Ainda não há produtos suficientes para listar os mais vendidos.")

