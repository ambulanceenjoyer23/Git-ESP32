<<<<<<< HEAD
print("hello")
=======
from machine import ADC,Pin,DAC 
import time 
 

'''Hard reset ESP32 (press EN/RST button) after each run due to absence of deinit() for inbuilt DAC,
or you'll get   File "<stdin>", line 7, in <module>
            OSError: (-259, 'ESP_ERR_INVALID_STATE')
'''
adc=ADC(Pin(36)) 
adc.atten(ADC.ATTN_11DB) 
adc.width(ADC.WIDTH_12BIT) 
dac =DAC(Pin(25)) #Hard reset ESP32 after each run due to absence of deinit() for inbuilt DAC

try: 
    while True:
        #ADC to voltage to DAC 
        adcVal=adc.read() #Max bits is 4095
        voltage=(adcVal/4095.0) * 3.3
        dacVal=int((voltage/3.3) * 255) #Convert voltage to digital value, max DAC value is 255
        #dac.write(dacVal)
        print(f"ADC value: {adcVal}, Voltage: {voltage}, DAC value: {dacVal}")
        dac.write(dacVal) #Change led intensity
        time.sleep_ms(300)
except: 
    pass 

>>>>>>> cb60dcd (Sensor commit)
