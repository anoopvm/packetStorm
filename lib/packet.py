
class Packet:
    def __init__(self,src_ip,dst_ip,proto_number):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.proto_number = proto_number
    def set_src_ip(self,src_ip):
        self.src_ip = src_ip
    def set_dst_ip(self,dst_ip):
        self.dst_ip = dst_ip
    def set_proto(self, proto_number):
        self.proto_number = proto_number
    def get_packet_info(self):
        return {"src_ip":self.src_ip,"dst_ip":self.dst_ip,"proto":self.proto.number}
