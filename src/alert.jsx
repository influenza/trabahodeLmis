import { useEffect, useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import axios from "axios";
import './App.css';
import { BrowserRouter, Route, Link } from 'react-router-dom';

export default function App2(){
    const [postado, setpostado] = useState(false);
    const [data, setData] = useState("");
  
    useEffect(() => {
      console.log(postado);
      if (postado === false) {
        setpostado(true);
      } else {
        axios.post('http://127.0.0.1:5000/my-datas', {
          plusone: 1
        }).then(response => {
          console.log(response.data);
          setData(response.data)
        }).catch(error => {
          console.log(error);
        });
      }
    }, [postado]);
    return (
      <>
        <div>
          Você e mais {data} pessoas foram enganadas pela internet
        </div>
      </>
    );
  }