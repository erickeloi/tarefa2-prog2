package questao_07;

public abstract class Posicao {
	  
	  // Atributos x e y, ambos do tipo int
	  private int x;
	  private int y;
	  
	  // Construtor que inicializa os atributos x e y com os valores especificados
	  public Posicao(int x, int y) {
	    this.x = x;
	    this.y = y;
	  }
	  
	  // Métodos set para os atributos x e y
	  public void setX(int x) {
	    this.x = x;
	  }
	  
	  public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public void setY(int y) {
	    this.y = y;
	  }
	  
	  // Método que retorna a posição em forma de string
	  public String retornaPosicao() {
	    return "(" + x + ", " + y + ")";
	  }
	}

