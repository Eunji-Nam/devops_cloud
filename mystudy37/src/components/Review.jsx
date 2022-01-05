import './Review.css';

function Review({ review, onClick }) {
  return (
    <div className={'review'} onClick={onClick}>
      {review.content} {review.star}
    </div>
  );
}

export default Review;
