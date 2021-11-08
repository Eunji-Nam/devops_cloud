"""
가수 별 곡수를 출력
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

song_list_cnt = {}

for song in song_list:
    if song["artist"] in song_list_cnt:
        song_list_cnt[song["artist"]] += 1
    else:
        song_list_cnt[song["artist"]] = 1


print(song_list_cnt)

# print(artist_list)
# print('')
