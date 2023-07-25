import { useState, useEffect } from "react";
import axios from "axios";
import FeedCard from "./components/FeedCard";

function App() {
  const [feeds, setFeeds] = useState<any>([]);

  useEffect(() => {
    axios("http://localhost:8000/api/v1/feeds/").then((res) => {
      setFeeds(res);
      console.log(res.data);
    });
  }, []);

  return (
    <>
      <h1 className="text-3xl font-bold underline text-center text-primary">
        NextFeed - Your Content Aggregator
      </h1>
      {}
      <div className="flex justify-center">
        {feeds.data
          ? feeds.data.map((feed: any, id: number) => (
              <FeedCard
                key={id}
                title={feed.title}
                tags={["Tech", "Art", "News"]}
                description={feed.description}
                thumbnail_url={feed.thumbnail_url}
                // tags={feed.tags}
              />
            ))
          : ""}
      </div>
    </>
  );
}

export default App;
