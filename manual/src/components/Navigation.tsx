import React from 'react'
import { Link } from 'react-router-dom';

const Navigation = () => {
  return (
    <div className="grid grid-cols-3 gap-5 flex-auto text-center mx-2 my-2 bg-green-400 rounded-lg py-5">
      <Link to="/manual-de-jogador" className='mx-2 hover:bg-green-600 rounded-lg py-2'>Manual de jogador</Link>
      <Link to="/manual-de-codigo" className='mx-2 hover:bg-green-600 rounded-lg py-2'>Manual de Codigo</Link>
      <Link to="/codigo-fonte" className='mx-2 hover:bg-green-600 rounded-lg py-2'>Codigo fonte</Link>
    </div>
  )
}

export default Navigation