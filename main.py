from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_covid():
	return render_template('login.html')