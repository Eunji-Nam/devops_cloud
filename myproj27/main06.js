const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

// 1개의 song object를 문자열로 변환
//-- 풀이
// const titleLen = song_array.map(
//     (song) => {
//         const word_count = song.title.trim().split(/\s+/).length;
//         return `${song.title} / ${word_count}`;
//     }
// )
// 연속된 공백 지우기: /\s+/나  RegEx사용
// 양 끝의 공백 제거 : trim()
// 양 끝과 연속된 공백 지우기 trim().split(/\s+/)

//-- 과제
// const titleLen2 = song_array.map(
//     (song) => {
//         const word_count = song.title.trim().split(/\s+/).length;
//         return `${song.title} / ${word_count}`;
//     },
// );

// console.log(titleLen2)


// // 기존 song_array 배열에서
// // word_count 라는 컬럼을 추가 하고 싶다.
const titleLen2 = song_array.map(
    (song) => {
        const word_count = song.title.trim().split(/\s+/).length;
        return {
            ...song,
            word_count: word_count,
        };
    },
);


for (const new_song of titleLen2) {
    console.log(new_song);  // 기존 song + word_count 컬럼
}

