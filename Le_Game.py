from random import *
import json
 
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
specialWords = ['pulo', '50', 'plat', 'plateia', 'uni', 'universitarios', 'parar', 'skip', 'pular', '50|50', 'metade', 'stop', 'para', 'eliminar', 'elemina']
stopWords = ['stop', 'parar', 'para']
platWords = ['plat', 'plateia']
cinWords = ['metade', '50', '50|50', 'eliminar', 'elemina']
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
            print(f"Found correct answer {inco[num]} on index {num} letters {letters[num]}")
            return letters[num], inco
        num += 1

#ChooseCorrect(0)
    
#Show questions test
##Arg:answers => the list of answers
def ShowQuestions(answers, how = 'default'):
    num = 0
    print(f"Pergunta numero {num + 1}")
    if(how == 'default'):
        for i in answers:
            print(f"{letters[num]}---{i}\n")
            num += 1
    elif(how == 'uni'):
        print(0)
    

    
#Get answer for question
##Arg: num => question number
###Todo add special case in show question
def GetAnswer(num):
    correct, answers = ChooseCorrect(num)
    ShowQuestions(answers)
    isAnswering = True
    inSpecialCase = False
    while(isAnswering):
        userInput = input("Digite sua resposta\n")
        userInput.lower()
        if(userInput in specialWords):
            print("Especial")
            inSpecialCase = True
            while(inSpecialCase):
                ShowQuestions(answers, detectCase(userInput))
            isAnswering = False
        elif(userInput in letters):
            if(userInput == correct):
                print("Correct")
                player["Quantidade_de_pontos"] += 100
                isAnswering = False
            else:
                print("Incorreto")
                player["Quantidade_de_pontos"] -= 100
                isAnswering = False
        else:
            print("Input invalido")

    print(1)
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
    totalQuestion = len(data["questions"])
    gameIsPlaying = False
    listOfQuestions = ArrayGenerator(totalQuestion)
    ShuffleArray(listOfQuestions)
    gameIsPlaying = True
    playerNick = input("Digite seu nome!\n")
    player["Nome_do_jogador"] = playerNick
    if(playerNick == ""):
        player["Nome_do_jogador"] = "Gamer"
    num = 0
    rounds = 0
    while(gameIsPlaying):
        GetAnswer(listOfQuestions[num])
        rounds += 1
        num += 1
        print(player["Quantidade_de_pontos"])
        if(rounds >= totalQuestion):
            break
    SaveResults()
   

#Main()
 

def batata():
    print(23)

    
 
# #List de numeros de questoes no jogo
# questionNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# #Randomicamente embaralha a lista
# shuffle(questionNum)
# print(questionNum)