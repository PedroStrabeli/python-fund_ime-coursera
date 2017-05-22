import re

###################### GIVEN METHODS ##############################
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))


    # return [4.79, 0.72, 0.56, 80.5, 2.5, 31.6] #mockado
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos
    # return ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', 
    # 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
    # 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    partialSum=0
    for i in range(len(as_a)):
        partialSum += abs(as_a[i]-as_b[i])
    return partialSum/len(as_a)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [calculatewal(texto), calculatettr(texto), calculatehlr(texto), calculatesal(texto), calculatesac(texto), calculatepal(texto)]

def avalia_textos(textos, ass_cp):
    calculados = CalculateSignatures(textos)
    mapper = dict()
    for i in range(len(calculados)):
        mapper[i+1]=compara_assinatura(calculados[i], ass_cp)
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    return min(mapper, key = mapper.get)


################## COMPLEMENTARY METHODS ####################

def TrimWord(word):
    newWord = word;
    for i in word:
            if i in [',', '.','?','!',':',';']:
                newWord = newWord.replace(i, '')
    return newWord

def calculatewal(texto):
    # retorna tamanho medio de palavra
    wordList = separa_palavras(texto)
    total = 0
    for word in wordList:
        total += len(TrimWord(word).strip())

    return  total/len(wordList)

def calculatettr(texto):
    # retorna relação Type-Token
    wordList = separa_palavras(texto)
    
    return n_palavras_diferentes(wordList)/len(wordList)

def calculatehlr(texto):
    # retorna Razão Hapax Legomana
    wordList = separa_palavras(texto)
    return n_palavras_unicas(wordList)/len(wordList)

def calculatesal(texto):
    # retorna tamanho médio de sentença
    sentenceList = separa_sentencas(texto)
    total = 0
    for s in sentenceList:
        total += len(s.strip())
    return total/len(texto)

def calculatesac(texto):
    # retorna complexidade média da sentença
    return len(separa_frases(texto))/len(separa_sentencas(texto))

def calculatepal(texto):
    # retorna tamanho medio de frase
    phraseList = separa_frases(texto)
    total = 0
    for word in phraseList:
        total += len(word.strip())

    return  total/len(phraseList)

def CalculateSignatures(texts):
    chaves = []
    for text in texts:
        chaves.append(calcula_assinatura(text))
    return chaves

########################################################################



def main():
    params = le_assinatura()
    textos = le_textos()

    infectado = avalia_textos(textos, params)
    print("O autor do texto", infectado, "está infectado com COH-PIAH")

main()
