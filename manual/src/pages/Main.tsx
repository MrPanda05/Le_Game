import React from 'react'
import { Helmet } from 'react-helmet-async';

const Main = () => {
  return (
    <div>
      <Helmet>
        <title>JOGAO DO BACALHAU</title>
      </Helmet>
        <div className='text-center bg-teal-300 rounded-xl mx-1 my-2 py-2'>
          <h1 className='font-semibold text-4xl'>
            Bem vindo ao site do Jogao do bacalhau!
          </h1>
        </div>
        <div className='text-center bg-teal-400 rounded-xl mx-1 my-2 py-2'>
          <h1 className='font-semibold text-2xl'>
            Perguntas e Repostas
          </h1>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>O que eh o jogao do bacalhau?</h1>
          <div className='font-medium text-lg mx-1'>
            O jogao do bacalhau, ou para os menos cultos entre nos, apenas jogo do bacalhau, eh um jogo de perguntas e respostas
            onde o seu objectivo eh conseguir o maior numero de pontos possivel.
          </div>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Como jogar esse jogao?</h1>
          <div className='font-medium text-lg mx-1'>
            Para jogar eh muito simples, basta baixar clickando aki <span className='text-xl text-rose-900'><a href='Le_Game.zip' download>Aki!</a></span> depois so unzipar o Le_Game.zip e por fim
            abrir o arquivo Le_Game.py e rodar
          </div>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Para quem eh esse jogao?</h1>
          <div className='font-medium text-lg mx-1'>
            O jogao do Bacalhau eh livre para todos os publicos, qualquer pessoa que tenha um computador com python instalado sera capaz
            de rodar esse belo jogao!
          </div>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Porque Bacalhau?</h1>
          <div className='font-medium text-lg mx-1'>
            Veja, se voce esta com essa pergunta, significa que voce nao eh culto o suficiente para simplismente entender a razao por tras do bacalhau, somente 
            quem sabe... sabe!
          </div>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Instalei e rodei, mas nao funcionou | Exemplo 1:</h1>
          <div className='font-medium text-lg mx-1'>
            Certifiquesse que o seu terminal esta na pasta certa, se vc unzipou e criou uma pasta no processo, ira estar mais ou menos assim.
            Por exemplo: "C:\User\Nome\Desktop\Le_Game" nesse caso. <br/>
            Use cd nomeDaPasta para avancar em uma pasta com o terminal <br/>
            Use cd .. Para voltar uma pasta. <br/>
          </div>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Instalei e rodei, mas nao funcionou | Exemplo 2:</h1>
          <div className='font-medium text-lg mx-1'>
            Certifiquesse que existe um arquivo chamado questions.json
          </div>
        </div>
        <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Instalei e rodei, mas nao funcionou | Exemplo 3:</h1>
          <div className='font-medium text-lg mx-1'>
            Certifiquesse que voce tenha python instalado
          </div>
        </div>
    </div>
  )
}

export default Main