# 1- Escreva a classe ObjetoGeometrico que represente um objeto geométrico em duas
# dimensões. 

# Esta classe deve ter métodos para inicializar o objeto, mostrar seus dados e
# calcular e retornar a sua área e perímetro. 
import math
class ObjetoGeometrico():
    # Metodo Construtor, para inicializar o objeto,
    # Com Argumentos das Coordenadas X e Y
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

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
    
    # Colocando funções de cálculo de perimetro e área 
    # (ainda não é possível cálcular ambos sem mais informações do objeto)
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

# Usando esta classe como base, escreva as classes herdeira
# que sobrepõem os métodos descritos em ObjetoGeometrico. 

# Circulo (contendo duas coordenadas para o centro e um raio),
class Circulo(ObjetoGeometrico):
    def __init__(self, x: int, y: int, raio: int):
        super().__init__(x, y)
        self.raio = raio

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

# Retangulo (contendo dois valores para os lados)
class Retangulo(ObjetoGeometrico):
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
        
    def calcula_perimetro(self):
        return 2*(self.x) + 2*(self.y)

    def calcula_area(self):
        return self.x * self.y

# Triangulo (contendo três valores para os lados), 
class Triangulo(ObjetoGeometrico):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
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

# Apresentar o diagrama UML, 
# Fazer instâncias das classes herdeiras na classe principal, 
# apresentando como saída áreas e perímetros dos objetos geométricos.

if __name__ == "__main__":
    print("Circulo de raio 2: \n")
    c = Circulo(0,0,2)
    c.setArea(c.calcula_area())
    c.setPerimetro(c.calcula_perimetro())
    print(c.retornar_dados())

    print()

    print("Retangulo de lados: 2 e 2: \n")
    r = Retangulo(2,2)
    r.setArea(r.calcula_area())
    r.setPerimetro(r.calcula_perimetro())
    print(r.retornar_dados())

    print()

    print("Triangulo de lados: 2,2,2: \n")
    t = Triangulo(2,2,2)
    t.setArea(t.calcula_area())
    t.setPerimetro(t.calcula_perimetro())
    print(t.retornar_dados())