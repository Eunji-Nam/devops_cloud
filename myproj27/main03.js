const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

// 좋아요 수에 대한 내림차순 정렬 -> 처음 10개

const like_top10 = song_array
    .sort((a, b) =>
        b.like - a.like)
    .slice(0, 10);

let i = 1;
for (const song of like_top10) {
    console.log(`${i} [${song.like}]`, song.title, song.artist);
    i++;
}


// for (const { like, title, artist } of like_top10) {
//     console.log(`[${like}] ${title} ${artist}`);
// }

// for (const [index, song] of like_top10.entries()) {
//     console.log(`${index + 1} [${song.like}]`, song.title, song.artist);
//     i++;
// }

// 좋아요 수에 대한 오름차순 정렬 -> 마지막 10개 -> 뒤집음