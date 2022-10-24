# MANAUAL DE CODIGO
# 1.Imports
```Python
import json
from random import *
from time import *
from collections import Counter
```
Importa json, para ler o arquivo das perguntas o question.json

Importa tudo da livraria random e time, para numeros aleatorios e para adcionar delay

Importa Counter da livraria collections, para contar on numero de itens em um dicionario
# 2. Variaveis globais

```Python
1-letters = ['a', 'b', 'c', 'd']
2-specialWords = ['pulo', '50', 'plat', 'plateia', 'uni', 'universitarios', 'parar', 'skip', 'pular', '50|50', 'metade', 'stop', 'para', 'eliminar', 'elimina']
3-stopWords = ['stop', 'parar', 'para']
4-platWords = ['plat', 'plateia']
5-cinWords = ['metade', '50', '50|50', 'eliminar', 'elimina']
6-uniWords = ['uni', 'universitarios']
7-skipWords = ['pular', 'pula', 'skip', 'pulo']
8-totalJumps = 0
9-total50 = 0
10-totalUni = 0
11-totalPlat = 0
12-totalPoints = 0
13-playerNick = ""

```
## Da linha 1 a 7, as variaveis sao responsaveis para comparar a resposta dada para o Jogador!

## Da linha 8 a 13, serao as responsaveis por pegar o nome do Jogador e acompanhar quantos pontos e power ups usados!
# 3. Dicionarios
```Python
Streaks = {
    "Posstreak": 0,
    "Negstreak": 0,
}

player = {
    "Quantidade_de_pontos": totalPoints,
    "Pulos_usados" : totalJumps,
    "50|50_usados": totalJumps,
    "Universitarios_usados": totalUni,
    "Plateias_usadas": totalUni,
    "Nome_do_jogador": playerNick,
}

```
## Dicionario Streaks eh responsavel por acampanhar quantas erradas ou acertos consecutivos o jogador tem!

## Dicionario player eh responsavel por guardar o nome do jogador, total de pontos e total de power ups usados

# 4. Lendo as perguntas e respostas por um arquivo .json
```Python
1-file = open('questions.json', encoding="utf8", errors="ignore")
2-data = json.load(file)
```

## Primeira linha abre o arquivo das perguntas, codifica para utf-8 e ignora erros se encontrar algum na hora da leitura.
## Segunda linha 'analisa' o arquivo inteiro e salva
### Assim, se pode ler o arquivo usando 
```Python
print(data["questions"])
#printa o arquivo questions.json inteiro

print(data["questions"][0])
#Prita primeira questao
```

# 5. Funcoes

## 5.1 ChooseCorrect()

## Descricao
Dado o id da questao retorna a letra correta e uma lista de todas as respostas!


## Syntax
ChooseCorrect(int n)

## Parametros

n - um numero inteiro, que corresponde ao id da questao

## Retorno

Retorna uma string e uma lista

## Exemplo:

```Python
print(ChooseCorrect(1))
#('b', ['Nao', 'Sim', 'TOGURO?', 'Nao sei'])
```

## 5.2 printdots()

## Descricao
Espera 1 segundo e printa um '.' repete 3 vezes

## Syntax
printdots()

## Exemplo:
```Python
printdots()
'''
#Espera 1 segundo
.
#Espera 1 segundo
.
#Espera 1 segundo
.
#Espera 1 segundo
'''
```

## 5.3 ShowQuestions()

## Descricao

Printa a pergunta e suas respostas, enumerando elas baseada no round atual

## Syntax

ShowQuestions(lista(answers), int rounds, int ques)

## Parametros

answers - Lista com todoas as respostas

rounds - round atual

ques - questao atual


## Exemplo 

```Python
questao = 1
correct, respostas = ChooseCorrect(questao)
ShowQuestions(respostas, 5, questao)
'''
______________________________________________
        Pergunta numero 5
______________________________________________
.
.
.
        P5--Conhece Elon musk?
______________________________________________
        Q1--a---Nao
______________________________________________
______________________________________________
        Q2--b---Nao sei
______________________________________________
______________________________________________
        Q3--c---TOGURO?
______________________________________________
______________________________________________
        Q4--d---Sim
______________________________________________
______________________________________________
'''
```
## 5.4 fiftyfifty()

## Descricao

Elemina duas respostas erradas!

## Syntax

fiftyfifty(Lista(answers), string correct)

## Parametros

answers - Lista com todas as respostas

correct - String da resposta certa


## Exemplo :
```Python
questao = 1
correct, respostas = ChooseCorrect(questao)
ShowQuestions(respostas, 5, questao)
'''
______________________________________________
        Pergunta numero 1
______________________________________________
.
.
.
        P1--Conhece Elon musk?
______________________________________________
        Q1--a---Sim
______________________________________________
______________________________________________
        Q2--b---Nao
______________________________________________
______________________________________________
        Q3--c---TOGURO?
______________________________________________
______________________________________________
        Q4--d---Nao sei
______________________________________________
______________________________________________
'''
fiftyfifty(respostas, correct)
'''
Q1--a---Sim
Q2--c---TOGURO?
'''
```

## 5.5 DoPorcentage()

## Descricao

Calcula uma porcentagem bem nas 'coxas'
Eh bem nas coxa pois nao calcula realmente a porcentagem dos intens em um dicionario
apenas conta o numero de itens e da uma porcentagem baseado nisso

## Syntax 

PlatCalculation(Lista(Arr1), Lista(arr2), string how)


## Parametros

Arr1 - Lista 1 

Arr2 - Lista 2

how - como sera feito o calculo => somente 'uni' e 'plat' fazem algo, 20 e 10 respectivamentes


## Retorna

Retorna um dicionario com as porcentagem

## 5.6 PlatCalculation()


## Descricao

Apesar do nome, essa funcao calcula a porcentagem da plateia e dos universitarios
O calculo da porcentagem eh feito pela funcao DoPorcentage()

## Syntax

PlatCalculation(Lista(answers), string correct, int peps, string how, float num1, float num2, )

## Parametros

answers - Lista de respostas

correct - Letra correta

num1 e num2(Opcional) - Ambos ajudam no calculo de escolher respostas de ambos o universitarios e a plateia| sempre menores que 
num2 - age como uma segunda chance, valor default = 0

peps - Quantidades de pessoas, se traduz na quantidade de vezes que sera loopado.

how - como mostrado o resultado final

## Exemplo :
```Python
correct, respostas = ChooseCorrect(questao)
PlatCalculation(respostas, correct, 0.3, 0.2, 10, 'plat')
#A plateia votou nas seguinte questoes {'a': '30%', 'b': '30%', 'c': '20%', 'd': '20%'}

```
## 5.7 ShowQuestionVar()

## Descricao

Mostra as questoes de maneiras diferente, baseados no 50|50, plateia e universitarios

## Syntax

ShowQuestionVar(Lista(answers), string how, int ques)

## Parametros

answers - Lista de respostas

how - Qual versao mostrar| plat, 50 e uni

ques - id da questao atual


## Modo de funcionar

how =  'plat' -> Chama funcao PlatCalculation()

how = 'uni' -> Chama funcao PlatCalculation()

how = '50' -> Chama funcao fiftyfifty()


## 5.8 detectCase()

## Descricao

Baseado no input do jogador, detecta se eh uma palavra especial

## Syntax

detectCase(string word)

## Parametros

word - palavra a ser analisada

## Retorno

Retorna 'skip' se o input esta em skipWords

Retorna 'uni' se o input esta em uniWords

Retorna 'stop' se o input esta em stopWords

Retorna 'plat' se o input esta em platWords

Retorna 'cin' se o input esta em cinWords

## Exemplo:

```Python
print(detectCase('plat'))
#plat
```

## 5.9 CalcPoints()

## Descricao
Calcula a pontuacao do jogador
a formula eh dada por round(rounds**2 + 100/2)

## Syntax 

CalcPoints(int rounds, string sign, int streak)

## Parametros

rounds - round atual

sign - + ou - em string, para saber se o resultado eh positivo ou negativo

streak - quantidades de acertos ou erros consecutivos desde o ultimo acerto/erro

## Retorno

se sign = '+' -> Retorna round(formula * streak / 1.7)

se sign = '-' -> round(-formula * streak / 1.3)

## Exemplo 

```Python

print(CalcPoints(5, '-', 4))
#-231

```


## 5.10 GetAnswer()

## Descricao

Pega a resposta do jogador para a pergunta sendo perguntada

## Syntax

GetAnswer(int num, int rounds)

## Parametros

num - id da questao

rounds - round atual

## 5.11 ArrayGenerator()

## Descricao

Gera Lista entre 0 e o tamanho especificado

## Syntax 

ArrayGenerator(int n)

## Parametros

n - tamanho da lista a ser gerada

## Retorno

Retorna a lista criada

## Exemplo:

```Python
print(ArrayGenerator(5))
#[0, 1, 2, 3, 4]

```

## 5.12 ShuffleArray()

## Descricao

Embaralha uma lista

## Syntax

ShuffleArray(list(arr))

## Parametros

arr - Lista a ser embaralhada

## Retorno 

retorna a lista embaralhada

## Exemplo:

```Python
print(ShuffleArray([0, 1, 2, 3, 4]))
#[3, 2, 0, 1, 4]
```

## 5.13 SaveResults()

## Descricao

Cria ou atualiza um arquivo data.json caso nao exista e salva a dicionario player nele


# 6. Funcao Main()


**Essa eh a funcao que sera chamada para iniciar o jogo.**

Depende de todas as outras funcoes anteriores

```Python
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
        print(f"Voce tem: {player['Quantidade_de_pontos']} pontos!")
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
```




