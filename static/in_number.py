# Função: Verificar se um número é par ou ímpar com Copilot.

def verifica_numero():
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 0:
                raise ValueError("Erro, zero é um número neutro.")
            elif numero % 2 == 0:
                print(True)
            else:
                print(False)
        except ValueError as e:
            e 
            print(e)
        
# Exemplo de uso
resultado = verifica_numero()
print(resultado)