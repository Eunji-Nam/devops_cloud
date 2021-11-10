# Pillow 라이브러리로 이미지 썸네일 처리하기
# pip install pillow

from PIL import Image
# PIL: Python Image Library

im = Image.open("static/kitten.jpg")
im.thumbnail((800, 600))
im.save("static/kitten.jpg")
