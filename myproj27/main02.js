const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TOOD: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter


const BTS_song = song_array
    .filter(song => song.artist === "방탄소년단");
// => 다음값이 true인지 false인지 리턴함 

// const BTS_song = song_array
// .filter(({ artist }) => artist === "방탄소년단"); 로 변경 가능


for (const song of BTS_song) {
    console.log(song.artist, song.title, song.like);
}

