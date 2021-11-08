from collections import Counter  # 맨 앞에 씀

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())
# print(song_list)

"""
방탄소년단의 곡명만 출력
HInt : for 루프 내에서 if 조건문을 통해 "가수"필드 체크
"""

for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])

"""
곡명에 "가을"이 들어가는 곡명만 출력
Hint: 포함여부="가을" in 곡명
"""

for song in song_list:
    if "가을" in song["title"]:
        print(song["title"])

"""
좋아요 수가 20_0000이 넘는 곡수는?
Hint: int(좋아요) > 20_0000
"""

song_count = 0
for song in song_list:
    if song["like"] > 20_0000:
        song_count += 1

print(f"좋아요가 200_000이 넘는 곡은 {song_count}곡 입니다.")

"""
가수 별 곡수를 출력
"""

artist_dict = {}

for song in song_list:
    artist: str = song["artist"]
    if artist not in artist_dict:
        artist_dict[artist] = 0
    artist_dict[artist] += 1
    # artist_list.append(artist)

print(artist_dict)

# {
#     "방단소년단" : 10,
# }
# 두번째 풀이
singer = []
for song in song_list:
    singer.append(song["artist"])

singer_1 = {}

for ch in singer_1:
    try:
        singer_1[ch] += 1  # KeyError 발생 가능성이 높기 때문에
    except KeyError:
        singer_1[ch] = 1  # except만 쓰지 않고 KeyError 추가

 # 세번째 풀이

# for song in song_list:
#     artist_list.append(song["artist"])

# list Comprehension
artist_list = []

artist_list = [
    song["artist"]
    for song in song_list]

counter = Counter(artist_list)

# for artist in counter:  #keys
#     print(artist)

for song_count in counter.values():  # values
    print(song_count)

for artist in counter:
    print(artist, counter[artist])

for artist, song_count in counter.items():  # keys와 values 한번에
    print(artist, song_count)
