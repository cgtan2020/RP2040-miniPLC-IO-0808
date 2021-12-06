from machine import Pin
from machine import ADC
from machine import PWM

class DigitalPin(Pin):
    def __init__(self, name, pin, mode=None):
        super().__init__(pin, mode, None)
        self._name = name

    def name(self):
        return self._name
