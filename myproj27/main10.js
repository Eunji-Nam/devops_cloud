const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

const BTS_song = song_array
    .filter(song => song.artist === "방탄소년단")
    .reduce((prev, curr) => prev + curr.like, 0);

console.log(BTS_song)



