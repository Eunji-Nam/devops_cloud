const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set

//-- 풀이 
// const artist_array = song_array
//     .map(({ artist }) => artist);

// const artist_set = new Set(artist_array)
// console.log(artist_set.size)

//-- 풀이2
const artist_count = song_array
    .map(({ artist }) => artist)
    .reduce((acc, artist) => {
        acc.add(artist);
        return acc;
    }, new Set())
    .size;

console.log(`artist_count : ${artist_count}`);


// //-- 과제
// const artist_set = new Set()

// for (const song of song_array) {
//     artist_set.add(song.artist)
// }

// console.log(artist_set.size);
