from flask import Flask, render_template, request, url_for, flash


app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")


if __name__ == "__main__":
	app.secret_key = "ai_project_2018"
	app.debug = True
	app.run(host="0.0.0.0", port=5000)