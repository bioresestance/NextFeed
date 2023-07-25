type FeedCardProps = {
  title: string;
  description: string;
  thumbnail_url: string;
  tags: string[];
};

function FeedCard(props: FeedCardProps) {
  return (
    <div className="card w-96 bg-secondary text-primary shadow-xl m-10">
      <figure>
        <img
          src="https://picsum.photos/400/200"
          alt="Shoes"
          className="w-full"
        />
      </figure>
      <div className="card-body">
        <h2 className="card-title font-bold">{props.title}</h2>
        <p className="">{props.description}</p>
        <div className="card-actions justify-end">
          {props.tags.length > 0
            ? props.tags.map((tag, index) => (
                <div key={index} className="badge badge-outline">
                  {tag}
                </div>
              ))
            : ""}
        </div>
      </div>
    </div>
  );
}

export default FeedCard;
