import os
import requests
from flask import Flask, redirect, request, make_response, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def hello_world():
	return redirect("https://transfer.sh")


@app.route('/upload/<filename>', methods=['POST', 'PUT'])
def upload(filename):
	if request.method == 'POST' or request.method == 'PUT':
		filename = secure_filename(filename)
		fileFullPath = os.path.join("/tmp/", filename)
		with open(fileFullPath, 'wb+') as f:
			inp = request.get_data(cache=False, as_text=False, parse_form_data=False)
			f.write(inp)
		try:
			res = requests.put("https://transfer.sh/" + filename, f)
			f.close()
			return res
		except Exception as e:
			print e
			return make_response(jsonify({"error": "Something Went Wrong"}))
	else:
		return make_response(jsonify({"error": "Invalid Method"}))


if __name__ == '__main__':
	app.run()
