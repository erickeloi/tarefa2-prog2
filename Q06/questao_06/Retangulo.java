package questao_06;


public class Retangulo extends Forma {
    private float lado;
    private float altura;

    public Retangulo(float lado, float altura) {
        this.lado = lado;
        this.altura = altura;
    }

    // Implementação do método calcularArea() herdado de Forma
    @Override
    public float calcularArea() {
        return lado * altura;
    }

    // Implementação do método calcularPerimetro() herdado de Forma
    @Override
    public float calcularPerimetro() {
        return 2 * (lado + altura);
    }
}
