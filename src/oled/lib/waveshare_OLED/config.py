# /*****************************************************************************
# * | File        :	  config.py
# * | Author      :   Waveshare team
# * | Function    :   Hardware underlying interface,for Raspberry pi
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2020-06-17
# * | Info        :   
# ******************************************************************************/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import time
from smbus import SMBus
import spidev
import ctypes

from gpiozero import LED

# Pin definition
RST_PIN         = 27
DC_PIN          = 25
CS_PIN          = 21

Device_SPI = 1
Device_I2C = 0

if(Device_SPI == 1):
    Device = Device_SPI
    spi = spidev.SpiDev(0, 0)
else :
    Device = Device_I2C
    address = 0x3c
    bus = SMBus(1)

rst = LED(RST_PIN)
dc = LED(DC_PIN)
cs = LED(CS_PIN)
# rst = 1
# dc = 1
# cs = 1

def delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_writebyte(data):
    spi.writebytes([data[0]])

def i2c_writebyte(reg, value):
    bus.write_byte_data(address, reg, value)
   
def module_init():
    #print("module_init")
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(RST_PIN, GPIO.OUT)

    global rst
    global dc
    global cs

    # if rst != 1:
    #     rst.close()
    # rst = LED(RST_PIN)

    # GPIO.setup(DC_PIN, GPIO.OUT)
    # if dc != 1:
    #     dc.close()
    # dc = LED(DC_PIN)

    # GPIO.setup(CS_PIN, GPIO.OUT)
    # cs.close()
    # cs = LED(CS_PIN)

    # GPIO.output(RST_PIN, 0)
    rst.off()
    if(Device == Device_SPI):
        spi.max_speed_hz = 10000000
        spi.mode = 0b11  
    # GPIO.output(CS_PIN, 0)
    cs.off()
    # GPIO.output(DC_PIN, 0)
    dc.off()

    return 0

def module_exit():
    if(Device == Device_SPI):
        spi.close()
    else :
        bus.close()
    # GPIO.output(RST_PIN, 0)
    # GPIO.output(DC_PIN, 0)

    rst.off()
    dc.off()
    

### END OF FILE ###
