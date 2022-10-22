import React from 'react'
import { Helmet } from 'react-helmet-async'
const Source = () => {
  return (
    <div>
      <Helmet>
        <title>Codigo fonte</title>
      </Helmet>
      <div>
        <h1>O codigo fonte do jogao do bacalhau pode ser encontrado no github!</h1>
      </div>
      <div>
        <iframe  src='https://github.com/MrPanda05/Le_Game' title='Github'></iframe>
      </div>
    </div>
  )
}

export default Source