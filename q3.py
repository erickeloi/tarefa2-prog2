# 3. Crie uma hierarquia de classes de domínio para uma loja que venda livros, CDs e
# DVDs. Sobrescreva o método toString() para que imprima:
# • Para livros: nome, preço e autor;
# • Para CDs: nome, preço e número de faixas;
# • Para DVDs: nome, preço e duração.

# Evite ao máximo repetição de código utilizando a palavra super no construtor e no
# método sobrescrito. Em seguida, crie uma classe Loja com o método main() que
# adicione 5 produtos diferentes (a sua escolha) a um vetor e, por fim, imprima o
# conteúdo do vetor. 

# Apresentar o Diagrama UML.

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

    def main(self):
        print("Adicionando 5 produtos ao banco de dados...")
        
        livro1 = Livro('001')
        livro1.adicionaDados("Androides Sonham com Ovelhas Elétricas?", 32.0, "Philip K. Dick")
        self.CadastrarProduto(livro1)

        livro2 = Livro("004")
        livro2.adicionaDados("Java para Iniciantes: Crie, Compile e Execute Programas Java Rapidamente", 122.5, "Herbert Schildt")
        self.CadastrarProduto(livro2)

        livro3 = Livro("005")
        livro3.adicionaDados("Começando a programar em Python para leigos", 75.95, "John Paul Mueller")
        self.CadastrarProduto(livro3)
        
        cd1 = CD("002")
        cd1.adicionaDados("TECNOMELODY 2022 VOL 07", 20.0, 8)
        self.CadastrarProduto(cd1)

        dvd1 = DVD("003")
        dvd1.adicionaDados("Tropa De Elite 2", 29.90, 115)
        self.CadastrarProduto(dvd1)

if __name__ == "__main__":
    loja = Loja()
    loja.main()
    loja.MostrarProdutosCadastrados()