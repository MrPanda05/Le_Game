import React from 'react'
import { Helmet } from 'react-helmet-async'
const Player = () => {
  return (
  <div>
      <Helmet>
        <title>
          Manual de Jogador!
        </title>
      </Helmet>
      <div className='text-center bg-teal-300 rounded-xl mx-1 my-2 py-2'>
          <h1 className='font-semibold text-4xl'>
            Manual do Jogador!
          </h1>
        </div>
      <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Como rodar esse jogao!</h1>
          <div className='font-medium text-lg mx-1'>
            <ol className='list-decimal mx-8'>
              <li>
              Baixe o Zip <span className='text-xl text-rose-900'><a href='Le_Game.zip' download>Aquii!</a></span>
              </li>
              <li>
              Unzipa
              </li>
              <li>
              Abra o arquivo Le_Game.py
              </li>
              <li>
              Execute o arquivo
              </li>
              <li>
                Baixe o manual em pdf <span className='text-xl text-rose-900'><a href='Jogador.pdf' download>Aquii!</a></span>
              </li>
            </ol>
          </div>
    </div>
    <div className='bg-blue-200 my-1 py-3 mx-2 rounded-md'>
          <h1 className='font-bold text-xl mx-1'>Como jogar?</h1>
          <div className='font-medium text-lg mx-1'>
            <ul className='list-disc mx-8'>
                <li>
                   Nesse jogão, você deverar responder todas as perguntas, quanto mais acertos e quantos mais rodadas jogadas você poderar
                   ganhar ou perder!!<br/>
                </li>
                <li>
                  Você deverar escolher entre as respostas <strong>A, B, C e D</strong><br/>
                </li>
                <li>
                  Você, tambem podera usar alguns tipos de power ups ou parar.<br/>
                </li>
                <li>
                  Para receber os power ups, basta digitar o comando no terminal, os comandos estao na tabela abaixo<br/>
                </li>
                <li>
                 Após o termino do jogo, você poderar joga-lo novamente apenas rodando o arquivo novamente!<br/>
                </li>
          </ul>
        </div>
  </div>
  <div className='text-center bg-teal-400 rounded-xl mx-1 my-2 py-2'>
      <h1 className='font-semibold text-2xl'>
            Power ups
      </h1>
  </div>
  <div className=' flex text-center rounded-xl my-2 py-2 items-center justify-center place-content-center mx-2'>
  <table className="border-collapse border border-slate-500  table-auto border-spacing-2 text-center justify-center rounded-xl">
  <thead>
    <tr className='mx-5 bg-slate-300'>
      <th className='border-2 border-slate-600'>Comando</th>
      <th className='border-2 border-slate-600'>Descricão</th>
      <th className='border-2 border-slate-600'>Usos</th>
    </tr>
  </thead>
  <tbody>
    <tr className='mx-5'>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Parar</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Para de jogar</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>1</td>
    </tr>
    <tr className='mx-5 bg-slate-300'>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Pular</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Pula a questão atual</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>1</td>
    </tr>
    <tr className='mx-5'>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>50</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Elimina 2 respostas</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>2</td>
    </tr>
    <tr className='mx-5 bg-slate-300'>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Universitarios</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Os universitários escolheram algumas resposta</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>2</td>
    </tr>
    <tr className='mx-5'>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>Plateia</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>A plateia escolherá algumas respostas</td>
      <td className='border-2 border-slate-700 pl-5 pr-5 font-semibold'>2</td>
    </tr>
  </tbody>
</table>
  </div>
  </div>
  )
}

export default Player