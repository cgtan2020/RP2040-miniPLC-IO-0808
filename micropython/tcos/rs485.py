import machine
from machine import Pin
from machine import UART

class _RS485:
    def __init__(self):
        self._txen_n = Pin(18, mode=Pin.OUT)
        self.init()

    def init(self, baudrate=9600, bits=8, parity=None, stop=1, **kwargs):
       self._uart = UART(1, baudrate=baudrate, bits=bits, parity=parity, stop=stop, tx=Pin(4), rx=Pin(5), **kwargs)

    def __getattr__(self, attr):
        return getattr(self._uart, attr)
    
    def txen(self, enable):
        self._txen_n(not enable)
        
RS485 = _RS485()

# initialize the port with given baudrate and timeouts
RS485.init(baudrate=9600, timeout=1000, timeout_char=1000)

# Unset TX-enable line to get ready to receive data
RS485.txen(True)
RS485.write("hellodsdsdsdsdsdsd")
RS485.txen(False)

while True:
    line = RS485.readline()
    print(line)
    
    
    RS485.txen(True) # Set TX-enable line before sending response 
    RS485.write("hello1")
    RS485.txen(False)
