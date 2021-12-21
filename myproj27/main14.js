const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const BTS_like1 = song_array
    .filter(song => song.artist === "방탄소년단")
    .reduce((previous, current) => {
        return previous.like < current.like ? previous : current;
    });


console.log(BTS_like1.title)