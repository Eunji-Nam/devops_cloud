import { useReducer } from 'react';

function reducer(prevState, action) {
  const { type, amount, color } = action;
  if (type === 'PLUS') {
    return { ...prevState, value: prevState.value + amount };
  } else if (type === 'MINUS') {
    return { ...prevState, value: prevState.value - amount };
  } else if (type === 'CHANGE_COLOR') {
    return { ...prevState, color: color };
  }
  return prevState;
}

function Counter3() {
  const [state, dispatch] = useReducer(reducer, { value: 0, color: 'red' });
  const { value, color } = state;

  return (
    <div>
      <h2>Counter3</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={() => dispatch({ type: 'PLUS', amount: 1 })}>+</button>
      <button onClick={() => dispatch({ type: 'PLUS', amount: 1 })}>-</button>
      <button
        onClick={() => dispatch({ type: 'CHANGE_COLOR', color: 'green' })}
      >
        green
      </button>
      <button onClick={() => dispatch({ type: 'CHANGE_COLOR', color: 'blue' })}>
        blue
      </button>
      <button onClick={() => dispatch({ type: 'CHANGE_COLOR', color: 'red' })}>
        red
      </button>
    </div>
  );
}

const defaultStyle = {
  width: '100px',
  height: '100px',
  borderRadius: '50px',
  lineHeight: '100px',
  textAlign: 'center',
  display: 'inline-block',
  fontSize: '3rem',
  userSelect: 'none',
};

export default Counter3;
