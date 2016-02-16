class SMBus(object):
    def __init__(self, port):
        pass
    def write_byte(self, address, data):
        print(address, bin(data)[2:].zfill(8))
