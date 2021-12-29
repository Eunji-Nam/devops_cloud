import { useState } from "react";

function makeLottoNumbers() {
  const range = [...Array(45).keys()];

  const randomNumbers = range
    .sort(() => Math.random() - Math.random())
    .map((number) => number + 1)
    .slice(0, 7)
    .sort((num1, num2) => num1 - num2);

  return randomNumbers;
}

// console.log(makeLottoNumbers());

function PageLotto() {
  const [numberList, setNumberList] = useState([10, 11, 12, 13, 14, 15, 16]);
  const handleClick = () => {
    console.log("clicked");
    setNumberList(makeLottoNumbers());
  };

  return (
    <div>
      <h2>Lotto</h2>
      <button onClick={handleClick}>예지!</button>
      <ul className="numberList">
        {numberList.map((number) => {
          return (
            <div
              style={{
                backgroundColor: "red",
                width: "30px",
                height: "30px",
                borderRadius: "50%",
                lineHeight: "30px",
                textAlign: "center",
                display: "inline-block",
                margin: "0.7rem",
              }}
            >
              {number}
            </div>
          );
        })}
      </ul>
    </div>
  );
}

export default PageLotto;
