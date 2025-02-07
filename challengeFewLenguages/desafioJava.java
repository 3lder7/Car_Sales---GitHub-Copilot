import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		//Lendo valores de entrada
		Scanner input = new Scanner(System.in);
		float valorSalario= input.nextFloat();
		float valorBeneficios = input.nextFloat();
		
		float valorImposto = 0;
		if(valorSalario >= 0 && valorSalario <= 1100){
		    //Atribui o imposto de 5% sobre o salário
		    valorImposto = 0.05F * valorSalario;
		}
		else if(valorSalario >= 0 && valorSalario <= 2500){
		    //Atribui o imposto de 10% sobre o salário
		    valorImposto = 0.10F * valorSalario;
		}
		else{
		    //Atribui o imposto de 15% sobre o salário
		    valorImposto = 0.15F * valorSalario;
		}
		//Completando com atividade
		
		//Calcula e imprime a Saída (com 2 casas decimais)
		float saida = valorSalario - valorImposto + valorBeneficios;
		System.out.println(String.format("%.2f", saida));
	}
}