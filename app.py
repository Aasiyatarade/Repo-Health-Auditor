from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from task import run_repo_health

app = Flask(__name__)

app.secret_key = "repo_health_secret"


USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username

            return redirect(url_for("home"))

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def home():

    if "user" not in session:
        return redirect(url_for("login"))

    report = None

    if request.method == "POST":

        repo = request.form["repo"]

        report = run_repo_health(repo)

    return render_template(
        "index.html",
        report=report
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)