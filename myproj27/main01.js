/*
  {
    'Unnamed: 0': 99,
    song_no: 31316695,
    title: '하루도 그대를 사랑하지 않은 적이 없었다',
    album: '하루도 그대를 사랑하지 않은 적이 없었다',
    artist: '임창정',
    rank: 100,
    like: 162928
  }
*/
const { melon_data: song_array } = require("./melon_data");

// for (const song of song_array) {
//     console.log(song.like, song.title);
// }

// TODO: #1 like 오름차순으로 정렬
// 출력포맷 : `[좋아요수] 곡명`
// Array의 sort 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/sort


// Array의 sort는 
//  자신의 (array)의 순서도 변경하고, 자신을 반환
// Python의 List sort는 
//  자신(list)의 순서만 변경하고, 리턴값이 없음(None)
song_array.sort((a, b) => {
  return a.like - b.like;
  // a가 크면, 양수를 반환 (오름차순)
  // b가 크면, 음수를 반환 (내림차순)
  // 같으면 0을 반환 
});

for (const song of song_array) {
  console.log(`[${song.like}]`, song.title);
}

// const { like, title } = song;

// for (const { like, title } of song_array) {
//   console.log(like, title);
// }

