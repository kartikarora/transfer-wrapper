"""
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
                print res.text
                f.close()
                return res.text
            except Exception as e:
                print e
                return make_response(jsonify({"error": "Something Went Wrong"}))
    else:
        return make_response(jsonify({"error": "Invalid Method"}))


if __name__ == '__main__':
    app.run()
