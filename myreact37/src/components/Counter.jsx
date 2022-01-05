import { useReducer, useState } from 'react';
import './Counter.css';

function reducer(prevState, action) {
  const { type } = action;
  if (type === 'PLUS') {
    return prevState + 1;
  } else if (type === 'MINUS') {
    return prevState - 1;
  }
  return prevState;
}

function Counter() {
  //   const [value, setvalue] = useState(0);
  const [state, dispatch] = useReducer(reducer, 0);

  //   const handleClick = () => {
  //     setvalue(value + 1);
  //   };

  //   const handleClick1 = (e) => {
  //     e.preventDefault();
  //     setvalue(value - 1);
  //   };

  return (
    <div
      className="counter"
      style={{ backgroundColor: 'red' }}
      onClick={() => dispatch({ type: 'PLUS' })}
      onContextMenu={(e) => {
        e.preventDefault();
        dispatch({ type: 'MINUS' });
      }}
    >
      {state}
    </div>
  );
}

export default Counter;
