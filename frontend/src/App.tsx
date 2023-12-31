import { useState, useEffect } from "react";
import axios from "axios";
import FeedCard from "./components/FeedCard";
import get_host from "./utils/host"

function App() {
  const [feeds, setFeeds] = useState<any>([]);

  useEffect(() => {
    const url:string = get_host("api/v1/feeds/")
    axios(url).then((res) => {
      setFeeds(res);
      console.log(res.data);
    });
  }, []);

  return (
    <>
      <h1 className="text-3xl font-bold underline text-center text-primary">
        NextFeed - Your Content Aggregator
      </h1>
      { }
      <div className="flex justify-center">
        {feeds.data
          ? feeds.data.map((feed: any, id: number) => (
            <FeedCard
              key={id}
              title={feed.title}
              tags={feed.tags}
              description={feed.description}
              thumbnail_url={feed.thumbnail_url}
            />
          ))
          : ""}
      </div>
    </>
  );
}

export default App;
