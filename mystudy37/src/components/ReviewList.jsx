import Review from './Review';
import './ReviewList.css';
import { useState } from 'react';
import ReviewForm from './ReviewForm';
import useFieldValues from 'hook/useFieldValues';

const INITIAL_STATE = [
  { content: '스파이더맨 1 부터 본 사람이면 재미없을 수가 없다.', star: 5 },
  {
    content:
      '전 스파이더맨 두명이 자책했던 일들이 여기서 어느정도 구원받았다는거에 감사드립니다.',
    star: 4,
  },
  {
    content:
      '엔드게임을 뛰어넘는 영화가 죽기전에 나올까 생각했었는데.. 2년만에 나왔습니다.',
    star: 5,
  },
];

function ReviewList() {
  const [reviewList, setReviewList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange, clearFieldValues] = useFieldValues({
    content: '',
    star: 5,
  });

  const appendReview = () => {
    const review = { ...fieldValues };

    setReviewList((prevReviewList) => [...prevReviewList, review]);

    clearFieldValues();
  };

  return (
    <div className="review_list">
      <h2 className="text-xl mb-2 border-b-2 border-orange-500">Review List</h2>
      <ReviewForm
        fieldValues={fieldValues}
        handleChange={handleChange}
        handleSubmit={appendReview}
      />
      <button className="bg-orange-200 hover:bg-orange-400 p-1 rounded text-sm cursor-point">
        New Review
      </button>

      {reviewList.map((review) => (
        <div className="bg-white my-1 p-1 border-2 border-green-600 hover:bg-green-200 cursor-pointer">
          <Review review={review} />
        </div>
      ))}
    </div>
  );
}

export default ReviewList;
