import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import os

# Tutorial:
#    https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan1 = AnalogIn(ads, ADS.P0)
chan2 = AnalogIn(ads, ADS.P1)
chan3 = AnalogIn(ads, ADS.P2)
chan4 = AnalogIn(ads, ADS.P3)

f= open("lightdata.csv","a+")

try:
    while True:
        vals = "{0}, {1:.2f}, {2:.2f}, {3:.2f}, {4:.2f}\n".format(int(time.time()), chan1.voltage, chan2.voltage, chan3.voltage, chan4.voltage)
        print(vals)
        f.write(vals)
        f.flush()
        os.fsync(f)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    f.close()