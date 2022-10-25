import React from 'react'
import { Helmet } from 'react-helmet-async'

const API = () => {
  return (
    <div>
      <Helmet>
        <title>Manual do Código!</title>
      </Helmet>
      <div className='text-center bg-teal-300 rounded-xl mx-1 my-2 py-2'>
        <h1 className='font-semibold text-4xl'>Baixe o manual em pdf <span className='text-teal-900'><a href='Codigo.pdf' download>Aquii!</a></span></h1>
      </div>
      <div className='text-center font-semibold bg-teal-100 rounded-xl mx-1 my-2 py-4'>
        Flow chart do programa do Jogão do Bacalhau
      </div>
      <div className='flex justify-center my-3'>
        <img src='/img/Le_GameFlowChart.png' alt='FlowChart'/>
      </div>
    </div>
  )
}

export default API