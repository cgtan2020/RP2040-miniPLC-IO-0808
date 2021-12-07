import time
import machine 
from machine import I2C
import os
import _thread
import utime
from time import sleep
from machine import Timer
from machine import Pin
#from machine import SD
from time import sleep_ms, ticks_ms
from _thread import start_new_thread
import gc
from machine import UART
import ds3231
from ds3231 import DS3231 #Our RTC clock



#i2c = I2C(0)   # default assignment: scl=Pin(9), sda=Pin(8)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=100_000)

# Get the hardware clock into the Pycom clock
# 
# i2c = I2C(2, pins=('P11','P12'))
# i2c.init(I2C.MASTER,baudrate = 100000)


print(i2c.scan())

ds = DS3231(i2c) 
#ds.set_time(2021,8,23,15,45,30,3,0)
#print(ds.get_time())
mytime = ds.get_time()
print(mytime)

# RTC format is YYMMDD,Day, HHMMSS, TIMEZONE

rtc = machine.RTC()
print(rtc.datetime())

rtc.datetime((mytime[0], mytime[1], mytime[2], 0,mytime[3], mytime[4], mytime[5], 0))
print(rtc.datetime())
myrtc = rtc.datetime()
DateStr = '{0:04d}'.format(myrtc[0])+'{0:02d}'.format(myrtc[1])+'{0:02d}'.format(myrtc[2])+'{0:02d}'.format(myrtc[4])+'{0:02d}'.format(myrtc[5])+'{0:02d}'.format(myrtc[6])
print(DateStr)

