# 4-Modifique o código do programa anterior, da seguinte forma:
# a) Adicione um atributo que represente o código de barras do produto (é um valor
# obrigatório e, portanto, deve ser pedido no construtor;

# b) Sobrescreva o método equals() retornando true se dois produtos possuem o mesmo
# código de barras;

# c) Na classe Loja, implemente um simples procedimento de busca que, dado um
# produto e um vetor de produtos, indique em que posição do vetor se encontra o produto
# especificado ou imprima que o mesmo não foi encontrado;

# d) No método Loja.main(), após a impressão do vetor (feita na questão 2a), escolha um
# dos 5 produtos e crie duas novas instâncias idênticas a ele: uma com o mesmo código
# de barras e outra e outra com o código diferente. Efetue a busca deste produto no vetor
# utilizando as duas instâncias e verifique o resultado. 
# 
# Apresentar diagrama UML 

# Equals()
#def __eq__(self, other):
#   return self.codigo_barras == other.codigo_barras

#def busca_produto(self, codigo_barras_other: str):
#   index = 0
#   for produto in self.banco_de_dados:
#       if produto.codigo_barras == codigo_barras_other:
#           return index
#       index += 1  
#       (procurar o metodo self.banco_de_dados.index(codigo_barras_other))
#    print("Código de barras não encontrado")
#    return None

# livro1 = Livro('001')
# livro1.adicionaDados("ITEM TESTE", 40.0, "AUTOR TESTE")
# self.CadastrarProduto(livro1)

# dvd1 = DVD("002")
# dvd1.adicionaDados("ITEM TESTE 2", 1.99, 90)
# self.CadastrarProduto(dvd1)

class Produto:
    def __init__(self, codigo_barras: str):
        self.codigo_barras: str = codigo_barras
        self.dados_adicionados = False

    def adicionaDados(self, nome: str, preco: float):
        self.nome: str = nome
        self.preco: float = preco
        self.dados_adicionados = True

    def toString(self):
        return f"""Nome: {self.nome}
Preço: {self.preco}
Código de Barras: {self.codigo_barras}\n"""

# Equals()
    def __eq__(self, other):
        return self.codigo_barras == other.codigo_barras

class Livro(Produto):
    def __init__(self, codigo_barras: str):
        super().__init__(codigo_barras)

    def adicionaDados(self, nome: str, preco: float, autor: str):
        super().adicionaDados(nome, preco)
        self.autor:str = autor
        
    def toString(self):
        return super().toString() + f"Autor: {self.autor}\n"

class CD(Produto):
    def __init__(self, codigo_barras: str):
        super().__init__(codigo_barras)

    def adicionaDados(self, nome: str, preco: float, n_faixas: int):
        super().adicionaDados(nome, preco)
        self.n_faixas: int = n_faixas

    def toString(self):
        return super().toString() + f"Número de Faixas: {self.n_faixas}\n"

class DVD(Produto):
    def __init__(self, codigo_barras: str):
        super().__init__(codigo_barras)

    def adicionaDados(self, nome: str, preco: float, duracao: int):
        super().adicionaDados(nome, preco)
        self.duracao: int = duracao

    def toString(self):
        return super().toString() + f"Duração (Minutos): {self.duracao}\n"

class Loja:
    def __init__(self):
        self.banco_de_dados: list = []

    def MostrarProdutosCadastrados(self):
        if len(self.banco_de_dados) == 0:
            print("Banco de Dados Vazio !")
        else:
            print(f"{'----- Menu De Informações -----': <50}")
            for produto in self.banco_de_dados:
                print(produto.toString())
                print(f"{'----- FIM DA FICHA -----': <50}")

    def CadastrarProduto(self, produto: Livro|CD|DVD):
        if produto.adicionaDados:
            self.banco_de_dados.append(produto)
        else:
            print("Ainda faltam informações do produto!")

    def busca_produto(self, produto: Produto|Livro|CD|DVD):
        try:
            index = self.banco_de_dados.index(produto)
            return index
        except:
            print("Produto Não Encontrado!")
            return None

        #index = 0
        #for produto in self.banco_de_dados:
        #    if produto.codigo_barras == codigo_barras:
        #        return index
        #    index += 1  
        #print("Código de barras não encontrado")
        #return None

    def main(self):
        print("Adicionando 5 produtos ao banco de dados...")
        
        livro1 = Livro('001')
        livro1.adicionaDados("Androides Sonham com Ovelhas Elétricas?", 32.0, "Philip K. Dick")
        self.CadastrarProduto(livro1)

        livro2 = Livro("002")
        livro2.adicionaDados("Java para Iniciantes: Crie, Compile e Execute Programas Java Rapidamente", 122.5, "Herbert Schildt")
        self.CadastrarProduto(livro2)

        livro3 = Livro("003")
        livro3.adicionaDados("Começando a programar em Python para leigos", 75.95, "John Paul Mueller")
        self.CadastrarProduto(livro3)
        
        cd1 = CD("004")
        cd1.adicionaDados("TECNOMELODY 2022 VOL 07", 20.0, 8)
        self.CadastrarProduto(cd1)

        dvd1 = DVD("005")
        dvd1.adicionaDados("Tropa De Elite 2", 29.90, 115)
        self.CadastrarProduto(dvd1)
    
        #Adicionando Itens Já existentes com Cod de barras (Questão 4 - ITEM D)

        #Código de Barras e Produto já existente
        livro_teste = Livro('001')
        livro_teste.adicionaDados("Androides Sonham com Ovelhas Elétricas?", 32.0, "Philip K. Dick")
        self.CadastrarProduto(livro_teste)

        #Código de Barras Diferente
        cd_teste = CD("777")
        cd_teste.adicionaDados("TECNOMELODY 2022 VOL 07", 20.0, 8)
        self.CadastrarProduto(cd_teste)

if __name__ == "__main__":
    loja = Loja()
    loja.main()
    print("Mostrando Produtos Cadastrados: ")
    loja.MostrarProdutosCadastrados()

    # Livro 001 - Já Cadastrado
    livro_aux = Livro('001')
    livro_aux.adicionaDados("Androides Sonham com Ovelhas Elétricas?", 32.0, "Philip K. Dick")

    # CD 555 - Não Cadastrado
    cd_aux = CD("555")
    cd_aux.adicionaDados("Dark Souls Complete OST", 99.0, 8)

    # Pegando o primeiro produto do banco de dados.
    primeiro_produto_bd = loja.banco_de_dados[0]

    print("Verificando se um Produto é igual a outro (Produtos com mesmo Código de Barras)")
    #Equals() -> __eq__ OU ==   
    #Itens Iguais (True)
    print(livro_aux.__eq__(primeiro_produto_bd))
    print(livro_aux == primeiro_produto_bd)

    print("Verificando se um Produto é igual a outro (Produtos Código de Barras Diferentes)")
    #Itens Diferentes (False)
    print(cd_aux.__eq__(primeiro_produto_bd))
    print(cd_aux == primeiro_produto_bd)

    print("Buscando Produto no Banco de Dados... (Produto Existente)")
    #Existe (Devolve Index)
    print(loja.busca_produto(livro_aux))

    #Não Existe (Devolve None e Printa "Produto Não Encontrado!")
    print("Buscando Produto no Banco de Dados... (Produto Inexistente)")
    print(loja.busca_produto(cd_aux))

    #Buscando Itens Já existentes (Questão 4 - ITEM D)

    #Código de Barras E Produto já existente (Retorna o valor do primeiro produto encontrado)
    livro_teste = Livro('001')
    print("Buscando Produto no Banco de Dados... ")
    print(loja.busca_produto(livro_teste))

    #Código de Barras Diferente de um Produto Já existente (Retorna o valor do primeiro produto encontrado (codigo de barras))
    print("Buscando Produto no Banco de Dados...")
    cd_teste = CD("004")
    print(loja.busca_produto(cd_teste))
