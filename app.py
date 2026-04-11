from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = "secret_key"

seikai = random.randint(1, 100)


@app.route("/", methods=["GET", "POST"])
def index():
    if "seikai" not in session:
        session["seikai"] = random.randint(1, 100)

    message = ""

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])

            if guess == session["seikai"]:
                message = "正解！！"
                session.pop("seikai")  # リセット
            elif guess < session["seikai"]:
                message = "もっと大きいで！"
            else:
                message = "もっと小さいで！"
        except ValueError:
            message = "数字を入力してな～！"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)