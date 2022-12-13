package questao_05;

public class Circulo implements Impressao, FormaGeometrica {

	private double raio;
	
	@Override
	public void imprimeDados() {
		System.out.println("Raio: " + raio + "\n"
				+ "Area: " + area() + "\n"
				+ "Comprimento: " + comprimento()
				+ "\n----------");

	}

	@Override
	public double area() {
		double area = Math.PI*(raio*raio);
		return area;
	}

	@Override
	public double comprimento() {
		double comprimento = Math.PI*raio*2;
		return comprimento;
	}

	public Circulo(double raio) {
		super();
		this.raio = raio;
	}

	
	
}
