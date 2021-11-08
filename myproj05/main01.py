import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

for song in song_list:
    if song["artist"] == "방탄소년단":
        # print(song["artist"], song["title"], song["like"])

        line = "{}, {}, {}".format(
            song["artist"], song["title"], song["like"])

        line = "{가수명}, {곡명}, {좋아요수}".format(
            가수명=song["artist"], 곡명=song["title"], 좋아요수=song["like"])

        line = "{artist}, {title}, {like}".format(
            artist=song["artist"], title=song["title"], like=song["like"])

        # unpack arguments
        line = "{artist}, {title}, {like}".format(**song)  # 제일 많이 쓰는 코드

        print(line)
