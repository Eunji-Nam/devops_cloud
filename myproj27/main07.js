const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const BTS_Song = song_array.filter(song => song.artist === "방탄소년단");

const BTS_strSong = BTS_Song.map(
    song => song.title
)

console.log(BTS_strSong)
