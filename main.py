from flask import Flask, render_template, flash, request
import ScreeningAlgo

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/applicants')
def applicants():
    return render_template("applicants.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/temp')
def event1():
    return render_template("temp.html")


@app.route('/handle_data', methods=['POST'])
def handle_data():
	print(request.form.to_dict())
	ename = request.form.to_dict()['eventname']
	interest = request.form.to_dict()['interests']
	noofcandidates = request.form.to_dict()['noofcandidates']
	print(ename)
	ScreeningAlgo.find_potential_candidates(ename, interest,noofcandidates)
	return  render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)