#!/usr/bin/python
from lib.udp import Udp
import sys

gen = Udp("127.0.0.1","127.0.0.1",1000,1000,1,"helloooo!!!")
gen.generate(int(sys.argv[1]))
 
