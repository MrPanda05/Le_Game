from random import *
import json
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
 
#Global variables
letters = ['a', 'b', 'c', 'd']
specialWords = ['pulo', '50', 'plat', 'plateia', 'uni', 'universitarios', 'parar', 'skip', 'pular', '50|50', 'metade', 'stop', 'para', 'eliminar', 'elimina']
stopWords = ['stop', 'parar', 'para']
platWords = ['plat', 'plateia']
cinWords = ['metade', '50', '50|50', 'eliminar', 'elimina']
uniWords = ['uni', 'universitarios']
skipWords = ['pular', 'pula', 'skip', 'pulo']

totalJumps = 0
total50 = 0
totalUni = 0
totalPlat = 0
totalPoints = 0
playerNick = ""


player = {
    "Quantidade_de_pontos": totalPoints,
    "Pulos_usados" : totalJumps,
    "50|50_usados": totalJumps,
    "Universitarios_usados": totalUni,
    "Plateias_usadas": totalUni,
    "Nome_do_jogador": playerNick,
}

file = open('questions.json')

data = json.load(file)

#Leitura do json. data["questions"][n]
#n eh para qual questao deve ser lida
#print(data["questions"][0]["inco"][0])
#sei la
#sei la
#sei la 


#Selects the correct answer
##Arg: n => the question number from json file
### Return the correct letter and answers
def ChooseCorrect(n):
    #0:A| 1:B | 2:C | 3:D
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

#ChooseCorrect(0)

def printdots():
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    
#Show questions test
##Arg:answers => the list of answers | rounds => current round | ques => current question
def ShowQuestions(answers, rounds, ques):
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
  
def fiftyfifty(answers, correct):
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

def DoPorcentage(arr1, arr2, how):
    dic1 = dict(Counter(arr1))
    dic2 = dict(Counter(arr2))
    z = {**dic1, **dic2}
    listed = dict(Counter(z))
    print(listed)
    if(how == 'uni'):
        for i in listed:
            listed[i] *= 20
            listed[i] = f"{listed[i]}%"
    elif(how == 'plat'):
        for i in listed:
            listed[i] *= 10
            listed[i] = f"{listed[i]}%"
        

    return listed
        

#Faz o calculo da plateia e universitarios
#todoTranforma em porcentagem dps
def PlatCalculation(answers, correct, num1, num2, peps, how):
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
                
    
    print(f"arr1 {arr1}")
    print(f"arr2 {arr2}")
    x = DoPorcentage(arr1, arr2, how)
    if(how == 'plat'):
        print(f"A plateia votou nas seguinte questoes {x}")
    elif(how == 'uni'):
        print(f"Os universitarios votaram nas seguinte questoes {x}")
            
        




#Show diferent question based on special case uni, 50 and plat
##Arg: answers => the list of answers| how => how it should be shown
def ShowQuestionVar(answers, how,ques):
    correct = data["questions"][ques]["correct"]
    if(how == 'cin'):
        fiftyfifty(answers, correct)
    elif(how == 'plat'):
        PlatCalculation(answers, correct, 0.3, 0.2, 10, how)
    elif(how == 'uni'):
        PlatCalculation(answers, correct, 0.5, -5, 5, how)
            


#print(f"\tQ{num + 1}--{letter}---{correct}")
#print(f"\tQ{num + 2}--{letters[3]}---{inco}")
                
    
#Detect what special word it is
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
    
#Get answer for question
##Arg: num => question number | rounds => current round
###Todo add special case in show question
def GetAnswer(num, rounds):
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

    
#Create a random array with n numbers in it
##Arg: n => lenght of array
def ArrayGenerator(n):
    arr = []
    #Loops and adds i to array
    for i in range(0,n):
        arr.append(i)
    return arr
 
#Shuffles array
##Arg: arr => array to be shuffle
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


#Creates json file for user score
def SaveResults():
    with open('data.json', 'w') as outfile:
        json.dump(player, outfile, indent=4)

 
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