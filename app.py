from flask import Flask, render_template, request
import random

app = Flask(__name__)

seikai = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess == seikai:
            message = "正解！！"
        elif guess < seikai:
            message = "もっと大きいで！"
        else:
            message = "もっと小さいで！"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)