projetos = []

#teste parhshfsfhusdhfushd

def interpolacao(projetos, caracteristica_atual):
    caracteristica_escolhida = 'orçamento'  # escolhe a característica de orçamento
    projetos.sort(key=lambda x: x[caracteristica_escolhida])  # ordena a lista por essa característica

    # Encontrar os projetos mais próximos
    idx = 0
    while idx < len(projetos) and projetos[idx][caracteristica_escolhida] < caracteristica_atual[caracteristica_escolhida]:
        idx += 1
    
    if idx == 0 or idx == len(projetos):
        P = 0.5  # Define uma probabilidade padrão se não houver projetos para interpolar
    else:
        x0 = projetos[idx-1][caracteristica_escolhida]
        x1 = projetos[idx][caracteristica_escolhida]

        # Calcular a probabilidade estimada
        if x1 - x0 == 0:
            P = 0.5  # ou outro valor padrão
        else:
            # Fórmula da interpolação 
            P = ((caracteristica_atual[caracteristica_escolhida] - x0) / (x1 - x0)) * 0.5 + 0.5

    # Aplicar o peso da complexidade
    peso_complexidade = {
        1: 0.5,  # Baixa complexidade
        2: 1.0,  # Complexidade moderada
        3: 1.5   # Alta complexidade
    }
    P *= peso_complexidade[caracteristica_atual['complexidade']]

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
        print(f"\nProjeto '{nome_projeto}' adicionado com sucesso!\n")

    elif opção == "2":
        if len(projetos) == 0:
            print("Não há projetos adicionados. Adicione um projeto primeiro!")
        else:
            print("\nProjetos adicionados:\n")
            for i, projeto in enumerate(projetos):
                print(f"|{i+1}| -> {projeto['nome']}")
                print(f"Dados do {projeto['nome']}:")
                print(f"  Nome: {projeto['nome']}")
                print(f"  Orçamento: R$ {projeto['orçamento']:.2f}")
                print(f"  Equipe: {projeto['equipe']} pessoas")
                print(f"  Complexidade: {projeto['complexidade']} = > (1)Baixa, (2)Moderada ou (3)Alta\n")

            projeto_escolhido = int(input("Escolha o número do projeto para calcular a probabilidade de sucesso: ")) - 1
            caracteristica_atual = projetos[projeto_escolhido]
            probabilidade_estimada = interpolacao(projetos, caracteristica_atual)
            probabilidade_estimada_porcentagem = probabilidade_estimada * 100
            print(f"\nA probabilidade estimada do projeto '{caracteristica_atual['nome']}' para dar certo é de {probabilidade_estimada_porcentagem:.1f}%")

    elif opção == "3":
        print("\nSaindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente!")



'''
P = ((caracteristica_atual[caracteristica_escolhida] - x0) / (x1 - x0)) * 0.5 + 0.5

P =  é a probabilidade estimada
caracteristica_atual[caracteristica_escolhida] = é o valor atual da característica do projeto que estamos avaliando (por exemplo, o orçamento),
x0 e x1 = são os valores das características dos projetos mais próximos que temos como referência para interpolação.

Essa fórmula assume que a probabilidade está linearmente relacionada com a diferença entre o valor atual e o valor de referência mais próximo, 
normalizando o resultado para um intervalo entre 0 e 1. A adição de 0.5 no final é para garantir que a probabilidade esteja sempre 
entre 0.5 e 1, evitando probabilidades negativas.
'''


'''
A função interpolação tem como finalidade estimar um valor (probabilidade, neste contexto) com base na posição de uma característica de orçamento específica (característica_atual) em relação a um conjunto de projetos existentes, levando em consideração também o nível de complexidade do projeto. Ela utiliza a técnica de interpolação linear para encontrar um valor estimado entre dois pontos conhecidos, ajustando essa estimativa com base na complexidade do projeto. A função pode ser utilizada em diversos contextos onde é necessário estimar valores ou tomar decisões baseadas em dados numéricos contínuos, como orçamentos. Aqui está como ela pode ser aplicada:

Contexto de Uso
Em um cenário de gerenciamento de projetos, onde cada projeto tem um orçamento associado e um nível de complexidade, a função interpolação pode ser usada para:

Estimar Custos: Determinar um custo estimado para um novo projeto com base nos custos de projetos anteriores que possuem características semelhantes, ajustando essa estimativa pela complexidade do novo projeto.
Alocação de Recursos: Auxiliar na decisão de alocação de recursos, estimando a probabilidade de sucesso ou o retorno sobre o investimento (ROI) de um projeto, baseando-se em dados históricos de projetos com orçamentos e complexidades similares.
Análise de Risco: Avaliar o risco associado a um novo projeto, comparando-o com projetos anteriores de características semelhantes, e ajustando a análise com base na complexidade do projeto.
Como Funciona
Ordenação dos Projetos: Primeiro, os projetos são ordenados com base em uma característica específica, neste caso, o orçamento. Isso permite a aplicação da interpolação linear entre dois pontos (projetos) conhecidos.

Encontrar Projetos Mais Próximos: A função identifica os dois projetos com orçamentos imediatamente inferior e superior ao do projeto atual (ou o mais próximo possível, no caso de extremos).

Cálculo da Interpolação Linear: Utiliza a interpolação linear para estimar um valor (probabilidade) com base na posição relativa do orçamento do projeto atual entre os dois projetos identificados.

Ajuste pela Complexidade: O valor estimado é então ajustado multiplicando-se por um fator que representa a complexidade do projeto atual, permitindo que a estimativa reflita não apenas a relação linear com o orçamento, mas também a complexidade do projeto.

Benefícios
Flexibilidade: Pode ser adaptada para diferentes características além do orçamento, como tempo estimado, tamanho da equipe, etc.
Decisões Baseadas em Dados: Fornece uma base quantitativa para tomada de decisões em gestão de projetos.
Customização: O ajuste pela complexidade permite uma customização da estimativa para refletir fatores específicos do projeto.
Em resumo, a função interpolação é uma ferramenta valiosa para estimar valores e tomar decisões informadas em gestão de projetos, permitindo uma análise detalhada baseada em características específicas dos projetos e suas complexidades.
'''


'''
EXEMPLO DE CRIAÇÃO DE UM PROJETO PARA ABRIR UMA LOJA DE SEMI-JOIAS

Projeto: Abrir uma loja de semi-joias
Resumo dos Custos Iniciais:
Estoque Inicial: R$ 15.000,00
Aluguel e Infraestrutura: R$ 17.000,00
Salários e Benefícios 3 PESSOAS (1º mês): R$ 6.000,00
Marketing e Divulgação: R$ 5.000,00
Licenças e Permissões: R$ 2.000,00
Capital de Giro: R$ 36.000,00
Total Estimado: R$ 81.000,00
'''
