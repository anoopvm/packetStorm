from scapy.all import *
from packet import Packet

class Icmp(Packet):
    def __init__(self,src_ip,dst_ip,proto_number,payload):
        Packet.__init__(self,src_ip,dst_ip,0,0,proto_number)
        self.payload = payload
    def generate(self,count=1):
        packet = IP(src=self.src_ip,dst=self.dst_ip)/ICMP()/self.payload
        send(packet,count=count)
        ##packet.show()
        ##print "Packet sent {} time(s).".format(count)
