from flask import Flask, jsonify, redirect, url_for, render_template

# create an instance of our app
app = Flask(__name__)

@app.route("/") # localhost:5000 is the default port for flask
def home():
    return redirect(url_for("login"))


@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/profile/")
def profile():
    return render_template("profile.html")



if __name__ == "__main__":
    app.run(debug=True)