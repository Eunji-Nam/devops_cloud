// Array
// name만 저장하고 싶을 때 
// const [name] = ["Tom", 10, "Seoul"];
// // age만 저장하고 싶을 때 
// const [, age,] = ["Tom", 10, "Seoul"];

// // height는 undefined
// const [name, age, region, height] = ["Tom", 10, "Seoul"];

// // 값 할당에 실패했을 때, 적용되는 디폴트 값
// const [name, age, region, height = 140] = ["Tom", 10, "Seoul"];

// 디폴트 값을 함수 호출로 지정 : 디폴트 값이 필요한 시점에 함수가 호출됨.
function get_default_height() {
    console.log("get_default_height 함수를 호출했습니다.");
    return 140;
}
// const [name, age, region, height = get_default_height()] = ["Tom", 10, "Seoul", 150];
const [name, age, region, height = get_default_height()] = ["Tom", 10, "Seoul"];