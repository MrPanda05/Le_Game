import React from 'react'
import { Link } from 'react-router-dom'

const Header = () => {
  return (
    <header className='bg-emerald-600 py-12 rounded-lg mx-2 my-2'>
        <h1 className='text-center'>
          <Link to='/'>JOGO PRO</Link>
        </h1>
    </header>
  )
}

export default Header