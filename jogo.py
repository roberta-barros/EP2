import funcoes
import perguntas

jogar_novamente = True

while jogar_novamente == True:
    questoes = 1
    questoes_corretas = 0
    respostas_lista = ['A', 'B', 'C', 'D']
    todas_respostas_lista = ['A', 'B', 'C', 'D', 'pular', 'ajuda', 'parar']
    pergunta = perguntas.quest
    base_de_questoes = funcoes.transforma_base(perguntas)
    print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
    nome = input('Qual seu nome? ')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')                     
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')