# Lista de questões do quiz, cada questão é um dicionário com a pergunta, opções, resposta correta e pontos
questoes = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Paris", "Londres", "Berlim", "Madri"],
        "resposta": "Paris",
        "pontos": 1
    },
    {
        "pergunta": "Qual é a capital do Japão?",
        "opcoes": ["Tóquio", "Pequim", "Seul", "Bangkok"],
        "resposta": "Tóquio",
        "pontos": 1
    },
    {
        "pergunta": "Qual é a capital da Austrália?",
        "opcoes": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "resposta": "Canberra",
        "pontos": 1
    },
    {
        "pergunta": "Qual é a capital do Canadá?",
        "opcoes": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
        "resposta": "Ottawa",
        "pontos": 1
    },
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"],
        "resposta": "Brasília",
        "pontos": 1
    }
]

# Função para exibir uma questão e obter a resposta do usuário
def show_question(questao):
    # Exibe a pergunta
    print(questao["pergunta"])
    # Exibe as opções de resposta
    for i, opcao in enumerate(questao["opcoes"]):
        print(f"{i + 1}. {opcao}")
    
    # Loop para garantir que o usuário insira uma resposta válida
    while True:
        try:
            # Obtém a resposta do usuário
            resposta = int(input("Escolha uma opção (1-4): "))
            # Verifica se a resposta está dentro do intervalo válido
            if 1 <= resposta <= 4:
                # Retorna se a resposta do usuário está correta
                return questao["opcoes"][resposta - 1] == questao["resposta"]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número entre 1 e 4.")

# Função para verificar se a resposta do usuário está correta
def verificar_resposta(questao, resposta_usuario):
    return questao["resposta"] == resposta_usuario

# Função principal do programa
def main():
    # Inicializa a pontuação
    score = 0

    # Itera sobre todas as questões
    for questao in questoes:
        # Exibe a questão e verifica a resposta do usuário
        if show_question(questao):
            # Incrementa a pontuação se a resposta estiver correta
            score += questao["pontos"]
            print("Resposta correta!")
        else:
            print("Resposta incorreta!")
            print("A resposta correta é:", questao["resposta"])
    
    # Exibe a pontuação final do usuário
    print("Você acertou", score, "perguntas de um total de", len(questoes))

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
