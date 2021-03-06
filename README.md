## Transfer.sh Wrapper  [![Build Status](https://travis-ci.org/kartikarora/transfer-wrapper.svg?branch=master)](https://travis-ci.org/kartikarora/transfer-wrapper)

Python + Flask based wrapper API for [Transfer.sh](https://transfer.sh) service

Just send a `POST` or a `PUT` request to `https://transfer-wrapper.herokuapp.com/upload/<filename>` and the binary file as the body

You will get a url similar to `https://transfer.sh/abcd/filename` as reply if all goes well.

Else a JSON object `{"error": "Something Went Wrong"}`

Feel free to fork and deploy 

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

### MIT License
```
MIT License

Copyright (c) 2016 Kartik Arora

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
```
