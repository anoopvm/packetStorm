#!/usr/bin/python
from lib.tcp import Tcp
import sys

gen = Tcp("127.0.0.1","127.0.0.1",1000,1000,1,"helloooo!!!")
gen.generate(int(sys.argv[1]))
 
