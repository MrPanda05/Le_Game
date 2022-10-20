import json
from random import *
from time import *
import os
from collections import Counter
'''
    Gdd jogo copia do show do milhao
 
    Deve ter
    1- Minimo de 15 perguntas
    2- Cada pergunta deve ter 4 perguntas, uma sera correta
    3- A cada pergunta, o jogador deve ter a opçao de escolher
    uma das opções ou parar
    4- Dever ter uma forma de pontuação
    5- Caso escolher parar, a pontuação deverar permanencer a mesma
    5.1- Caso falhe, a pontuação deve decrescer um pouco
    5.2- Pode haver mais estrategias de pontuação
    6- Deverão ter "power ups"
    6.1- Pulo-pula uma questao, somente usado uma vez
    6.2- 50|50- remove metade das questoes erradas, somente 2 usos
    6.3- Plateia- 10 opçoes sorteadas da plateia, cada opçao com 30% de chance
    de estarcorreta, 2 usos
    6.4- Universitarios,5 opções sorteadas, cada opçao com 50% de certeza, 2 usos
    7- Dois manuais
    7.1- Manual de usuario, como jogar o jogo, suas regras e tal
    7.2- Manual de api, oque cada funcao, codigo faz
'''
'''
    Leitura de comentarios Guia!
    #!Descricao rapida
    ##-Arg descreve os asgumentos de uma funcao
    ###-oq retorna
    #?-Descricao mais detalhada
    As explicacoes de algoritimo da funcao serao dadas em comentarios multilinhas
'''

#1-Variaveis globais
#!Variaveis que todo o codigo usa
#?identificacao de input do usuario
letters = ['a', 'b', 'c', 'd']
specialWords = ['pulo', '50', 'plat', 'plateia', 'uni', 'universitarios', 'parar', 'skip', 'pular', '50|50', 'metade', 'stop', 'para', 'eliminar', 'elimina']
stopWords = ['stop', 'parar', 'para']
platWords = ['plat', 'plateia']
cinWords = ['metade', '50', '50|50', 'eliminar', 'elimina']
uniWords = ['uni', 'universitarios']
skipWords = ['pular', 'pula', 'skip', 'pulo']
#?Reseta todas as variaveis de powerups usados
totalJumps = 0
total50 = 0
totalUni = 0
totalPlat = 0
totalPoints = 0
playerNick = ""

#2-Dicionario do player
#!Highscore que sera salvo em outro arquivo
#?Essas informacoes sao usadas no arquivo pra saber se o usuario usou algun powerups, salva os pontos e sera usada para o highscore
player = {
    "Quantidade_de_pontos": totalPoints,
    "Pulos_usados" : totalJumps,
    "50|50_usados": totalJumps,
    "Universitarios_usados": totalUni,
    "Plateias_usadas": totalUni,
    "Nome_do_jogador": playerNick,
}

#3-Json
#!Abre o json com as questoes e o le
file = open('questions.json', encoding="utf8", errors="ignore")
data = json.load(file)
#Leitura do json. data["questions"][n]
#n eh para qual questao deve ser lida



#4-Funcoes
#!Escolhe uma resposta correta
##Arg: n => O id da questao do .json
###Retorna uma letra e uma lista com as respostas toda embaralhadas

def ChooseCorrect(n):
    '''
        1-Declara uma variavel correta que recebe aa resposta certa do .json baseada em n
        2-faz a mesma coisa da anterios so que com as incorretas
        3-junta a resposta certa, com a lista de resposta errada
        3-1Ex: Certa = [y1]
        incorretas = [x1,x2,x3]
        dps => [x1,x2,x3,y1]
        4-Embaralha a lista toda
        5-Loppa pela lista, se achar a correta retorna
    '''
    correct = data["questions"][n]["correct"]
    inco = data["questions"][n]["inco"]
    inco.append(data["questions"][n]["correct"])
    shuffle(inco)
    num = 0
    for i in inco:
        if(i == correct):
            #print(f"Found correct answer {inco[num]} on index {num} letters {letters[num]}")
            return letters[num], inco
        num += 1

#!Printa 3 pontos em um intervalo de 1 segundo cada
def printdots():
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    
#!Mostra as questoes no terminal
#?Essa eh a primeira coisa que aparecera quando um nova pergunta for dada
##Arg:answers => Lista de respostas | rounds => O round atual | ques => A questao atual
def ShowQuestions(answers, rounds, ques):
    '''
        1-Pega o nome da questao
        2-printa a UI
        3-Loppa pela lista de resposta e printa cada uma das respostas
    '''
    num = 0
    questionName = data["questions"][ques]["name"]
    print('______________________________________________')
    print(f"\tPergunta numero {rounds}")
    print('______________________________________________')
    printdots()
    print(f"\tP{rounds}--{questionName}")
    print('______________________________________________')
    for i in answers:
        print(f"\tQ{num + 1}--{letters[num]}---{i}")
        sleep(1)
        print('______________________________________________\n______________________________________________')
        num += 1

#!Mostra 1 certa e outra errada
#?Usado quando usuario usa o commando 50|50
##Arg: answers => Lista de resposta | correct => resposta certa
def fiftyfifty(answers, correct):
    '''
        1-Acha o index da resposta certa na lista de respostas
        2-Checa qual index que eh
        2-1-Baseado no index, ele checa em qual ordem se deve printar as respostas, sempre gerando um novo numero inteiro
    '''
    index = answers.index(correct)
    print(index)
    if(index == 0):
        num = randint(1, 3)
        print(f"\tQ{1}--{letters[index]}---{correct}")
        print(f"\tQ{2}--{letters[num]}---{answers[num]}")
    elif(index == 1):
        num = choice([i for i in range (0, 3) if i not in [1]])
        if(num < 1):
            print(f"\tQ{1}--{letters[num]}---{answers[num]}")
            print(f"\tQ{2}--{letters[index]}---{correct}")
        else:
            print(f"\tQ{1}--{letters[index]}---{correct}")
            print(f"\tQ{2}--{letters[num]}---{answers[num]}")
    elif(index == 2):
        num = choice([i for i in range (0, 3) if i not in [2]])
        if(num < 2):
            print(f"\tQ{1}--{letters[num]}---{answers[num]}")
            print(f"\tQ{2}--{letters[index]}---{correct}")
        else:
            print(f"\tQ{1}--{letters[index]}---{correct}")
            print(f"\tQ{2}--{letters[num]}---{answers[num]}")
    else:
        num = randint(1, 2)
        print(f"\tQ{1}--{letters[num]}---{answers[num]}")
        print(f"\tQ{2}--{letters[index]}---{correct}")

#!Calcula a porcentagem
#? O calculo eh difirente baseado no input do jogador
##Arg: arr1 e arr2 => Lista comuns | how => Como o calcula de porcentagem deve ser feito
###Retorna A lista de porcentagem de cada elemento
def DoPorcentage(arr1, arr2, how):
    '''
        1-Transforma em dicionario arr1 e arr2
        2-Conta quantos elementos iguas ha em cada um
        3-Junta os dois dicionarios
        4-Conta novamente quantos elementos ha na juncao de ambos
        5-Baseado no how, define como a porcentagem deve ser feita
        5-1-Se for universitarios, o valor eh 20
        5-2-Se for plateia, o valor eh 10
        6-retorna o Dicionario ja em porcentagem
    '''
    dic1 = dict(Counter(arr1))
    dic2 = dict(Counter(arr2))
    z = {**dic1, **dic2}
    listed = dict(Counter(z))
    #print(listed)
    if(how == 'uni'):
        for i in listed:
            listed[i] *= 20
            listed[i] = f"{listed[i]}%"
    elif(how == 'plat'):
        for i in listed:
            listed[i] *= 10
            listed[i] = f"{listed[i]}%"
        

    return listed
        

#!Faz o calculo de plateia e universitarios
#?Originalmente era apenas para plateia
##Arg: answers => Lista de respostas | correct => correta
##Arg: num 1 e num2 => numeros que ajudam no calculo
##Arg: peps: Quantidade de pessoas | how => se eh universitarios ou plateia
def PlatCalculation(answers, correct, num1, num2, peps, how):
    '''
        1-Acha o index da correta
        2-declara um inteiro que sera usado para o loop
        3-Enquanto o inteiro for menor que o numero de pessoas
        3-1- adciona 1 ao inteiro
        3-2-Gera um numero entre 0 e 1
        3.3- Se o rng for menor que num1, adciona a letra da correta em uma lista
        3.4-Se nao, repete o passo 3.3, mas agora com num2, se nao adciona a letra errada no arr2
        3-5-repete ate que o inteiro for maior ou igual ao numero de pessoas
        4-Calcula a porcentagem, usando a funcao anterior
        5-printa baseado no how
    '''
    index = answers.index(correct)
    arr1 = []
    arr2 = []
    ints = 0
    while(ints < peps):
        ints += 1
        num = random()
        if(num <= num1):
            arr1.append(letters[index])
        else:
            num = random()
            if(num <= num2):
                arr1.append(letters[index])
            else:
                arr2.append(letters[choice([i for i in range (0, 4) if i not in [index]])])
                
    
    #print(f"arr1 {arr1}")
    #print(f"arr2 {arr2}")
    x = DoPorcentage(arr1, arr2, how)
    if(how == 'plat'):
        print(f"A plateia votou nas seguinte questoes {x}")
    elif(how == 'uni'):
        print(f"Os universitarios votaram nas seguinte questoes {x}")
            
        




#!Mostra as perguntas baseadas no powerups utilizado
##Arg: answers => lista de respostas| how => Como se deve mostrar | ques => atual questao
def ShowQuestionVar(answers, how,ques):
    correct = data["questions"][ques]["correct"]
    if(how == 'cin'):
        fiftyfifty(answers, correct)
    elif(how == 'plat'):
        PlatCalculation(answers, correct, 0.3, 0.2, 10, how)
    elif(how == 'uni'):
        PlatCalculation(answers, correct, 0.5, -5, 5, how)
            


#!Acha qual powerup foi usado
def detectCase(word):
    word.lower()
    if(word in skipWords):
        return 'skip'
    if(word in uniWords):
        return 'uni'
    if(word in stopWords):
        return 'stop'
    if(word in platWords):
        return 'plat'
    if(word in cinWords):
        return 'cin'
    
#!Recebe o input da questao e checka se esta certa
##Arg: num => numero da questao | rounds => o round atual
###Todo add special case in show question
def GetAnswer(num, rounds):
    '''
        ma nem fudend oque vo explica essa kkkkkkkk
    '''
    correct, answers = ChooseCorrect(num)
    id = data["questions"][num]["id"]
    ShowQuestions(answers, rounds, num)
    isAnswering = True
    inSpecialCase = False
    while(isAnswering):
        userInput = input("Digite sua resposta\n").lower()
        if(userInput in specialWords):
            print("Especial")
            caseSpecial = detectCase(userInput)
            inSpecialCase = True
            while(inSpecialCase):
                if(caseSpecial == 'stop'):
                    inSpecialCase = False
                    isAnswering = False
                    return "STOP"
                elif(caseSpecial == 'skip'):
                    if(player['Pulos_usados'] == 1):
                        print("Voce esgotou todos os seus pulos!")
                        inSpecialCase = False
                    else:
                        inSpecialCase = False
                        isAnswering = False
                        player['Pulos_usados'] += 1
                        return "SKIP"
                elif(caseSpecial == 'cin'):
                    if(player['50|50_usados'] == 2):
                        print("Voce gastou todas os seus usos de 50|50!")
                        inSpecialCase = False
                    else:
                        ShowQuestionVar(answers, 'cin', num)
                        player['50|50_usados'] += 1
                        inSpecialCase = False
                elif(caseSpecial == 'plat'):
                    if(player['Plateias_usadas'] == 2):
                        print("Voce gastou todas os seus usos da plateia!")
                        inSpecialCase = False
                    else:
                        ShowQuestionVar(answers, 'plat',num)
                        player['Plateias_usadas'] += 1
                        inSpecialCase = False
                elif(caseSpecial == 'uni'):
                    if(player['Universitarios_usados'] == 2):
                        print("Voce gastou todas os seus usos de universitarios!")
                        inSpecialCase = False
                    else:
                        ShowQuestionVar(answers, 'uni',num)
                        player['Universitarios_usados'] += 1
                        inSpecialCase = False
                #ShowQuestionVar(answers, caseSpecial)
        elif(userInput in letters):
            if(userInput == correct):
                printdots()
                print("Resposta certa!")
                sleep(1)
                player["Quantidade_de_pontos"] += 100
                isAnswering = False
            else:
                printdots()
                print("Errou!!")
                sleep(1)
                player["Quantidade_de_pontos"] -= 100
                isAnswering = False
        else:
            print("Input invalido")

    #print(1)

    
#!Cria uma lista com n intens dentro
##Arg: n => tamanho da lista
###Retorna a lista
def ArrayGenerator(n):
    arr = []
    #Loops and adds i to array
    for i in range(0,n):
        arr.append(i)
    return arr
 
#!Embaralha a lista
##Arg: arr => lista para ser embaralhada
###Retorna a lista
def ShuffleArray(arr):
    shuffle(arr)
    return arr
 

#Make a special question case
#if num is divisible by 5
def SpecialQuestion():
    newArr = ShuffleArray()
    oldArr = []
    for i in range(0, len(newArr)):
        if(newArr[i] % 5 == 0 and newArr[i] != 0):
            oldArr.insert(i, newArr[i])
    return oldArr


#!Salva o score do player em um json
def SaveResults():
    with open('data.json', 'w') as outfile:
        json.dump(player, outfile, indent=4)

#!O jogo inteiro sera rodado aqui dentro
def Main():
    num = 0
    totalQuestion = len(data["questions"])
    gameIsPlaying = False
    listOfQuestions = ArrayGenerator(totalQuestion)
    ShuffleArray(listOfQuestions)
    gameIsPlaying = True
    playerNick = input("Digite seu nome!\n")
    player["Nome_do_jogador"] = playerNick
    if(playerNick == ""):
        player["Nome_do_jogador"] = "Gamer"
    rounds = 1
    roundPlayed = 0
    while(gameIsPlaying):
        clause = GetAnswer(listOfQuestions[num], rounds)
        sleep(1)
        rounds += 1
        roundPlayed += 1
        num += 1
        print(player["Quantidade_de_pontos"])
        if(clause == 'STOP'):
            print("Voce escolheu parar")
            break
        elif(clause == 'SKIP'):
            print("Voce Pulou a questao")
        if(roundPlayed >= totalQuestion):
            print("Acabou!!")
            break
    SaveResults()
   

Main()


def printtest():
    anim = [" O\n/|\\\n |\n/ \\", " O\n/|/\n |\n/ \\"]
    canvas = ""
    for i in anim:
        canvas = i
        print(f"\r{canvas}")

 
# #List de numeros de questoes no jogo
# questionNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# #Randomicamente embaralha a lista
# shuffle(questionNum)
# print(questionNum)