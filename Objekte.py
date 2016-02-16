from tkinter import *
import time
import threading

# Klasse fuer einfache Objekte, Licht an- und ausschalten (Schalter)
class LichtObjekt(Frame, threading.Thread):
    COLOR_DISABLED = "#fcc"
    COLOR_WAITING = "#ffaf4b"
    COLOR_ENABLED = "#cfc"
    def __init__(self, master, text, port, module):
        Frame.__init__(self, master)
        threading.Thread.__init__(self)
        self._Label = Label(self, text=text, anchor=E, bg=self.COLOR_DISABLED)
        self._Label.place(x=0, y=0, width=200, height=25)
        self._Button = Button(self, text="Anschalten", command=self.__pressed)
        self._Button.place(x=200, y=0, width=200, height=25)
        self._port = port
        self._on = False
        self._module = module
        self._threaded = False

    def __pressed(self):
        if (not self._threaded):
            if self._on:
                self.switchOff()
            else:
                self.switchOn()

    def switchOn(self):
        if (not self._on):
            self._module.switchOn(self._port)
            self._Label.config(bg=self.COLOR_ENABLED)
            self._Button.config(text="Ausschalten")
            self._on = True

    def switchOff(self):
        if (self._on):
            self._module.switchOff(self._port)
            self._Label.config(bg=self.COLOR_DISABLED)
            self._Button.config(text="Anschalten")
            self._on = False

    def disable(self):
        self._Button.config(state=DISABLED)

    def enable(self):
        self._Button.config(state=NORMAL)



# Klasse fuer z.B. Strassenlaternen
class ComplexLichtObjekt(LichtObjekt):
    def __init__(self, master, text, port1, port2, delayOn, delayOff, module):
        LichtObjekt.__init__(self, master, text, port1, module)
        self._port2 = port2
        self._delayOn = delayOn
        self._delayOff = delayOff
        self._Button.config(command=self.__pressed)


    def __pressed(self):
        if self._on:
            self.switchOff()
        else:
            self.switchOn()

    def switchOn(self):
        if (not self._on):
            self._module.switchOn(self._port)
            self._Label.config(bg=self.COLOR_WAITING)
            self._Button.config(text="Wird angeschaltet", state=DISABLED)
            time.sleep(self._delayOn)
            self._module.switchOn(self._port2)
            self._Label.config(bg=self.COLOR_ENABLED)
            self._Button.config(text="Ausschalten", state=NORMAL)
            self._on = True

    def switchOff(self):
        if (self._on):
            self._module.switchOff(self._port2)
            self._Label.config(bg=self.COLOR_WAITING)
            self._Button.config(text="Wird ausgeschaltet", state=DISABLED)
            time.sleep(self._delayOff)
            self._module.switchOff(self._port)
            self._Label.config(bg=self.COLOR_DISABLED)
            self._Button.config(text="Anschalten", state=NORMAL)
            self._on = False

class StralatLichtObjekt(LichtObjekt):
    def __init__(self):
        pass


class DelayedShutdown(threading.Thread):
    def __init__(self, lichtObjekt, laufzeit):
        threading.Thread.__init__(self)
        self.__object = lichtObjekt
        self.__laufzeit = laufzeit

    def run(self):
        self.__object.disable()
        self.__object.switchOn()
        time.sleep(self.__laufzeit)
        self.__object.switchOff()
        self.__object.enable()
        
