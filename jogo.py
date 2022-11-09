import funcoes
import perguntas

jogo_correto = True

while jogo_correto == True:
    
    base_de_questoes = funcoes.transforma_base(perguntas)
    print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!')
    nome = input('Qual seu nome? ')
    print(f'Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!')                     
    print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!')
    print('Aperte ENTER para continuar...')
    print('O jogo já vai começar! Lá vem a primeira questão!')
    print('Vamos começar com as questões do nível FACIL!')
    print('Aperte ENTER para continuar...')