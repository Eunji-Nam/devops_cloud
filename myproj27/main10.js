const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
}

// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

// const BTS_song = song_array
//     .filter(song => song.artist === "방탄소년단")
//     .reduce((acc, song) => acc + song.like, 0);

// const BTS_song = song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .reduce((acc, { like }) => acc + like, 0);

// ---- js에는 sum함수가 없기 때문에 위의 Array함수 구현했을 때, .sum() 사용 가능
const BTS_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .map(({ like }) => like)
    .sum();

console.log("result :", BTS_song)



