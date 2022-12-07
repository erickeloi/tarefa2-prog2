# 1- Escreva a classe ObjetoGeometrico que represente um objeto geométrico em duas
# dimensões. 

# Esta classe deve ter métodos para inicializar o objeto, mostrar seus dados e
# calcular e retornar a sua área e perímetro. 
import math
class ObjetoGeometrico():
    # Metodo Construtor, para inicializar o objeto,
    # Com Argumentos de Area e Perimetro Opcionais na Inicialização da classe.
    def __init__(self, area=0, perimetro=0):
        self.area = area
        self.perimetro = perimetro
    def calcula_area(self):
        print("Não é possível calcular a área sem previamente informar mais informações sobre o objeto.")
    def calcula_perimetro(self):
        print("Não é possível calcular o perimetro sem previamente informar mais informações sobre o objeto.")
    def mostrar_dados(self):
        print(f"Área: {self.area}")
        print(f"Perimetro: {self.perimetro}")

# Usando esta classe como base, escreva as classes herdeira
# que sobrepõem os métodos descritos em ObjetoGeometrico. 

# Circulo (contendo duas coordenadas para o centro e um raio),
class Circulo(ObjetoGeometrico):
    def __init__(self, centro=0, raio=0):
        self.centro = centro
        self.raio = raio
    def calcula_area(self):
        self.area = math.pi*(self.raio*self.raio)
    def calcula_perimetro(self):
        self.perimetro = 2*math.pi*self.raio 
    def mostrar_dados(self):
        print(f"Raio: {self.raio}")
        print(f"Coordenada do centro: {self.centro}")
        print(f"Área: {self.area}")
        print(f"Perimetro: {self.perimetro}")
# Retangulo (contendo dois valores para os lados)
class Retangulo(ObjetoGeometrico):
    def __init__(self, lado1=0, lado2=0):
        self.lado1 = lado1
        self.lado2 = lado2
    def calcula_perimetro(self):
        self.perimetro = 2*(self.lado1) + 2*(self.lado2)
    def calcula_area(self):
        self.area = self.lado1 * self.lado2
    # A área do retângulo é dada por b*h onde b é um dos lados e h é o outro lado. 
    # Seu perímetro é dado por 2*b+2*h. 
# Triangulo (contendo três valores para os lados), 
class Triangulo(ObjetoGeometrico):
    def __init__(self, lado1=0, lado2=0, lado3=0):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def calcula_area(self):
        a = self.lado1
        b = self.lado2
        c = self.lado3
        s = self.perimetro/2
        self.area = math.sqrt((s*(s-a)*(s-b)*(s-c))) 
    def calcula_perimetro(self):
        self.perimetro = self.lado1+self.lado2+self.lado3
    def mostrar_dados(self):
        print(f"Lado 1: {self.lado1}")
        print(f"Lado 2: {self.lado2}")
        print(f"Lado 3: {self.lado3}")
        print(f"Área: {self.area}")
        print(f"Perimetro: {self.perimetro}")

# Apresentar o diagrama UML, 
# Fazer instâncias das classes herdeiras na classe principal, 
# apresentando como saída áreas e perímetros dos objetos geométricos.