const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const LikeOver20 = song_array.filter(song => song.like >= 200000);

const LikeOver20List = LikeOver20.map(
    song => song.title
)

console.log(LikeOver20List)
