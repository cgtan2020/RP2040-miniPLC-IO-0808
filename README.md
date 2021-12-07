# RP2040-miniPLC-IO-0808
RP2040 based miniPLC with 8 Digital Input and Output, I2C, SDCard Support, PWM, RS232, RS485 and Analogue Input

1. 07-Dec-2021 Updated sample python code to demo the board capabilities

pwm.py - High Speed PWM using PIO functions of the RP2040/r/r
sd_fat.py - FAT files access to SDCard using SPI functions
sd_rawtest.py - RAW access to SDCard using SPI functions.
RS232.py - Write and Read from RS232 port
rs485.py - half duplex Write and Read from RS485 port
DigitalIO.py - Read Digital Input and Set Digital Outout
RTC.py - Set the optional RTC clock link to the I2C pins
ADC.py - Read the Analogue Pins of the board
