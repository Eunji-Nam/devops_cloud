import Todo from './Todo';
import './TodoList.css';
import TodoForm from './TodoForm';
import { useState } from 'react';
import useFieldValues from 'hooks/useFieldValues';

const INITIAL_STATE = [
  { content: '2022년에는 취업하기' },
  { content: '파이썬 복습하기' },
  { content: '리액트 복습하기' },
];

function TodoList() {
  const [todoList, setTodoList] = useState(INITIAL_STATE);

  const [fieldValues, handleChange] = useFieldValues();

  const removeTodo = (todoIndex) => {
    setTodoList((prevTodoList) =>
      prevTodoList.filter((_, index) => index !== todoIndex),
    );
  };

  //   const changedInputText = (e) => {
  //     setInputText(e.target.value);
  //   };

  //   const appendInputText = (e) => {
  //     console.log('e.key :', e.key);
  //     if (e.key === 'Enter') {
  //       // todoList 배열 끝에 inputText 추가
  //       // inputText 다시 비우기
  //       console.log('inputText :', inputText);

  //       //setTodoList 에 함수를 넘기는 것.
  //       //todoList 상탯값을 변경하는 것이 아님. (배열의 push 사용 X)

  //       setTodoList((prevTodoList) => {
  //         return [...prevTodoList, { content: inputText }];
  //       });

  //       setInputText('');
  //     }
  //   };

  return (
    <div className="todo_list">
      <h2>Todo List</h2>
      <TodoForm handleChange={handleChange} />

      <hr />
      {JSON.stringify(fieldValues)}
      {/* <input
        type="text"
        value={inputText}
        onChange={changedInputText}
        onKeyPress={appendInputText}
      /> */}

      {todoList.map((todo, index) => (
        <Todo todo={todo} onClick={() => removeTodo(index)} />
        // {/* <div onClick={() => removeTodo(index)}>{todo.content}</div> */}
      ))}
    </div>
  );
}

export default TodoList;
