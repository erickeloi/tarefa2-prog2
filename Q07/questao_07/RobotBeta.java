package questao_07;

public class RobotBeta extends RobotAbstrato{

	public RobotBeta(int x, int y) {
		super(x, y);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void moveDireita(double dx, double par) {
		setX(getX() + (int) (dx * par));
	}

	@Override
	public void moveEsquerda(double dx, double par) {
		setX(getX() - (int) (dx * par));
	}

	@Override
	public void moveCima(double dy, double par) {
		setY(getY() + (int) (dy * par));
	}

	@Override
	public void moveBaixo(double dy, double par) {
		setY(getY() - (int) (dy * par));
	}

	public void imprimePosicao() {
		System.out.println(retornaPosicao());
	}
	
	
}