## Transfer.sh Wrapper  [![Build Status](https://travis-ci.org/kartikarora/transfer-wrapper.svg?branch=master)](https://travis-ci.org/kartikarora/transfer-wrapper)

Python + Flask based wrapper API for [Transfer.sh](https://transfer.sh) service

Just send a `POST` or a `PUT` request to `https://transfer-wrapper.herokuapp.com/upload/<filename>` and the binary file as the body

You will get a url similar to `https://transfer.sh/abcd/filename` as reply if all goes well.

Else a JSON object `{"error": "Something Went Wrong"}`

Feel free to fork and deploy 

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
