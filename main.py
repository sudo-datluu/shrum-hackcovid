from flask import Flask, render_template


app = Flask(__name__)

user_data ={}

@app.route("/")
def hello_covid():
	return render_template('login.html')

@app.route("/login")
def login():
	return render_template('Login_Screen.html')

@app.route("/create_goal_1")
def create_goal_1():
	return render_template('create_goal_1.html')
	
@app.route("/create_goal_2/<goaltype>")
def create_goal_2(goaltype):
	user_data["goal_type"] = str(goaltype)
	print(user_data)
	return render_template('create_goal_2.html')

@app.route("/create_goal_3/<goal_name>/<plan_content>")
def create_goal_3(goal_name, plan_content):
	user_data["goal_name"] = str(goal_name)
	user_data["plan_content"] = str(plan_content)
	print(user_data)
	return render_template('create_goal_3.html')


if __name__ == "__main__":
	app.run(debug=True)