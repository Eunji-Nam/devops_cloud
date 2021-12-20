//var는 최신버전에서 사용하지 않는 문법
// var name = "남은지";  // 변수 선언
// name = "제인"; // 변수 변경

// 변수 - 변경 가능 
let name = "남은지" // 변수 선언 
name = "제인"; // 변수 변경

// 상수(Constant) - 변경 불가
const age = 10;
//age = 12; // 상수는 값을 변경할 수 없음 

console.log(name, age);

const number = 10;

//
// 제어구조
if (number % 2 === 0) {
    console.log("짝수");
}
else {
    console.log("홀수");
}

// i++: i의 값을 1씩 증가
for (let i = 1; i < 11; i++) {
    console.log(i);
}
// 홀수 출력 - i+=2: i의 값을 2씩 증가 
for (let i = 1; i < 11; i += 2) {
    console.log(i);
}


//
// 함수 

function mysum(x, y) {
    return x + y;
}
console.log(mysum(1, 2));

const mysum2 = function (x, y) {
    return x + y;
};
console.log(mysum2(1, 2));

// arrow function
const mysum3 = (x, y) => {
    return x + y;
};
console.log(mysum3(1, 2));

const mysum4 = (x, y) => x + y;
console.log(mysum4(1, 2));


function mysum5(x, y, ...args) {
    console.log(x, y, args);
}

mysum5(1, 2, 3, 4, 5);  // 1 2 [ 3, 4, 5 ] 출력


function reducer(prevValue, currentValue) {
    return prevValue + currentValue;
}

const result = [1, 2, 3, 4, 5].reduce(reducer, 0);
console.log(result);

const result2 = [1, 2, 3, 4, 5].reduce((prevValue, currentValue) => {
    return prevValue + currentValue;
}, 0);

console.log(result2);


const result3 = [1, 2, 3, 4, 5].reduce(
    (prevValue, currentValue) => prevValue + currentValue,
    0);

console.log(result3);