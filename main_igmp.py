#!/usr/bin/python
from lib.igmp import Igmp
import sys

gen = Igmp("127.0.0.1","127.0.0.1",2,"helloooo!!!")
gen.generate(int(sys.argv[1]))
 
