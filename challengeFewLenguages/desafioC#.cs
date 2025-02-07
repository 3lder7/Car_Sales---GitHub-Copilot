using System;

public class Program
{
    public static void Main(string[] args)
    {
        // Lendo valores de entrada
        float valorSalario = float.Parse(Console.ReadLine());
        float valorBeneficios = float.Parse(Console.ReadLine());

        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <= 1100)
        {
            // Atribui o imposto de 5% sobre o salário
            valorImposto = 0.05F * valorSalario;
        }
        else if (valorSalario >= 0 && valorSalario <= 2500)
        {
            // Atribui o imposto de 10% sobre o salário
            valorImposto = 0.10F * valorSalario;
        }
        else
        {
            // Atribui o imposto de 15% sobre o salário
            valorImposto = 0.15F * valorSalario;
        }

        // Calcula e imprime a Saída (com 2 casas decimais)
        float saida = valorSalario - valorImposto + valorBeneficios;
        Console.WriteLine(saida.ToString("F2"));
    }
}