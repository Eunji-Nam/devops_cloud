import { useState } from 'react';

function reducer(action, prevState) {
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
  //   const [value, setValue] = useState(0);
  //   const [color, setColor] = useState('red');
  const [state, setState] = useState({ value: 0, color: 'red' });

  const { value, color } = state;

  const handlePlus = () => {
    //     // setValue(value + 1);
    //     // setValue((prevValue) => prevValue + 1);
    //     // setState((prevState) => ({
    //     //   ...prevState,
    //     //   value: prevState.value + 1,
    //     // }));
    const action = { type: 'PLUS', amount: 1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleMinus = () => {
    //     // setValue(value - 1);
    //     // setValue((prevValue) => prevValue - 1);
    //     // setState((prevState) => ({
    //     //   ...prevState,
    //     //   value: prevState.value - 1,
    //     // }));
    const action = { type: 'MINUS', amount: 1 };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleGreen = () => {
    //     // setColor('green');
    //     // setColor(() => 'green');
    //     // setState((prevState) => ({
    //     //   ...prevState,
    //     //   color: 'green',
    //     // }));
    const action = { type: 'CHANGE_COLOR', color: 'green' };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleBlue = () => {
    //     // setColor('blue');
    //     // setColor(() => 'blue');
    //     // setState((prevState) => ({
    //     //   ...prevState,
    //     //   color: 'blue',
    //     // }));
    const action = { type: 'CHANGE_COLOR', color: 'blue' };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  const handleRed = () => {
    //     // setColor('red');
    //     // setColor(() => 'red');
    //     // setState((prevState) => ({
    //     //   ...prevState,
    //     //   color: 'red',
    //     // }));
    const action = { type: 'CHANGE_COLOR', color: 'red' };
    setState((prevState) => {
      return reducer(action, prevState);
    });
  };

  return (
    <div>
      <h2>Counter3</h2>
      <div style={{ ...defaultStyle, backgroundColor: color }}>{value}</div>
      <hr />
      <button onClick={handlePlus}>+</button>
      <button onClick={handleMinus}>-</button>
      <button onClick={handleGreen}>green</button>
      <button onClick={handleBlue}>blue</button>
      <button onClick={handleRed}>red</button>
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
