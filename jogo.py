import funcoes
import perguntas

jogar_novamente = True

while jogar_novamente == True:
    questoes = 0
    questoes_corretas = 0
    respostas_lista = ['A', 'B', 'C', 'D']
    todas_respostas_lista = ['A', 'B', 'C', 'D', 'pular', 'ajuda', 'parar']
    premios = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    i = 0
    premio = premios[i]
    lista_perguntas = perguntas.quest
    base_questoes = funcoes.transforma_base(lista_perguntas)
    questoes_sorteadas = []
    x = True
    jogar = True
    niveis = ['facil', 'medio', 'dificil']
    for nivel in niveis:
        validar_base = base_questoes[nivel]
        base_validada = funcoes.valida_questoes(validar_base)
        for i in range(len(base_validada)):
            if base_validada[i] != {}:
                print('ERRO! O jogo não pode ser iniciado.')
                x = False
                jogar = False
    if x == True:
        print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
        nome = input('Qual seu nome? ')
        print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')                     
        print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')
        print('O jogo já vai começar! Lá vem a primeira questão!')
        print('Vamos começar com as questões do nível FACIL!')
    while jogar == True:
        questoes += 1
        if questoes <= 3:
            nivel = 'facil'
            questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
            questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
            print(questao_printada)
            resposta = input('Qual sua resposta? ')
            questoes_sorteadas.append(questao_sorteada)
            if resposta not in todas_respostas_lista:
                print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')
            else:
                ajudas = 2
                pulos = 3
                if resposta == 'ajuda':
                    if ajudas > 0:
                        ajuda = funcoes.gera_ajuda(questao_sorteada)
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(ajuda)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        ajudas -= 1
                        if resposta == 'ajuda':
                            print('Não deu! Você já pediu ajuda nessa questão')
                            print(questao_printada)
                            resposta = input('Qual sua resposta? ')
                    if ajudas == 0:
                        print('Não deu! Você não tem mais direito à ajuda')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'pular':
                    if pulos > 0:
                        questoes += 1
                        pulos -= 1
                        print(f'Ok, pulando! Você ainda tem direito a {pulos} pulos')
                        questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
                        questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        questoes_sorteadas.append(questao_sorteada)
                    if pulos == 0:
                        print('Você não tem direito a mais pulos')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'parar':
                    print(f'Deseja mesmo parar? Se sim, seu prêmio é de {premio}')
                if resposta in respostas_lista:
                    if resposta == questao_sorteada['correta']:
                        i += 1
                        print(f'Você acertou! Seu prêmio atual é de {premio} reais')
                    else:
                        print('Você errou!')
        if questoes > 3 and questoes <= 6:
            print('HEY! Você passou para o nível MÉDIO')
            nivel = 'medio'
            questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
            questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
            print(questao_printada)
            resposta = input('Qual sua resposta? ')
            questoes_sorteadas.append(questao_sorteada)
            if resposta not in todas_respostas_lista:
                print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')
            else:
                ajudas = 2
                pulos = 3
                if resposta == 'ajuda':
                    if ajudas > 0:
                        ajuda = funcoes.gera_ajuda(questao_sorteada)
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(ajuda)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        ajudas -= 1
                        if resposta == 'ajuda':
                            print('Não deu! Você já pediu ajuda nessa questão')
                            print(questao_printada)
                            resposta = input('Qual sua resposta? ')
                    if ajudas == 0:
                        print('Não deu! Você não tem mais direito à ajuda')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'pular':
                    if pulos > 0:
                        questoes += 1
                        pulos -= 1
                        print(f'Ok, pulando! Você ainda tem direito a {pulos} pulos')
                        questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
                        questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        questoes_sorteadas.append(questao_sorteada)
                    if pulos == 0:
                        print('Você não tem direito a mais pulos')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'parar':
                    print(f'Deseja mesmo parar? Se sim, seu prêmio é de {premio}')
                if resposta in respostas_lista:
                    if resposta == questao_sorteada['correta']:
                        i += 1
                        print(f'Você acertou! Seu prêmio atual é de {premio} reais')
                    else:
                        print('Você errou!')
        if questoes > 6 and questoes <= 9:
            nivel = 'dificil'
            questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
            questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
            print(questao_printada)
            resposta = input('Qual sua resposta? ')
            questoes_sorteadas.append(questao_sorteada)
            if resposta not in todas_respostas_lista:
                print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')
            else:
                ajudas = 2
                pulos = 3
                if resposta == 'ajuda':
                    if ajudas > 0:
                        ajuda = funcoes.gera_ajuda(questao_sorteada)
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(ajuda)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        ajudas -= 1
                        if resposta == 'ajuda':
                            print('Não deu! Você já pediu ajuda nessa questão')
                            print(questao_printada)
                            resposta = input('Qual sua resposta? ')
                    if ajudas == 0:
                        print('Não deu! Você não tem mais direito à ajuda')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'pular':
                    if pulos > 0:
                        pulos -= 1
                        print(f'Ok, pulando! Você ainda tem direito a {pulos} pulos')
                        questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
                        questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        questoes_sorteadas.append(questao_sorteada)
                    if pulos == 0:
                        print('Você não tem direito a mais pulos')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'parar':
                    print(f'Deseja mesmo parar? Se sim, seu prêmio é de {premio}')
                if resposta in respostas_lista:
                    if resposta == questao_sorteada['correta']:
                        i += 1
                        print(f'Você acertou! Seu prêmio atual é de {premio} reais')
                    else:
                        print('Você errou!')