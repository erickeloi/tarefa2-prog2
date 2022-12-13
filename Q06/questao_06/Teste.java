package questao_06;

public class Teste {
    public static void main(String[] args) {
        Forma[] formas = new Forma[5];
        formas[0] = new Retangulo(10, 5);
        formas[1] = new Circulo(2);
        formas[2] = new Quadrado(6);
        formas[3] = new Retangulo(3, 8);
        formas[4] = new Circulo(4);

        for (Forma forma : formas) {
            System.out.println("Área: " + forma.calcularArea());
            System.out.println("Perímetro: " + forma.calcularPerimetro());
        }
    }
}
