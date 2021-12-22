const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

// ---- 함수를 만들어서 적용하는 방법 

function compare_string_for_sort(string1, string2, is_ascending = true) {
    if (string1 < string2) {
        // 3항 연산자
        return is_ascending ? -1 : 1;   // 참 : 거짓
        // return -1;  // 오름차순 
        // return 1;   // 내림차순
    }
    else if (string1 > string2) {
        return is_ascending ? 1 : -1
    }
    else {
        return 0;
    }
}

const LikeOver20 = song_array
    .filter(song => song.like >= 200000)
    .sort((a, b) => {
        return compare_string_for_sort(a.title, b.title, true)
    });


// -------- 기본

// const LikeOver20 = song_array
//     .filter(song => song.like >= 200000)
//     .sort((a, b) => { // 문자열끼리 -는 할 수 없지만 대소비교는 가능 
//         // 오름차순
//         // a가 b보다 크다면 음수를 반환
//         // a가 b보다 작다면 양수를 반환 
//         // 내림차순
//         // a가 b보다 크다면 양수를 반환
//         // a가 b보다 작다면 음수를 반환 
//         if (a.title < b.title) return -1;
//         else if (a.title > b.title) return 1;
//         else return 0;
//     });

for (const song of LikeOver20) {
    console.log(`[${song.like}]`, song.title, song.artist);
};