const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

const artist_count_object = song_array
    .reduce((acc, { artist }) => {
        // if(!acc[artist]) acc[artist] = 0;
        acc[artist] ||= 0
        // i = i || 0
        // i ||= 0
        acc[artist] += 1
        return acc;
    }, {});

Object.value(artist_count_object) // 값만 출력
    .filter(number => number >= 2)


    //python version
    //if artist not in acc:
    //  acc[artist] = 0