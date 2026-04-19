from flask import Flask, render_template, request, session
import random

app = Flask(__name__)

app.secret_key = "secret_key"


@app.route("/", methods=["GET", "POST"])
def index():
    if "seikai" not in session:
        session["seikai"] = random.randint(1, 100)
    
    if "count" not in session:
        session["count"] = 10

    message = ""
    hint = ""
    error = ""

    if request.method == "POST":
        if "reset" in request.form:
            session.clear()

        try:
            guess = int(request.form["guess"])
            session["count"] -= 1

            if guess == session["seikai"]:
                 message = "正解！！"
                 session.clear()

            elif session["count"] <= 0:
                message = f"ゲームオーバー！正解は{session['seikai']}"
                
            elif guess < session["seikai"]:
                hint = f"もっと大きいで！残り{session['count']}回！"

            else:
                hint = f"もっと小さいで！残り{session['count']}回！"

        except ValueError:
            error = "数字を入力してな～！"

    return render_template("index.html", message = message,hint = hint,error=error,count=session.get("count"))

if __name__ == "__main__":
    app.run(debug=True)