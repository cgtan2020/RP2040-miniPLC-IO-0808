from machine import Pin, SPI
import sdcard

def sdrawtest():
    cs = machine.Pin(9, machine.Pin.OUT)

#spi = SPI(1, baudrate=100000, polarity=0, phase=0, bits=8, firstbit = machine.SPI.MSB,sck=machine.Pin(10,machine.Pin.OUT), mosi=machine.Pin(11,machine.Pin.IN), miso=machine.Pin(8,machine.Pin.OUT))
    spi = SPI(1, 400_000, sck=Pin(10), mosi=Pin(11), miso=Pin(8))
    #sd = sdcard.SDCard(SPI(1), Pin(9))
    sd = sdcard.SDCard(spi, cs)    
    buf = bytearray(512)
    
    sd.readblocks(0, buf)
    
    for i in range(0, 512):
        if i % 16 == 8:
            print('    ',end='')
            
        if i % 16 == 0:
            print()
            print('{:04X}'.format(i), end=': ')
    
        print('{:02X}'.format(buf[i]), end=' ')
    
sdrawtest()