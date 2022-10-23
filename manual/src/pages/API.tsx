import React from 'react'
import { Helmet } from 'react-helmet-async'

const API = () => {
  return (
    <div>
      <Helmet>
        <title>Manual do Código!</title>
      </Helmet>
      <div className='flex justify-center my-3'>
        <img src='/img/Le_GameFlowChart.png' alt='FlowChart'/>
      </div>
    </div>
  )
}

export default API