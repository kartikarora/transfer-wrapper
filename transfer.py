import requests
from flask import Flask, redirect, request, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
	return redirect("https://transfer.sh")


@app.route('/upload', methods=['POST', 'PUT'])
def upload():
	if request.method == 'POST' or request.method == 'PUT':
		data = request.files['files']
		file = data.read()
		name = file.filename
		try:
			response = requests.put("https://transfer.sh/" + name, file)
			return response
		except Exception as e:
			print e
			return "Something went wrong"
	else:
		return make_response("Invalid Method")


if __name__ == '__main__':
	app.run()
