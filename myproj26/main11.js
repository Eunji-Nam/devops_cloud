const fs = require("fs");
const fsPromises = fs.promises;


// await는 promise 문법에 대한 축약 - async와 쌍으로 함께 사용
async function main() {
    try {
        const files = await fsPromises.readdir("c:/Dev");
        console.log("loaded :", files);
    }
    catch (error) {
        console.log(error);
    }
}

main();


// 2: Promise
// fsPromises.readdir("c:/Dev")
//     .then(function (files) {   // 정상동작했을 떄 
//         console.log("loaded :", files);
//     })
//     .catch(function (error) {    // error 가 났을 때 
//         console.error(error);
//     });
// // 2-1
// fsPromises.readdir("c:/Dev")
//     .then((files) => {   // 정상동작했을 떄 
//         console.log("loaded :", files);
//     })
//     .catch((error) => {    // error 가 났을 때 
//         console.error(error);
//     });
// // 2-2
// fsPromises.readdir("c:/Dev")
//     .then(files => console.log("loaded :", files))
//     .catch(error => console.error(error));


// // 1 
// fs.readdir("c:/Dev", function (err, files) {
//     if (err) {
//         console.error(err);
//     }
//     else {
//         console.log(files);
//     }
// });


console.log("ENDED");
