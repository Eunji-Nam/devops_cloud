const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

// const love_Song = song_array
//     .filter(song => song.title.includes("사랑"))
//     .map(song => song.title)

const love_Song = song_array
    .filter(({ title }) => title.includes("사랑"))
    .map(({ title }) => title)

console.log(love_Song)
