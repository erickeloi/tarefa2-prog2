package questao_07;

public abstract class RobotAbstrato extends Posicao {
	  
	  // Construtor que chama o construtor da superclasse Posicao
	  public RobotAbstrato(int x, int y) {
	    super(x, y);
	  }
	  
	  // Operações que movem o robô para a direita e para a esquerda,
	  // recebendo um parâmetro dx que indica o deslocamento e um parâmetro
	  // par que indica a velocidade
	  public abstract void moveDireita(double dx, double par);
	  public abstract void moveEsquerda(double dx, double par);
	  
	  // Operações que movem o robô para cima e para baixo,
	  // recebendo um parâmetro dy que indica o deslocamento e um parâmetro
	  // par que indica a velocidade
	  public abstract void moveCima(double dy, double par);
	  public abstract void moveBaixo(double dy, double par);
	}