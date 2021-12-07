from machine import ADC, Pin
adc = ADC(Pin(28))     # create ADC object on ADC pin
adc.read_u16()
adc2 = ADC(Pin(29))     # create ADC object on ADC pin
adc2.read_u16()

print(adc.read_u16()*3.3/65535)
print(adc2.read_u16()*3.3/65535)
