import funcoes
import perguntas

jogar_novamente = True

while jogar_novamente == True:
    questoes = 1
    questoes_corretas = 0
    respostas_lista = ['A', 'B', 'C', 'D']
    todas_respostas_lista = ['A', 'B', 'C', 'D', 'pular', 'ajuda', 'parar']
    premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    lista_perguntas = perguntas.quest
    base_questoes = funcoes.transforma_base(lista_perguntas)
    faceis = base_questoes['facil']
    medias = base_questoes['medio']
    dificeis = base_questoes['dificil']
    print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
    nome = input('Qual seu nome? ')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')                     
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    print('Aperte ENTER para continuar...')
    print('O jogo já vai começar! Lá vem a primeira questão!')
    print('Vamos começar com as questões do nível FACIL!')
    print('Aperte ENTER para continuar...')
    valida_facil = funcoes.valida_questoes(faceis)
    valida_medio = funcoes.valida_questoes(medias)
    valida_dificil = funcoes.valida_questoes(dificeis)
    questoes_sorteadas = []
    if valida_facil != [] or valida_medio != [{},{},{},{},{},{},{},{},{},{}] or valida_dificil != [{},{},{},{},{},{},{},{},{},{}]:
        print('ERRO! O jogo não pode ser iniciado')
    else:
        for i in range(len(lista_perguntas)):
            if questoes <= 3:
                nivel = 'facil'
                questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
                questao_printada = funcoes.questao_para_texto(questao_sorteada)
                print(questao_printada)
                resposta = input('Qual sua resposta? ')
                if resposta not in todas_respostas_lista:
                    print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')