import time
from machine import Pin, PWM
from time import sleep

print(machine.freq())          # get the current frequency of the CPU
machine.freq(240000000) # set the CPU frequency to 240 MHz
# 
# 
pwm = PWM(Pin(27))      # create PWM object from a pin
# print(pwm0.freq())             # get current frequency
# pwm0.freq(20000000)         # set frequency
# print(pwm0.duty_u16())         # get current duty cycle, range 0-65535
# pwm0.duty_u16(35767)      # set duty cycle, range 0-65535


# # Set the PWM frequency.
# pwm.freq(2000000)
# 
# # Fade the LED in and out a few times.
# duty = 0
# direction = 10
# for _ in range(65536):
#     duty += direction
#     if duty > 65536:
#         duty = 65536
#         direction = -10
#     elif duty < 0:
#         duty = 0
#         direction = 10
#     pwm.duty_u16(duty)
#     print(duty)
#     time.sleep(0.01)

from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep


@asm_pio(sideset_init=PIO.OUT_LOW)
def pwm_prog():
    pull(noblock) .side(0)
    mov(x, osr) # Keep most recent pull data stashed in X, for recycling by noblock
    mov(y, isr) # ISR must be preloaded with PWM count max
    label("pwmloop")
    jmp(x_not_y, "skip")
    nop()         .side(1)
    label("skip")
    jmp(y_dec, "pwmloop")


class PIOPWM:
    def __init__(self, sm_id, pin, max_count, count_freq):
        self._sm = StateMachine(sm_id, pwm_prog, freq=2 * count_freq, sideset_base=Pin(pin))
        # Use exec() to load max count into ISR
        self._sm.put(max_count)
        self._sm.exec("pull()")
        self._sm.exec("mov(isr, osr)")
        self._sm.active(1)
        self._max_count = max_count

    def set(self, value):
        # Minimum value is -1 (completely turn off), 0 actually still produces narrow pulse
        value = max(value, -1)
        value = min(value, self._max_count)
        self._sm.put(value)


# Pin 25 is LED on Pico boards
pwm = PIOPWM(0, 27, max_count=(1 << 16) - 1, count_freq=50_000_000)

# while True:
#     for i in range(65536):
#         pwm.set(i)
#         print (i)
#         sleep(0.000001)
# 
#     for i in reverse(range(65536)):
#         pwm.set(i )
#         print (i)
#         sleep(0.000001)
# 
# 
