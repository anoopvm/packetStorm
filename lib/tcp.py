from scapy.all import *
from packet import Packet

class Tcp(Packet):
    def __init__(self,src_ip,dst_ip,src_port,dst_port,proto_number,payload):
        Packet.__init__(self,src_ip,dst_ip,src_port,dst_port,proto_number)
        self.payload = payload
    def generate(self,count=1):
        packet = IP(src=self.src_ip,dst=self.dst_ip)/TCP(seq=RandInt(), sport=self.src_port, dport=self.dst_port)/self.payload
        send(packet,count=count)
        return True
