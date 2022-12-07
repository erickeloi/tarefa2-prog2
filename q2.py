# 2- Usando o exercício 1 como base, escreva as classes 
# Quadrado, que herda da classe Retangulo 
# mas somente precisa inicializar um dos lados, 

# e as classes:
# TrianguloEquilatero, TrianguloIsosceles e TrianguloEscaleno que precisam inicializar
# somente um, dois ou três lados do triângulo. 
# 
# Para cada uma destas classes, quais métodos devem ser sobrepostos 
# e quais podem ser aproveitados, 
# apresentar Diagrama UML e Fazer instâncias das classes herdeiras na classe principal, 
# apresentando como saída áreas e perímetros dos objetos geométricos.

import math
class ObjetoGeometrico():
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

class Retangulo(ObjetoGeometrico):
    def __init__(self, lado1=0, lado2=0):
        self.lado1 = lado1
        self.lado2 = lado2
    def calcula_perimetro(self):
        self.perimetro = 2*(self.lado1) + 2*(self.lado2)
    def calcula_area(self):
        self.area = self.lado1 * self.lado2

class Triangulo(ObjetoGeometrico):
    def __init__(self, lado1=0, lado2=0, lado3=0):
        super().__init__()
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

# Quadrado, que herda da classe Retangulo 
# mas somente precisa inicializar um dos lados, 
class Quadrado(Retangulo):
    def __init__(self, lado):
        self.lado = lado
        self.perimetro = 4*lado
        self.area = lado**2

q = Quadrado(2)
q.mostrar_dados()

# e as classes:
# TrianguloEquilatero, TrianguloIsosceles e TrianguloEscaleno que precisam inicializar
# somente um, dois ou três lados do triângulo. 
class TrianguloEquilatero(Triangulo):
    def __init__(self, lado):
        super().__init__(lado, lado, lado)

class TrianguloIsosceles(Triangulo):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado2
class TrianguloEscaleno(Triangulo):
    pass

te = TrianguloEquilatero(2)

te.calcula_perimetro()
te.calcula_area()
print(te.area)