import requests
from flask import Flask, redirect, request, make_response

app = Flask(__name__)


@app.route('/')
def hello_world():
	return redirect("https://transfer.sh")


@app.route('/upload', methods=['POST', 'PUT'])
def upload():
	if request.method == 'POST' or request.method == 'PUT':
		file = request.files['image']
		f = file.read()
		filename = file.filename
		t = open("convert_landmark.png", "wb+")
		t.write(f)
		t.close()
		try:
			response = requests.put("https://transfer.sh/" + filename, f)
			return response
		except Exception as e:
			print e
			return "Something went wrong"
	else:
		return make_response("Invalid Method")


if __name__ == '__main__':
	app.run()
