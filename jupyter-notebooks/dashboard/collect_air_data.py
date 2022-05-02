import serial
import struct
import time
import math
from pms5003 import PMS5003

#Grove Multichannel Gas Sensor V2
import gas_gmxxxb

#BME680 Temperature, Pressure, Humidity & Gas Sensor
import bme680

#Analog sensors setup
from redpitaya.overlay.mercury import mercury as FPGA

class collect_air_object():
    #Grove Multichannel Gas Sensor V2
    gas_gmxxxb = gas_gmxxxb.GAS_GMXXX()
    
    #PMS5003 particle sensor
    pms5003 = None
    UART_device = None
    
    #BME680 Temperature, Pressure, Humidity & Gas Sensor
    bme_680 = None
    
    #Analog sensors setup
    ANALOG_TEMP = None
    voc_air_pin = None # define which pin will be used for VOC sensor
    voc_air_ref = 0.2157 #Refrence value considered zero VOC
    analog_alcohol_pin = FPGA.analog_in(3) # define which pin will be used for alcohol sensor
    alcohol_air_ref = 2.3864
    
    #Digital sensors setup
    GM102B_ref = 1.6516
    GM302B_ref = 1.2871
    GM502B_ref = 1.0097
    GM702B_ref = 0.9516
    
    def __init__(self,UART_object='/dev/ttyPS1', 
                 bme_680_object = bme680.BME680(i2c_addr=0x76, i2c_device=None),
                 ANALOG_TEMP_pin = FPGA.analog_in(1),
                 voc_pin = FPGA.analog_in(2)):
        
        self.bme_680 = bme_680_object
        self.UART_device = UART_object
        self.pms5003 = PMS5003(UART_object,baudrate=9600)
        self.ANALOG_TEMP = ANALOG_TEMP_pin
        self.voc_air_pin = voc_pin
    
    #Grove analog temperature sensor V1.2 
    def res_to_temp(self,Rntc):
        B = 4275; # B value of the thermistor
        return (1.0/(math.log10(Rntc/100000.0)/B+1/298.15)-273.15) #convert to temperature via datasheet 
    
    def reset_ref_values(self):
        self.voc_air_ref = self.voc_air_pin.read()
        self.alcohol_air_ref = self.analog_alcohol_pin.read()
        self.GM102B_ref = self.gas_gmxxxb.getGM102B_volts()
        self.GM302B_ref = self.gas_gmxxxb.getGM302B_volts()
        self.GM502B_ref = self.gas_gmxxxb.getGM502B_volts()
        self.GM702B_ref = self.gas_gmxxxb.getGM702B_volts()
        return self.voc_air_ref,self.alcohol_air_ref,self.GM102B_ref,self.GM302B_ref,self.GM502B_ref,self.GM702B_ref;
    
    def analog_temp(self):
        Va0=self.ANALOG_TEMP.read() # read voltage of sensor
        R0 = 100000;       # R0 = 100k
        Rntc = 3.3/(Va0)-1.0 
        Rntc = 100000.0*Rntc # thermistor resistance
        return self.res_to_temp(Rntc);
    
    def analog_voc_ratio(self):
        self.voc_volt = self.voc_air_pin.read()
        return (self.voc_volt/self.voc_air_ref);
    
    def analog_alcohol_ratio(self):
        self.alcohol_volt = self.analog_alcohol_pin.read()
        return 1/(self.alcohol_volt/self.alcohol_air_ref);