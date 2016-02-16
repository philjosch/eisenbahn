class Steuerung:
    ELEMENTS_PER_MODULE = 8
    def __init__(self, bus, address):
        self.__address = address
        self.__bus = bus
        self.__current = [0]*self.ELEMENTS_PER_MODULE
        self.__publish()

    def switchOn(self, number):
        self.__current[number] = 1
        self.__publish()

    def switchOff(self, number):
        self.__current[number] = 0
        self.__publish()

    def __publish(self):
        ausgabe = 0
        for i in range(1, 1+self.ELEMENTS_PER_MODULE):
            ausgabe = ausgabe*2
            if self.__current[-i] == 0:
                ausgabe += 1
        self.__bus.write_byte(self.__address, ausgabe)
        
    def switchOffAll(self):
        self.__current = [0]*self.ELEMENTS_PER_MODULE
        self.__publish()
        
    def switchOnAll(self):
        self.__current = [1]*self.ELEMENTS_PER_MODULE
        self.__publish()
