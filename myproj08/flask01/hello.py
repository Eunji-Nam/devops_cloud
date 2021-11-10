# pip install flask

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    # DB Access
    like_foods = [
        "초밥",
        "육회",
        "샤브샤브",
        "쌀국수",
        "대창",
    ]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():  # ->누가 받을지 설정
    return render_template("post_list.html")
