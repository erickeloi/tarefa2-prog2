package questao_06;

public class Circulo extends Forma {
    private float raio;

    public Circulo(float raio) {
        this.raio = raio;
    }

    // Implementação do método calcularArea() herdado de Forma
    @Override
    public float calcularArea() {
        return (float) (Math.PI * raio * raio);
    }

    // Implementação do método calcularPerimetro() herdado de Forma
    @Override
    public float calcularPerimetro() {
        return (float) (2 * Math.PI * raio);
    }
}
