const { question } = require("readline-sync");

function shuffle(array) {
    array.sort(() => Math.random() - 0.5);
}
const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];
shuffle(animal_names);


const begin_time = Date.now();

let ok_counter = 0;

const random_names = animal_names.slice(0, 5);

// console.log(random_names);


for (names of random_names) {
    console.log(names);
    const line = question(">>> ");

    if (names === line) {
        ok_counter++;
        console.log("정확합니다!");
    }
    else {
        console.log("오타가 있어요.");
    }
}

const end_time = Date.now();


console.log(`${ok_counter}번 성공하셨습니다.`)
console.log(`총 ${(end_time - begin_time) / 1000}초가 걸리셨어요.`)
