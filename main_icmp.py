#!/usr/bin/python
from lib.icmp import Icmp
import sys

gen = Icmp("127.0.0.1","127.0.0.1",1,"helloooo!!!")
gen.generate(int(sys.argv[1]))
 
