package questao_05;

public class Quadrado implements Impressao, FormaGeometrica {

	private double lado;
	
	@Override
	public double area() {
		double area = lado*lado;
		return area;
	}

	@Override
	public double comprimento() {
		double comprimento = lado*4;
		return comprimento;
	}

	@Override
	public void imprimeDados() {
		System.out.println("Lado: " + lado + "\n"
				+ "Area: " + area() + "\n"
				+ "Comprimento: " + comprimento()
				+ "\n----------");
	}

	public Quadrado(double lado) {
		super();
		this.lado = lado;
	}

	
	
}
