package questao_07;

public class TesteRobot {
	  public static void main(String[] args) {
	    // Criar um novo objeto RobotAlfa e RobotBeta
	    RobotAlfa robotAlfa = new RobotAlfa(0,0);
	    RobotBeta robotBeta = new RobotBeta(1,1);
	    
	    
	    // Mover os robôs no plano xy
	    robotAlfa.moveBaixo(1, 3);
	    robotAlfa.moveEsquerda(3, 2);
	    robotAlfa.moveDireita(6, 1);
	    
	    robotBeta.moveDireita(2, 2);
	    robotBeta.moveBaixo(5, 1);
	    robotBeta.moveCima(3, 2);
	    
	    // Retorna Posição Final dos Robôs
	    robotAlfa.imprimePosicao();
	    robotBeta.imprimePosicao();
	  }
	}
