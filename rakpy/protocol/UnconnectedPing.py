from rakpy.protocol.Packet import Packet
from rakpy.protocol.PacketIdentifiers import PacketIdentifiers

class UnconnectedPing(Packet):
    PID = PacketIdentifiers.UnconnectedPing
    
    time = 0
    clientID = 0
    
    def encodePayload(self):
        self.putLong(self.time)
        self.putMagic()
        self.putLong(self.clientID)
        
    def decodePayload(self):
        self.time = self.getLong()
        self.magic = self.getMagic()
        self.clientID = self.getLong()
    
