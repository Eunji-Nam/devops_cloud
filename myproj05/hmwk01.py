"""
멜론 TOP100 리스트에서 "곡명"단어수 출력
 총 100줄 중에 한 줄 출력의 예 : Dynamite -> 1
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

title_list = []
for song in song_list:
    title_list.append(song["title"])

    # title_word_count = title_list.split()

# print(title_word_count)


# title_word_count = list(map(title_list, title_list.split()))
# print(title_word_count)


def song_word_count(title_list):
    return len(title_list.split())
    print(song_word_count)
