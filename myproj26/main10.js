// => {} : arrow function뒤의 {}는 코드의 시작
// {} : 코드의 시작이나 object화에서 이용되기 때문에 헷갈릴 수 있음 

const mysum2 = (x, y) => { x, y };
console.log(mysum2(1, 2));

const mysum3 = (x, y) => {
    return { x, y };
};
console.log(mysum3(1, 2));

const mysum4 = (x, y) => ({ x, y });
console.log(mysum4(1, 2));
