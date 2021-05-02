import wiringpi
PIN_TO_SENSE = 29

def gpio_callback():
    print("GPIO_CALLBACK!")
    value = wiringpi.digitalRead(PIN_TO_SENSE)
    print("value: "+str(value))


wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_SENSE, wiringpi.GPIO.INPUT)
wiringpi.pullUpDnControl(PIN_TO_SENSE, wiringpi.GPIO.PUD_UP)

wiringpi.wiringPiISR(PIN_TO_SENSE, wiringpi.GPIO.INT_EDGE_BOTH, gpio_callback)

while True:
    wiringpi.delay(2000)
