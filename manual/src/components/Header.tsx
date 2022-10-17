import React from 'react'
import { Link } from 'react-router-dom'

const Header = () => {
  return (
    <header className='bg-emerald-600 py-12 rounded-lg mx-2 my-2'>
        <h1 className='text-center'>
          <Link to='/' className='font-semibold font-mono text-2xl'>JOGAO DO BACALHAU</Link>
        </h1>
        <div className='grid grid-cols-3 gap-5 flex-auto'>
          <img src='/img/cod.png' alt='bacalhau.png' width="400" height="300" className='text-center hover:animate-spin'/>
          <img src='/img/cod.png' alt='bacalhau.png' width="400" height="300" className='text-center hover:animate-spin'/>
          <img src='/img/cod.png' alt='bacalhau.png' width="400" height="300" className='text-center hover:animate-spin'/>
        </div>
    </header>
  )
}

export default Header