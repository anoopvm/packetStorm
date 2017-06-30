#!/usr/bin/python
from lib.tcp import Tcp
import sys

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/generate_packets", methods = ['POST'])
def api_proto_tcp():
    src_ip = request.form['src-ip']
    dst_ip = request.form['dst-ip']
    src_port = int(request.form['src-port'])
    dst_port = int(request.form['dst-port'])
    #proto_number = int(request.form['proto-number'])
    no_of_packets = int(request.form['no-of-packets'])
    payload = request.form['payload']

    #gen = Tcp("127.0.0.1","127.0.0.1",1000,1000,1,"helloooo!!!")
    gen = Tcp(src_ip,dst_ip,src_port,dst_port,1,str(payload))
    #gen.generate(int(sys.argv[1]))
    gen.generate(no_of_packets)
    return render_template('index.html')

#if __name__ == "__main__":
app.run()
