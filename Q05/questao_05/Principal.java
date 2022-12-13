package questao_05;

public class Principal {

	public static void main(String[] args) {
		
		Circulo circulo1 = new Circulo(1.5);
		Circulo circulo2 = new Circulo(5);
	
		Quadrado quadrado1 = new Quadrado(1.5);
		Quadrado quadrado2 = new Quadrado(4);
		
		circulo1.imprimeDados();
		circulo2.imprimeDados();
		
		quadrado1.imprimeDados();
		quadrado2.imprimeDados();
		
	}
	
}
