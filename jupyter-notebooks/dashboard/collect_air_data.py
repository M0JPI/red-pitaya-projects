import serial
import struct
import time
import math
from pms5003 import PMS5003



#Grove analog temperature sensor V1.2 
def res_to_temp(Rntc):
    B = 4275; # B value of the thermistor
    return (1.0/(math.log10(Rntc/100000.0)/B+1/298.15)-273.15) #convert to temperature via datasheet 

#PMS5003 particle sensor
pms5003 = PMS5003(device='/dev/ttyPS1',baudrate=9600)

#Grove Multichannel Gas Sensor V2
import gas_gmxxxb
gas_gmxxxb = gas_gmxxxb.GAS_GMXXX()

#BME680 Temperature, Pressure, Humidity & Gas Sensor
import bme680
bme_680 = bme680.BME680()

#Analog sensors setup
from redpitaya.overlay.mercury import mercury as FPGA
ANALOG_TEMP = FPGA.analog_in(1)
def reset_initial_values():
    voc_air_ref = voc_air_pin.read()
    alcohol_air_ref = analog_alcohol_pin.read()
    return voc_air_ref,alcohol_air_ref;

def analog_temp():
    Va0=ANALOG_TEMP.read() # read voltage of sensor
    R0 = 100000;       # R0 = 100k
    Rntc = 3.3/(Va0)-1.0 
    Rntc = 100000.0*Rntc # thermistor resistance
    return res_to_temp(Rntc);

voc_air_pin = FPGA.analog_in(2) # define which pin will be used for VOC sensor
voc_air_ref = 0.140 #Refrence value considered zero VOC
def analog_voc_ratio():
    voc_volt = voc_air_pin.read()
    voc_gas = voc_volt/(5.0)
    return (voc_gas/voc_air_ref)*3;

analog_alcohol_pin = FPGA.analog_in(3) # define which pin will be used for alcohol sensor
alcohol_air_ref = 1.885
def analog_alcohol_ratio():
    alcohol_volt = analog_alcohol_pin.read()
    alcohol_gas = alcohol_volt/(5.0-alcohol_volt)
    return 1/(alcohol_gas/alcohol_air_ref);

#class BME680(BME680Data):
#    def __init__(self,