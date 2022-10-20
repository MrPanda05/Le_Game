# Repo do Jogo Do Bacalhau


## [Site do Jogo do Bacalhau!!](https://jogao-do-bacalhau.netlify.app/)
## Manual da api esta em [Manual de Codigo/Api](https://jogao-do-bacalhau.netlify.app/manual-de-codigo) ou [Aqui](https://github.com/MrPanda05/Le_Game/blob/master/Api.md)


## Manual de usuarios esta em [Manual de Jogador](https://jogao-do-bacalhau.netlify.app/manual-de-jogador) ou [Aqui](https://github.com/MrPanda05/Le_Game/blob/master/User.md)

# Como Jogar!

1. Baixe ou Clone esse repo!
    - Baixe la em Releases ou no Site oficial
2. Se baixado, unzipa
3. Abra o Le_Game.py com alguma IDE
4. Rode o arquivo!

# Considerecoes!

- O Jogo prescisa do arquivoquestions.json
> La eh onde esta todas as perguntas e respostas
> Caso voce queira fazer suas propias perguntas ou...~~[chetar](https://youtu.be/76hji9gdvOE)~~
- Quem eu to querendo enganar, claro que o jogador deste jogo eh 100% honesto e nao roubaria como alguem chamado **[Serie Sul Coreana]** afinal ***[Explicacao removida pelo Trimestral Superador Elemental]***

# Manual para criacoes de perguntas

- Use esse template a cada nova pergunta

        {
            "id": X,
            "name": "Nome da perguntas",
            "correct": "Resposta correta",
            "inco":
            [
                "Resposta errada1",
                "Resposta errada2",
                "Resposta errada3"
            ]
        }

## Tabela sobre o template

| Variavel | Tipo | Descricao|
| --- | --- | --- |
| id | Inteiro | Id da pergunta |
| name | String | Nome da pergunta |
| correct | String | Resposta correta |
| inco | List(String) | Lista de resposta erradas |