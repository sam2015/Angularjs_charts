from flask import Flask, render_template


app = Flask(__name__)


@app.route("/line")
def line():
	return render_template('lineIndex.html')


@app.route("/bar")
def bar():
	return render_template('barIndex.html')


@app.route("/scatter")
def scatter():
	return render_template('scatterIndex.html')


@app.route("/pie")
def pie():
	return render_template('pieIndex.html')


if __name__ == '__main__':
	app.run(debug=True)