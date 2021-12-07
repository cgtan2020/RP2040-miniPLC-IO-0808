import machine
import sdcard
import uos
from machine import Pin, SPI

cs = machine.Pin(9, machine.Pin.OUT)

#spi = SPI(1, baudrate=100000, polarity=0, phase=0, bits=8, firstbit = machine.SPI.MSB,sck=machine.Pin(10,machine.Pin.OUT), mosi=machine.Pin(11,machine.Pin.IN), miso=machine.Pin(8,machine.Pin.OUT))
spi = SPI(1, 10_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(8))

sd = sdcard.SDCard(spi,cs)





#vfs = uos.VfsFat(sd)
uos.mount(sd,'/sd')

with open("/sd/test01.txt", "w") as file:
    file.write("Hello, SD World!\r\n")
    file.write("This is a test\r\n")
    
with open("/sd/test01.txt", "r") as file:
    data = file.read()
    print(data)
    
    
    