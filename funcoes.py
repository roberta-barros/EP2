import random

def transforma_base(lista):
    novo = {}
    for questao in lista:
        if questao['nivel'] in novo:
            novo[questao['nivel']].append(questao)
        if questao['nivel'] not in novo:
            novo[questao['nivel']] = []
            novo[questao['nivel']].append(questao)
    return novo

def valida_questao(questao):
    retorno = {}
    if 'titulo' not in questao:
        retorno['titulo'] = 'nao_encontrado'
    if 'nivel' not in questao:
        retorno['nivel'] = 'nao_encontrado'
    if 'opcoes' not in questao:
        retorno['opcoes'] = 'nao_encontrado'
    if 'correta' not in questao:
        retorno['correta'] = 'nao_encontrado'
    if len(questao) != 4:
        retorno['outro'] = 'numero_chaves_invalido'
    if 'titulo' in questao:
        if questao['titulo'] == '' or questao['titulo'].strip() == '':
            retorno['titulo'] = 'vazio'
    if 'nivel' in questao:
        if questao['nivel'] != 'facil' and questao['nivel'] != 'medio' and questao['nivel'] != 'dificil':
            retorno['nivel'] = 'valor_errado'
    if 'opcoes' in questao:
        if len(questao['opcoes']) != 4:
            retorno['opcoes'] = 'tamanho_invalido'
        if len(questao['opcoes']) == 4:
            if 'A' not in questao['opcoes'] or 'B' not in questao['opcoes'] or 'C' not in questao['opcoes'] or 'D' not in questao['opcoes']:
                retorno['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                novo = {}
                if questao['opcoes']['A'].strip() == '':
                    novo['A'] = 'vazia'
                if questao['opcoes']['B'].strip() == '':
                    novo['B'] = 'vazia'
                if questao['opcoes']['C'].strip() == '':
                    novo['C'] = 'vazia'
                if questao['opcoes']['D'].strip() == '':
                    novo['D'] = 'vazia'
                if novo != {}:
                    retorno['opcoes'] = novo
    if 'correta' in questao:
        if questao['correta'] != 'A' and questao['correta'] != 'B' and questao['correta'] != 'C' and questao['correta'] != 'D':
            retorno['correta'] = 'valor_errado'
    return retorno

def valida_questoes(lista):
    newlist = []
    for questao in lista:
        newlist.append(valida_questao(questao))
    return newlist

def sorteia_questao(dic, nivel):
    if nivel in dic:
        questoes = dic[nivel]
        a = random.choice(questoes)
    return a

def sorteia_questao_inedida(dic, nivel, lista):
    a = sorteia_questao(dic, nivel)
    while a in lista:
        a = sorteia_questao(dic, nivel)
    lista.append(a)
    return a

def questao_para_texto(dicionario, n):
    x = f'''----------------------------------------
QUESTAO {n}

{dicionario['titulo']}

RESPOSTAS:
A: {dicionario['opcoes']['A']}
B: {dicionario['opcoes']['B']}
C: {dicionario['opcoes']['C']}
D: {dicionario['opcoes']['D']}'''
    return x

def gera_ajuda(questao):
    correta = questao['correta']
    lista = [questao['opcoes']['A'], questao['opcoes']['B'], questao['opcoes']['C'], questao['opcoes']['D']]
    y = lista.index(questao['opcoes'][correta])
    del lista[y]
    x = random.randint(1,2)
    if x == 1:
        a = random.choice(lista)
        return f'DICA:\nOpções certamente erradas: {a}'
    if x == 2:
        a = random.choice(lista)
        y = lista.index(a)
        del lista[y]
        b = random.choice(lista)
        return f'DICA:\nOpções certamente erradas: {a} | {b}'
