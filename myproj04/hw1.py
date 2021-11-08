"""
방탄소년단의 곡명만 출력
HInt : for 루프 내에서 if 조건문을 통해 "가수"필드 체크
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


for song in song_list:
    if song["artist"] == "방탄소년단":
        print(song["title"])
