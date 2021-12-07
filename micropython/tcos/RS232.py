from machine import UART, Pin

#There are two UARTs, UART0 and UART1. UART0 can be mapped to GPIO 0/1  and UART1 to GPIO 4/5 For TCOS RP2040 MiniPLC


uart1 = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
uart1.write('hello world\n\r')  # write 13 bytes
uart1.read(5)         		# read 5 bytes



    
    