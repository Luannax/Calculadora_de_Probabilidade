projetos = []

def interpolação(projetos, característica_atual):
    característica_escolhida = 'orçamento'  # escolhe a característica de orçamento
    projetos.sort(key=lambda x: x[característica_escolhida])  # ordena a lista por essa característica

    # Encontrar os projetos mais próximos
    idx = 0
    while projetos[idx][característica_escolhida] < característica_atual[característica_escolhida]:
        idx += 1
    x0 = projetos[idx-1][característica_escolhida]
    x1 = projetos[idx][característica_escolhida]

    # Calcular a probabilidade estimada
    if x1 - x0 == 0:
        P = 0.5  # ou outro valor padrão, dependendo do que você deseja fazer nesse caso
    else:
        P = (característica_atual[característica_escolhida] - x0) / (x1 - x0) * 0.5 + 0.5

    # Aplicar o peso da complexidade
    peso_complexidade = {
        1: 0.5,  # Baixa complexidade
        2: 1.0,  # Complexidade moderada
        3: 1.5   # Alta complexidade
    }
    P *= peso_complexidade[característica_atual['complexidade']]

    return P

while True:
    print("\nOpções:")
    print("1. Adicionar projeto")
    print("2. Calcular probabilidade de sucesso")
    print("3. Sair")

    opção = input("Escolha uma opção: ")

    if opção == "1":
        nome_projeto = input("Informe o nome do projeto: ")
        orçamento = float(input("Informe o orçamento do projeto: "))
        equipe = int(input("Informe o tamanho da equipe do projeto: "))
        complexidade = int(input("Informe a complexidade do projeto (1 - Baixa, 2 - Moderada, 3 - Alta): "))
        projetos.append({'nome': nome_projeto, 'orçamento': orçamento, 'equipe': equipe, 'complexidade': complexidade})
        

    elif opção == "2":
        if len(projetos) == 0:
            print("Não há projetos adicionados. Adicione um projeto primeiro!")
        else:
            print("Projetos adicionados:")
            for i, projeto in enumerate(projetos):
                print(f"|{i+1}| -> {projeto['nome']}")
                print(f"\nProjeto '{nome_projeto}' adicionado com sucesso!\n")
                print(f"Dados do {projeto['nome']}:")
                print(f"  Nome: {nome_projeto}")
                print(f"  Orçamento: R$ {orçamento:.2f}")
                print(f"  Equipe: {equipe} pessoas")
                print(f"  Complexidade: {complexidade} = > (1)Baixa, (2)Moderada ou (3)Alta\n")

            projeto_escolhido = int(input("Escolha o número do projeto para calcular a probabilidade de sucesso: ")) - 1
            característica_atual = projetos[projeto_escolhido]
            probabilidade_estimada = interpolação(projetos, característica_atual)
            print(f"A probabilidade estimada do projeto '{característica_atual['nome']}' dar certo é de {probabilidade_estimada:.2f}%")

    elif opção == "3":
        print("\nSaindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente!")