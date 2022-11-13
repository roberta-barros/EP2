import funcoes
import perguntas

jogar_novamente = True

while jogar_novamente == True:
    questoes = 0
    questoes_corretas = 0
    respostas_lista = ['A', 'B', 'C', 'D']
    todas_respostas_lista = ['A', 'B', 'C', 'D', 'pular', 'ajuda', 'parar']
    premios = [0, 1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
    ajudas = 2
    pulos = 3
    j = 0
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
        print('\33[1;33mOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\33[m\n')
        nome = input('Qual seu nome? ')
        print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')                     
        print('\33[1;33mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!/33[m\n')
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
                if resposta == 'ajuda':
                    ajudas -= 1
                    if ajudas > 0:
                        ajuda = funcoes.gera_ajuda(questao_sorteada)
                        print('\33[1;34mOk, lá vem ajuda! Você ainda tem 1 ajudas!\33[m\n')
                        print(ajuda)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        if resposta == 'ajuda':
                            print('Não deu! Você já pediu ajuda nessa questão')
                            print(questao_printada)
                            resposta = input('Qual sua resposta? ')
                    if ajudas == 0:
                        print('Não deu! Você não tem mais direito à ajuda')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'pular':
                    pulos -= 1
                    if pulos > 0:
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
                    print(f'Deseja mesmo parar [S/N]? Se sim, seu prêmio é de {premio}')
                    parar = input('')
                    if parar == 'S':
                        jogar = False
                        print('Deseja jogar novamente? [S/N]')
                        jogar_dnv = input('')
                        if jogar_dnv == 'S':
                            jogar_novamente = True
                if resposta in respostas_lista:
                    if resposta == questao_sorteada['correta']:
                        j += 1
                        premio = premios[j]
                        print(f'Você acertou! Seu prêmio atual é de {premio} reais')
                        questoes_corretas += 1
                    else:
                        print('Você errou e perdeu tudo!')
                        jogar = False
                        print('Deseja jogar novamente? [S/N]')
                        jogar_dnv = input('')
                        if jogar_dnv == 'S':
                            jogar_novamente = True
                        else:
                            print('Até mais!')
                            jogar_novamente = False
        if questoes == 4:
            print('HEY! Você passou para o nível MÉDIO')
        if questoes > 3 and questoes <= 6:
            nivel = 'medio'
            questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
            questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
            print(questao_printada)
            resposta = input('Qual sua resposta? ')
            questoes_sorteadas.append(questao_sorteada)
            if resposta not in todas_respostas_lista:
                print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')
            else:
                if resposta == 'ajuda':
                    ajudas -= 1
                    if ajudas > 0:
                        ajuda = funcoes.gera_ajuda(questao_sorteada)
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(ajuda)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        if resposta == 'ajuda':
                            print('Não deu! Você já pediu ajuda nessa questão')
                            print(questao_printada)
                            resposta = input('Qual sua resposta? ')
                    if ajudas == 0:
                        print('Não deu! Você não tem mais direito à ajuda')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'pular':
                    pulos -= 1
                    if pulos > 0:
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
                    parar = input('')
                    if parar == 'S':
                        jogar = False
                        print('Deseja jogar novamente? [S/N]')
                        jogar_dnv = input('')
                        if jogar_dnv == 'S':
                            jogar_novamente = True
                if resposta in respostas_lista:
                    if resposta == questao_sorteada['correta']:
                        j += 1
                        premio = premios[j]
                        print(f'Você acertou! Seu prêmio atual é de {premio} reais')
                        questoes_corretas += 1
                    else:
                        print('Você errou e perdeu tudo!')
                        jogar = False
                        print('Deseja jogar novamente? [S/N]')
                        jogar_dnv = input('')
                        if jogar_dnv == 'S':
                            jogar_novamente = True
                        else:
                            print('Até mais!')
                            jogar_novamente = False
        if questoes == 7:
            print('HEY! Você passou para o nível DIFÍCIL')
        if questoes > 6 and questoes <= 9:
            nivel = 'dificil'
            questao_sorteada = funcoes.sorteia_questao_inedita(base_questoes, nivel, questoes_sorteadas)
            questao_printada = funcoes.questao_para_texto(questao_sorteada, questoes)
            print(questao_printada)
            resposta = input('Qual sua resposta? ')
            questoes_sorteadas.append(questao_sorteada)
            if resposta not in todas_respostas_lista:
                print('Opção inválida! \nAs opções de resposta são "A", "B", "C", "D", "ajuda", "pular" e "parar"!')
                print(questao_printada)
                resposta = input('Qual sua resposta? ')
            else:
                if resposta == 'ajuda':
                    ajudas -= 1
                    if ajudas > 0:
                        ajuda = funcoes.gera_ajuda(questao_sorteada)
                        print('Ok, lá vem ajuda! Você ainda tem 1 ajudas!')
                        print(ajuda)
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                        if resposta == 'ajuda':
                            print('Não deu! Você já pediu ajuda nessa questão')
                            print(questao_printada)
                            resposta = input('Qual sua resposta? ')
                    if ajudas == 0:
                        print('Não deu! Você não tem mais direito à ajuda')
                        print(questao_printada)
                        resposta = input('Qual sua resposta? ')
                if resposta == 'pular':
                    pulos -= 1
                    if pulos > 0:
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
                    parar = input('')
                    if parar == 'S':
                        jogar = False
                        print('Deseja jogar novamente? [S/N]')
                        jogar_dnv = input('')
                        if jogar_dnv == 'S':
                            jogar_novamente = True
                    if parar == 'N':
                        jogar = True
                if resposta in respostas_lista:
                    if resposta == questao_sorteada['correta']:
                        j += 1
                        premio = premios[j]
                        print(f'Você acertou! Seu prêmio atual é de {premio} reais')
                        questoes_corretas += 1
                        if questoes_corretas == 9:
                            print('\33[1;31mParabéns! Você zerou o jogo e ganhou 1 milhão de reais\33[m')
                    else:
                        print('Você errou e perdeu tudo!')
                        jogar = False
                        print('Deseja jogar novamente? [S/N]')
                        jogar_dnv = input('')
                        if jogar_dnv == 'S':
                            jogar_novamente = True
                        else:
                            print('Até mais!')
                            jogar_novamente = False