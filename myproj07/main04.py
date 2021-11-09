"""
멜론 TOP100 리스트에서 
 리스트에 랭트된 가수는 총 몇 팀?(중복 제거한 가수명 리스트의 크기)
 """
import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 1
artist_list = []
for song_dict in song_list:
    artist: str = song_dict["artist"]
    if artist not in artist_list:
        artist_list.append(artist)

print(len(artist_list))

# 2
artist_set = set()
for song_dict in song_list:
    artist: str = song_dict["artist"]
    artist_set.add(artist)
print(len(artist_set))


# 3

artist_set = set([song_dict["artist"]
                  for song_dict in song_list])  # append할 항목을 for 앞에
print(len(artist_set))


# 4 : Set Comprehension

artist_set = {song_dict["artist"]
              for song_dict in song_list}   # 만들 때부터 set
print(len(artist_set))


#  2곡 이상 랭크된 가수는 몇 팀?
#  "방탄소년단"의 좋아요 총 합?
