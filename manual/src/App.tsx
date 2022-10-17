import React from 'react';
import {
  Routes,
  Route,
} from "react-router-dom";
import Main from './pages/Main';
import Header from './components/Header';
import Navigation from './components/Navigation';
import Player from './pages/Player';
import API from './pages/API';
import Source from './pages/Source';

function App() {
  return (
    <div className="App">
      <Header />
      <Navigation />
      <Routes>
        <Route path='/' element={<Main/>}/>
        <Route path='/manual-de-jogador' element={<Player />} />
        <Route path='/manual-de-codigo' element={<API />} />
        <Route path='/codigo-fonte' element={<Source />} />
      </Routes>
    </div>
  );
}

export default App;
