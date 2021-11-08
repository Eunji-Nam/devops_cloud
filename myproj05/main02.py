import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


def 정렬기준값을_만들어줄_함수(song):
    return song["like"]

# 정렬을 하려면 각 값들에 대한 대소비교가 가능해야 한다.
# 10 < 100     "가" < "나"
# {"A" : 1} < {"B" : 2}   => dict끼리는 비교 불가(기준필요)

# for song in sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수):
#     print("[{like}] {title} {artist}".format(**song))


sorted_song_list = sorted(song_list, reverse=True, key=정렬기준값을_만들어줄_함수)

# 좋아요 상위 10
for song_dict in sorted_song_list[:10]:
    print("[{like}] {title} {artist}".format(**song_dict))

# print(song_list["title"][:10])
