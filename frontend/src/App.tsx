import { useState, useEffect } from 'react'
import axios from 'axios'


function App() {

  const [feeds, setFeeds] = useState<any>([]);


  useEffect(() => {
    axios("http://localhost:8000/api/v1/feeds/").then((res) => {
      setFeeds(res);
    });
  }, []);

  return (
    <>

      <h1>NextFeed - Your Content Aggregator</h1>
      {JSON.stringify(feeds, null, 4)}

    </>
  )
}

export default App
