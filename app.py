#!/usr/bin/python
from lib.tcp import Tcp
import sys

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/protocols/tcp")
def api_proto_tcp():
	gen = Tcp("127.0.0.1","127.0.0.1",1000,1000,1,"helloooo!!!")
	#gen.generate(int(sys.argv[1]))
	gen.generate(10)
	return render_template('index.html')

#if __name__ == "__main__":
app.run()