import serial
import struct
import time
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
Bme680 = bme680.BME680()