'''
Utility library for TCOS RP2040-miniPLC-IO-0808

Copyright (C) 2021 TCOS System Sdn Bhd - All rights reserved.
Date: 03-Dec-2021
Revision: 1.0.0

For information, see:
http://www.tcosystem.com/

This code is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
See file LICENSE.txt for further informations on licensing terms.
'''

from micropython import const
from machine import UART
from tcos.io import *

__version__ = '1.0.0'

class IO:
    PIN_DO1 = const(18)
    PIN_DO2 = const(19)
    PIN_DO3 = const(20)
    PIN_DO4 = const(21)
    PIN_DO5 = const(22)
    PIN_DO6 = const(23)
    PIN_DO7 = const(24)
    PIN_DO8 = const(26)
    
    PIN_DI1 = const(6)
    PIN_DI2 = const(7)
    PIN_DI3 = const(12)
    PIN_DI4 = const(13)
    PIN_DI5 = const(14)
    PIN_DI6 = const(15)
    PIN_DI7 = const(16)
    PIN_DI8 = const(17)

    PIN_HB = const(25)
    
    def __init__(self):
        self.DO1 = DigitalPin('DO1', PIN_DO1, mode=Pin.OUT)
        self.DO2 = DigitalPin('DO2', PIN_DO2, mode=Pin.OUT)
        self.DO3 = DigitalPin('DO3', PIN_DO3, mode=Pin.OUT)
        self.DO4 = DigitalPin('DO4', PIN_DO4, mode=Pin.OUT)
        self.DO5 = DigitalPin('DO4', PIN_DO5, mode=Pin.OUT)
        self.DO6 = DigitalPin('DO4', PIN_DO6, mode=Pin.OUT)
        self.DO7 = DigitalPin('DO4', PIN_DO7, mode=Pin.OUT)
        self.DO8 = DigitalPin('DO4', PIN_DO8, mode=Pin.OUT)
        
        self._all = [self.DO1, self.DO2, self.DO3, self.DO4,self.DO5,self.DO6,self.DO7,self.DO8]

        self.DI1 = DigitalPin('DI1', PIN_DI1, mode=Pin.IN)
        self.DI2 = DigitalPin('DI2', PIN_DI2, mode=Pin.IN)
        self.DI3 = DigitalPin('DI3', PIN_DI3, mode=Pin.IN)
        self.DI4 = DigitalPin('DI4', PIN_DI4, mode=Pin.IN)
        self.DI5 = DigitalPin('DI5', PIN_DI5, mode=Pin.IN)
        self.DI6 = DigitalPin('DI6', PIN_DI6, mode=Pin.IN)
        self.DI7 = DigitalPin('DI7', PIN_DI7, mode=Pin.IN)
        self.DI8 = DigitalPin('DI8', PIN_DI8, mode=Pin.IN)

        self._all.append(self.DI1)
        self._all.append(self.DI2)
        self._all.append(self.DI3)
        self._all.append(self.DI4)
        self._all.append(self.DI5)
        self._all.append(self.DI6)
        self._all.append(self.DI7)
        self._all.append(self.DI8)
        
    def all(self):
        return self._all
    
class _RS232_1:
    def __init__(self):
        self.init(self)

    def init(self, port_no,baudrate=9600, bits=8, parity=None, stop=1, **kwargs):
        self._uart = UART(1, baudrate=baudrate, bits=bits, parity=parity, stop=stop, tx=Pin(4), rx=Pin(5), **kwargs)
        

    def __getattr__(self, attr):
        return getattr(self._uart, attr)
    
RS232_1 = _RS232_1()
    
class _RS232_0:
    def __init__(self):
        self.init(self)

    def init(self, port_no,baudrate=9600, bits=8, parity=None, stop=1, **kwargs):
        self._uart = UART(0, baudrate=baudrate, bits=bits, parity=parity, stop=stop, tx=Pin(0), rx=Pin(1), **kwargs)
        

    def __getattr__(self, attr):
        return getattr(self._uart, attr)
    
RS232_0 = _RS232_0()
    

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