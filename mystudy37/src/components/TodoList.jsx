import { useState } from 'react';

const INITIAL_STATE = [
  { content: '잘가라 2021', color: 'DarkViolet' },
  { content: '반갑다 2022', color: 'Maroon' },
  { content: '파이팅 2022', color: 'Maroom' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);
  const [inputText, setInputText] = useState('');

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  const changeInputText = (e) => {
    setInputText(e.target.value);
  };

  const appendInputText = (e) => {
    if (e.key === 'Enter') {
      setTodoList((prevTodoList) => {
        return [...prevTodoList, { content: inputText }];
      });
      setInputText('');
    }
  };

  return (
    <div>
      <h2>Todo List</h2>

      <input
        type="text"
        value={inputText}
        onChange={changeInputText}
        onKeyPress={appendInputText}
      />

      {todoList.map((todo, index) => (
        <div onClick={() => removeTodo(index)}>{todo.content}</div>
      ))}
    </div>
  );
}

export default TodoList;
