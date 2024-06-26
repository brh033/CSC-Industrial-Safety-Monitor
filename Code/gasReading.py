import RPi.GPIO as GPIO

SPICLK = 11
SPIMISO = 9
SPIMOSI =10
SPICS = 8
MQ2_APIN = 0

def init():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(SPIMOSI,GPIO.OUT)
    GPIO.setup(SPIMISO,GPIO.IN)
    GPIO.setup(SPICLK,GPIO.OUT)
    GPIO.setup(SPICS,GPIO.OUT)


def readadc(adcnum,clockpin,mosipin,misopin,cspin):
    init()
    if((adcnum>7)or(adcnum<0)):
        return -1
    GPIO.output(cspin,True)

    GPIO.output(clockpin,False)
    GPIO.output(cspin,False)

    commandout = adcnum
    commandout |= 0x18 #start bit +  single-ended bit
    commandout <<=3 #we only need to send 5 bits here

    for i in range(5):
        if(commandout & 0x80):
            GPIO.output(mosipin,True)
        else:
            GPIO.output(mosipin,False)
        
        commandout <<= 1
        GPIO.output(clockpin,True)
        GPIO.output(clockpin,False)

    adcout = 0

    for i in range(12):
        GPIO.output(clockpin,True)
        GPIO.output(clockpin,False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1
    
    GPIO.output(cspin,True)

    adcout >>= 1 # first bit is 'null' so drop it
    return adcout



while True:
    gas_level = readadc(MQ2_APIN,SPICLK,SPIMOSI,SPIMISO,SPICS)

    air_quality = ((gas_level/1024.)*3.3)