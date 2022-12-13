# 2- Usando o exercício 1 como base, escreva as classes:
# Quadrado, que herda da classe Retangulo 
# mas somente precisa inicializar um dos lados, 

# E as classes:
# TrianguloEquilatero, TrianguloIsosceles e TrianguloEscaleno que precisam inicializar
# somente um, dois ou três lados do triângulo. 

# Para cada uma destas classes, quais métodos devem ser sobrepostos 
# e quais podem ser aproveitados, 

# Apresentar Diagrama UML e Fazer instâncias das classes herdeiras na classe principal, 
# apresentando como saída áreas e perímetros dos objetos geométricos.

import math
class ObjetoGeometrico():
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        self.area: float
        self.perimetro: int
    # Definindo Getters
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getArea(self):
        return self.area
    def getPerimetro(self):
        return self.perimetro

    # Definindo Setters
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def setPerimetro(self, perimetro):
        self.perimetro = perimetro
    def setArea(self, area):
        self.area = area

    def calcula_perimetro(self):
        return None
    def calcula_area(self):
        return None

    def retornar_dados(self):
        dados = f"""Coordenada X: {self.x}
Coordenada Y: {self.y}    
Área: {self.area}
Perimetro: {self.perimetro}"""
        return dados

class Circulo(ObjetoGeometrico):
    def __init__(self, x: int, y: int, raio: int):
        self.raio = raio
        super().__init__(x, y)

    def getRaio(self):
        return self.raio
    
    def setRaio(self, raio: int):
        self.raio = raio

    def calcula_area(self):
        return math.pi*(self.raio*self.raio)

    def calcula_perimetro(self):
        return 2*math.pi*self.raio 

    def retornar_dados(self):
        return f"Raio: {self.raio}\n"+ super().retornar_dados()

class Retangulo(ObjetoGeometrico):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        
    def calcula_perimetro(self):
        return 2*(self.x) + 2*(self.y)

    def calcula_area(self):
        return self.x * self.y

class Triangulo(ObjetoGeometrico):
    def __init__(self, x: int, y: int, z: int):
        super().__init__(x, y)
        self.z = z

    def calcula_perimetro(self):
        return self.x + self.y + self.z

    def calcula_area(self):
        a = self.x
        b = self.y
        c = self.z
        s = (self.calcula_perimetro()/2)
        return math.sqrt((s*(s-a)*(s-b)*(s-c))) 

    def retornar_dados(self):
        return f"Coordenada Z: {self.z}\n" + super().retornar_dados()


# Questão 2:

# Classe Quadrado (Só é necessário colocar um dos lados)
class Quadrado(Retangulo):
    def __init__(self, x: int):
        super().__init__(x, x)

# Classe Triangulo Equilatero (Só é necessário colocar um dos lados)
class TrianguloEquilatero(Triangulo):
    def __init__(self, x: int):
        super().__init__(x, x, x)

# Classe Triangulo Isosceles (Só é necessário colocar dois dos lados)
class TrianguloIsosceles(Triangulo):
    def __init__(self, lado_maior: int, lado_igual: int):
        super().__init__(lado_igual, lado_igual, lado_maior)

# Classe Triangulo Escaleno (É necessário colocar os três lados)   
class TrianguloEscaleno(Triangulo):
    def __init__(self, x: int, y: int, z: int):
        super().__init__(x, y, z)

if __name__ == "__main__":
    print("Quadrado de lado 2: \n")
    q = Quadrado(2)
    q.setArea(q.calcula_area())
    q.setPerimetro(q.calcula_perimetro())
    print(q.retornar_dados())

    print()

    print("Triangulo Equilatero de lado 2: \n")
    te = TrianguloEquilatero(2)
    te.setArea(te.calcula_area())
    te.setPerimetro(te.calcula_perimetro())
    print(te.retornar_dados())
