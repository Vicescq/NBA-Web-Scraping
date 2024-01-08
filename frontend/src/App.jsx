import React, {useState, useEffect} from "react"
import Home from "./components/home/home.jsx"





function App(){
  
  // fetching data
  const [data, setData] = useState(0)
  const ms = 3000
  useEffect(() => {
    const interval = setInterval(() => {
      fetch("/homedata").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          console.log(data)
          // do stuff with data
        }
      )
      
    }, ms)
    return () => clearInterval(interval)
  }, []);

  return(
    <>
      <Home/>
    </>
  )
}

export default App