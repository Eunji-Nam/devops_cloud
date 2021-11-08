"""
곡명에 "가을"이 들어가는 곡명만 출력
-Hint: 포함여부="가을" in 곡명
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


for song in song_list:
    if "가을" in song["title"]:
        print(song["title"])
