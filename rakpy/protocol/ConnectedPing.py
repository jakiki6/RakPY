from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class ConnectedPing(Packet):
    id = PacketIdentifiers.ConnectedPing
    
    time = None
    
    def encodePayload(self):
        self.putLong(self.time)
        
    def decodePayload(self):
        self.time = self.getLong()
