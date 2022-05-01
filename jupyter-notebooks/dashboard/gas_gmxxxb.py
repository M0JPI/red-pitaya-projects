##    Multichannel_Gas_GMXXX.cpp
##    Description: A drive for Seeed Grove Multichannel gas sensor V2.0.
##    2019 Copyright (c) Seeed Technology Inc.  All right reserved.
##    Author: Hongtai Liu(lht856@foxmail.com) ported to Python by John Bracegirdle M0JPI
##    2019-6-18

##    The MIT License (MIT)
##    Permission is hereby granted, free of charge, to any person obtaining a copy
##    of this software and associated documentation files (the "Software"), to deal
##    in the Software without restriction, including without limitation the rights
##    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
##    copies of the Software, and to permit persons to whom the Software is
##    furnished to do so, subject to the following conditions:
##    The above copyright notice and this permission notice shall be included in
##    all copies or substantial portions of the Software.
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
##    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
##    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
##    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
##    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
##    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
##    THE SOFTWARE.1  USA
    

from smbus2 import SMBus, i2c_msg

__version__ = '1.1.1'

class GAS_GMXXX():
    GM_102B = 0x01
    GM_302B = 0x03
    GM_502B = 0x05
    GM_702B = 0x07
    CHANGE_I2C_ADDR = 0x55
    WARMING_UP = 0xFE
    WARMING_DOWN = 0xFF
    
    i2c_address=0x08
    isPreheated = True
    _i2c=None
    
    def __init__(self,i2c_addr=0x08, i2c_device=None, isPreheated = True):
        """Initialise GAS_GMXXX sensor instance.

        :param i2c_addr: Optional i2c address of GAS_GMXXX
        :param i2c_device: Optional SMBus-compatible instance for i2c transport
        :param isPreheated: Optional turn on the heater
        """
        self.i2c_address = i2c_addr
        self._i2c = i2c_device
        if self._i2c is None:
            self._i2c = SMBus(0)
        
        self.isPreheated = isPreheated
        if self.isPreheated == True:
            self.preheated()
        else:
            self.unPreheated()
        
    def preheated(self):
        msg = i2c_msg.write(self.i2c_address, [self.WARMING_UP])
        self._i2c.i2c_rdwr(msg)
        self.isPreheated = True
        return True
    
    def unPreheated(self):
        msg = i2c_msg.write(self.i2c_address, [self.WARMING_DOWN])
        self._i2c.i2c_rdwr(msg)
        self.isPreheated = False
        return True
    
    def calcVol(self, adc_value, verf = 3.3, resolution = 1023):
        return (adc_value * verf) / (resolution * 1.0)
    
    def getGM102B_raw(self):
        return int.from_bytes(self._i2c.read_i2c_block_data(self.i2c_address, self.GM_102B,2), byteorder='little')
    
    def getGM102B_volts(self):
        return self.calcVol(self.getGM102B_raw())

    def getGM302B_raw(self):
        return int.from_bytes(self._i2c.read_i2c_block_data(self.i2c_address, self.GM_302B,2), byteorder='little')
    
    def getGM302B_volts(self):
        return self.calcVol(self.getGM302B_raw())   
 
    def getGM502B_raw(self):
        return int.from_bytes(self._i2c.read_i2c_block_data(self.i2c_address, self.GM_502B,2), byteorder='little')
    
    def getGM502B_volts(self):
        return self.calcVol(self.getGM502B_raw())
 
    def getGM702B_raw(self):
        return int.from_bytes(self._i2c.read_i2c_block_data(self.i2c_address, self.GM_702B,2), byteorder='little')
    
    def getGM702B_volts(self):
        return self.calcVol(self.getGM702B_raw())
    
    def change_I2C_Address(self, newAddress):
        self._i2c.write_byte_data(self.i2c_address, self.CHANGE_I2C_ADDR, newAddress)
        self.i2c_address = newAddress