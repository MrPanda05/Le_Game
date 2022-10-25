import React from 'react'
import { Link } from 'react-router-dom';

const Navigation = () => {
  return (
    <div className="grid grid-cols-3 gap-5 flex-auto text-center mx-2 my-2 bg-green-400 rounded-lg py-5">
      <Link to="/manual-de-jogador" className='mx-2 hover:bg-green-600 rounded-lg py-2'><p className='font-semibold'>Manual de Jogador</p></Link>
      <Link to="/manual-de-codigo" className='mx-2 hover:bg-green-600 rounded-lg py-2'><p className='font-semibold'>Manual de Código</p></Link>
      <Link to="/codigo-fonte" className='mx-2 hover:bg-green-600 rounded-lg py-2'><p className='font-semibold'>Código fonte</p></Link>
    </div>
  )
}

export default Navigation