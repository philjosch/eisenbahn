from tkinter import *
from Steuerung import *
from smbus import *
from Objekte import *
import random



class LichtSteuerung(Tk):
    def __init__(self, port):
        Tk.__init__(self)
        self.title("Lichtsteuerung fuer die Eisenbahn")
        
        self.geometry("400x400")

        self.__port = port
        self.__bus = SMBus(self.__port)
        self.__module1 = Steuerung(self.__bus, 0x20)


        # Die Einzelnen Buttons zur Steuerung des Lichtes
        self.__caffee = LichtObjekt(self, "Cafe", 0, self.__module1)
        self.__caffee.place(x=0, y=0, width=400, height=25)

        self.__stralat = ComplexLichtObjekt(self, "Strassenlaternen", 1, 2, 0.1, 1, self.__module1)
        self.__stralat.place(x=0, y=25, width=400, height=25)

        self.__kirche = LichtObjekt(self, "Kirche", 3, self.__module1)
        self.__kirche.place(x=0, y=50, width=400, height=25)

        self.__flutlicht = LichtObjekt(self, "Flutlicht", 4, self.__module1)
        self.__flutlicht.place(x=0, y=75, width=400, height=25)

        self.__hammerschmiede = LichtObjekt(self, "Hammerschmiede", 5, self.__module1)
        self.__hammerschmiede.place(x=0, y=100, width=400, height=25)

        self.__2famhaus = LichtObjekt(self, "2-Familienhaus", 6, self.__module1)
        self.__2famhaus.place(x=0, y=125, width=400, height=25)

        self.__neubau1 = LichtObjekt(self, "Neubau 1", 7, self.__module1)
        self.__neubau1.place(x=0, y=150, width=400, height=25)

        self.__objects = [self.__caffee, self.__stralat, self.__kirche,
                          self.__flutlicht, self.__hammerschmiede, self.__2famhaus,
                          self.__neubau1]

        Label(self, text="Spezielle Funktionen:").place(x=0, y=175, width=400, height=25)
        self.__alle = Frame(self)
        self.__alle.place(x=0, y=200, width=400, height=50)

        self.__alleAnButton = Button(self.__alle, text="Alle Anschalten", command=self.alleAn)
        self.__alleAnButton.place(x=0, y=0, width=200, height=25)

        self.__alleAusButton = Button(self.__alle, text="Alle Ausschalten", command=self.alleAus)
        self.__alleAusButton.place(x=200, y=0, width=200, height=25)

        self.__gottesdienstButton = Button(self.__alle, text="Gottesdienst", command=self.gottesdienst)
        self.__gottesdienstButton.place(x=0, y=25, width=200, height=25)

        self.__randomButton = Button(self.__alle, text="Zufaelliges Schalten", command=self.random)
        self.__randomButton.place(x=200, y=25, width=200, height=25)

    def alleAn(self):
        for i in self.__objects:
            i.switchOn()

    def alleAus(self):
        for i in self.__objects:
            i.switchOff()

    # Spezielle Programme zum Ablauf der Lichtsteuerung
    def gottesdienst(self):
        self.__kirchenThread = DelayedShutdown(self.__kirche, 30)
        self.__kirchenThread.start()

    def random(self):
        for i in self.__objects:
            if (random.random() < 0.5):
                i.switchOn()
            else:
                i.switchOff()


if __name__ == "__main__":
    App = LichtSteuerung(0)
    App.mainloop()
