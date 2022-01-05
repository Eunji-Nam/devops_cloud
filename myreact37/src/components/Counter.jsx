import { useReducer, useState } from 'react';
import './Counter.css';

const ACTION_TYPES = {
  PLUS: 'PLUS',
  MINUS: 'MINUS',
};

function reducer(prevState, action) {
  const { type } = action;
  if (type === ACTION_TYPES.PLUS) {
    return prevState + 1;
  } else if (type === ACTION_TYPES.MINUS) {
    return prevState - 1;
  }
  return prevState; // 방어
}

function Counter() {
  //   const [value, setvalue] = useState(0);
  const [state, dispatch] = useReducer(reducer, 0);

  //   const handleClick = () => {
  //     setvalue((prevValue)=> prevValue + 1 );
  //   };

  //   const handleClick1 = (e) => {
  //     e.preventDefault();
  //     setvalue((prevValue)=> prevValue - 1 );
  //   };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'red' }}
      onClick={() => dispatch({ type: ACTION_TYPES.PLUS })}
      onContextMenu={(e) => {
        e.preventDefault();
        dispatch({ type: ACTION_TYPES.MINUS });
      }}
    >
      {state}
    </div>
  );
}

export default Counter;
