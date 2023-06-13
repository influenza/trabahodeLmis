import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import App2 from './alert.jsx';

ReactDOM.createRoot(document.getElementById('root')).render(
<Router>
  <Routes>
    <Route path='/' element={<App />}/>
    <Route path='/trolagem' element={<App2/>}></Route>
  </Routes>
</Router>
)
