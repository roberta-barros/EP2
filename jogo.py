import funcoes
import perguntas

jogar_novamente = True

while jogar_novamente == True:
    questoes = 1
    questoes_corretas = 0
    respostas_lista = ['A', 'B', 'C', 'D']
    todas_respostas_lista = ['A', 'B', 'C', 'D', 'pular', 'ajuda', 'parar']
    premios = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    pergunta = perguntas.quest
    base_questoes = funcoes.transforma_base(perguntas)
    valida_base = funcoes.valida_questoes(base_questoes)
    print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
    nome = input('Qual seu nome? ')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')                     
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    print('Aperte ENTER para continuar...')
    print('O jogo já vai começar! Lá vem a primeira questão!')
    print('Vamos começar com as questões do nível FACIL!')
    print('Aperte ENTER para continuar...')
    if valida_base != {}:
        print('ERRO! O jogo não pode ser iniciado')
    else:
        for i in range(len(pergunta)):
            questao_testada = funcoes.questao_para_texto(pergunta)
            print(questao_testada)
            resposta = input('Qual sua resposta? ')
            if resposta not in todas_respostas_lista:
                print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')