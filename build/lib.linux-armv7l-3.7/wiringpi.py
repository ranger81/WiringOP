# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_wiringpi')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_wiringpi')
    _wiringpi = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_wiringpi', [dirname(__file__)])
        except ImportError:
            import _wiringpi
            return _wiringpi
        try:
            _mod = imp.load_module('_wiringpi', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _wiringpi = swig_import_helper()
    del swig_import_helper
else:
    import _wiringpi
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def wiringPiISR(pin, mode, PyFunc):
    return _wiringpi.wiringPiISR(pin, mode, PyFunc)
wiringPiISR = _wiringpi.wiringPiISR

def wiringPiFailure(fatal, message):
    return _wiringpi.wiringPiFailure(fatal, message)
wiringPiFailure = _wiringpi.wiringPiFailure

def wiringPiFindNode(pin):
    return _wiringpi.wiringPiFindNode(pin)
wiringPiFindNode = _wiringpi.wiringPiFindNode

def wiringPiNewNode(pinBase, numPins):
    return _wiringpi.wiringPiNewNode(pinBase, numPins)
wiringPiNewNode = _wiringpi.wiringPiNewNode

def wiringPiSetup():
    return _wiringpi.wiringPiSetup()
wiringPiSetup = _wiringpi.wiringPiSetup

def wiringPiSetupSys():
    return _wiringpi.wiringPiSetupSys()
wiringPiSetupSys = _wiringpi.wiringPiSetupSys

def wiringPiSetupGpio():
    return _wiringpi.wiringPiSetupGpio()
wiringPiSetupGpio = _wiringpi.wiringPiSetupGpio

def wiringPiSetupPhys():
    return _wiringpi.wiringPiSetupPhys()
wiringPiSetupPhys = _wiringpi.wiringPiSetupPhys

def pinModeAlt(pin, mode):
    return _wiringpi.pinModeAlt(pin, mode)
pinModeAlt = _wiringpi.pinModeAlt

def pinMode(pin, mode):
    return _wiringpi.pinMode(pin, mode)
pinMode = _wiringpi.pinMode

def pullUpDnControl(pin, pud):
    return _wiringpi.pullUpDnControl(pin, pud)
pullUpDnControl = _wiringpi.pullUpDnControl

def digitalRead(pin):
    return _wiringpi.digitalRead(pin)
digitalRead = _wiringpi.digitalRead

def digitalWrite(pin, value):
    return _wiringpi.digitalWrite(pin, value)
digitalWrite = _wiringpi.digitalWrite

def pwmWrite(pin, value):
    return _wiringpi.pwmWrite(pin, value)
pwmWrite = _wiringpi.pwmWrite

def analogRead(pin):
    return _wiringpi.analogRead(pin)
analogRead = _wiringpi.analogRead

def analogWrite(pin, value):
    return _wiringpi.analogWrite(pin, value)
analogWrite = _wiringpi.analogWrite

def piBoardRev():
    return _wiringpi.piBoardRev()
piBoardRev = _wiringpi.piBoardRev

def piBoardId(model, rev, mem, maker, overVolted):
    return _wiringpi.piBoardId(model, rev, mem, maker, overVolted)
piBoardId = _wiringpi.piBoardId

def wpiPinToGpio(wpiPin):
    return _wiringpi.wpiPinToGpio(wpiPin)
wpiPinToGpio = _wiringpi.wpiPinToGpio

def physPinToGpio(physPin):
    return _wiringpi.physPinToGpio(physPin)
physPinToGpio = _wiringpi.physPinToGpio

def physPinToPin(physPin):
    return _wiringpi.physPinToPin(physPin)
physPinToPin = _wiringpi.physPinToPin

def setPadDrive(group, value):
    return _wiringpi.setPadDrive(group, value)
setPadDrive = _wiringpi.setPadDrive

def getAlt(pin):
    return _wiringpi.getAlt(pin)
getAlt = _wiringpi.getAlt

def pwmToneWrite(pin, freq):
    return _wiringpi.pwmToneWrite(pin, freq)
pwmToneWrite = _wiringpi.pwmToneWrite

def digitalWriteByte(value):
    return _wiringpi.digitalWriteByte(value)
digitalWriteByte = _wiringpi.digitalWriteByte

def pwmSetMode(mode):
    return _wiringpi.pwmSetMode(mode)
pwmSetMode = _wiringpi.pwmSetMode

def pwmSetRange(range):
    return _wiringpi.pwmSetRange(range)
pwmSetRange = _wiringpi.pwmSetRange

def pwmSetClock(divisor):
    return _wiringpi.pwmSetClock(divisor)
pwmSetClock = _wiringpi.pwmSetClock

def gpioClockSet(pin, freq):
    return _wiringpi.gpioClockSet(pin, freq)
gpioClockSet = _wiringpi.gpioClockSet

def waitForInterrupt(pin, mS):
    return _wiringpi.waitForInterrupt(pin, mS)
waitForInterrupt = _wiringpi.waitForInterrupt

def piThreadCreate(fn):
    return _wiringpi.piThreadCreate(fn)
piThreadCreate = _wiringpi.piThreadCreate

def piLock(key):
    return _wiringpi.piLock(key)
piLock = _wiringpi.piLock

def piUnlock(key):
    return _wiringpi.piUnlock(key)
piUnlock = _wiringpi.piUnlock

def piHiPri(pri):
    return _wiringpi.piHiPri(pri)
piHiPri = _wiringpi.piHiPri

def delay(howLong):
    return _wiringpi.delay(howLong)
delay = _wiringpi.delay

def delayMicroseconds(howLong):
    return _wiringpi.delayMicroseconds(howLong)
delayMicroseconds = _wiringpi.delayMicroseconds

def millis():
    return _wiringpi.millis()
millis = _wiringpi.millis

def micros():
    return _wiringpi.micros()
micros = _wiringpi.micros

def wiringPiI2CRead(fd):
    return _wiringpi.wiringPiI2CRead(fd)
wiringPiI2CRead = _wiringpi.wiringPiI2CRead

def wiringPiI2CReadReg8(fd, reg):
    return _wiringpi.wiringPiI2CReadReg8(fd, reg)
wiringPiI2CReadReg8 = _wiringpi.wiringPiI2CReadReg8

def wiringPiI2CReadReg16(fd, reg):
    return _wiringpi.wiringPiI2CReadReg16(fd, reg)
wiringPiI2CReadReg16 = _wiringpi.wiringPiI2CReadReg16

def wiringPiI2CWrite(fd, data):
    return _wiringpi.wiringPiI2CWrite(fd, data)
wiringPiI2CWrite = _wiringpi.wiringPiI2CWrite

def wiringPiI2CWriteReg8(fd, reg, data):
    return _wiringpi.wiringPiI2CWriteReg8(fd, reg, data)
wiringPiI2CWriteReg8 = _wiringpi.wiringPiI2CWriteReg8

def wiringPiI2CWriteReg16(fd, reg, data):
    return _wiringpi.wiringPiI2CWriteReg16(fd, reg, data)
wiringPiI2CWriteReg16 = _wiringpi.wiringPiI2CWriteReg16

def wiringPiI2CSetupInterface(device, devId):
    return _wiringpi.wiringPiI2CSetupInterface(device, devId)
wiringPiI2CSetupInterface = _wiringpi.wiringPiI2CSetupInterface

def wiringPiI2CSetup(devId):
    return _wiringpi.wiringPiI2CSetup(devId)
wiringPiI2CSetup = _wiringpi.wiringPiI2CSetup

def wiringPiSPIGetFd(channel):
    return _wiringpi.wiringPiSPIGetFd(channel)
wiringPiSPIGetFd = _wiringpi.wiringPiSPIGetFd

def wiringPiSPIDataRW(channel, data):
    return _wiringpi.wiringPiSPIDataRW(channel, data)
wiringPiSPIDataRW = _wiringpi.wiringPiSPIDataRW

def wiringPiSPISetupMode(channel, speed, mode):
    return _wiringpi.wiringPiSPISetupMode(channel, speed, mode)
wiringPiSPISetupMode = _wiringpi.wiringPiSPISetupMode

def wiringPiSPISetup(channel, speed):
    return _wiringpi.wiringPiSPISetup(channel, speed)
wiringPiSPISetup = _wiringpi.wiringPiSPISetup

def serialOpen(device, baud):
    return _wiringpi.serialOpen(device, baud)
serialOpen = _wiringpi.serialOpen

def serialClose(fd):
    return _wiringpi.serialClose(fd)
serialClose = _wiringpi.serialClose

def serialFlush(fd):
    return _wiringpi.serialFlush(fd)
serialFlush = _wiringpi.serialFlush

def serialPutchar(fd, c):
    return _wiringpi.serialPutchar(fd, c)
serialPutchar = _wiringpi.serialPutchar

def serialPuts(fd, s):
    return _wiringpi.serialPuts(fd, s)
serialPuts = _wiringpi.serialPuts

def serialPrintf(fd, message):
    return _wiringpi.serialPrintf(fd, message)
serialPrintf = _wiringpi.serialPrintf

def serialDataAvail(fd):
    return _wiringpi.serialDataAvail(fd)
serialDataAvail = _wiringpi.serialDataAvail

def serialGetchar(fd):
    return _wiringpi.serialGetchar(fd)
serialGetchar = _wiringpi.serialGetchar

def shiftIn(dPin, cPin, order):
    return _wiringpi.shiftIn(dPin, cPin, order)
shiftIn = _wiringpi.shiftIn

def shiftOut(dPin, cPin, order, val):
    return _wiringpi.shiftOut(dPin, cPin, order, val)
shiftOut = _wiringpi.shiftOut

def drcSetupSerial(pinBase, numPins, device, baud):
    return _wiringpi.drcSetupSerial(pinBase, numPins, device, baud)
drcSetupSerial = _wiringpi.drcSetupSerial

def max31855Setup(pinBase, spiChannel):
    return _wiringpi.max31855Setup(pinBase, spiChannel)
max31855Setup = _wiringpi.max31855Setup

def max5322Setup(pinBase, spiChannel):
    return _wiringpi.max5322Setup(pinBase, spiChannel)
max5322Setup = _wiringpi.max5322Setup

def mcp23008Setup(pinBase, i2cAddress):
    return _wiringpi.mcp23008Setup(pinBase, i2cAddress)
mcp23008Setup = _wiringpi.mcp23008Setup

def mcp23016Setup(pinBase, i2cAddress):
    return _wiringpi.mcp23016Setup(pinBase, i2cAddress)
mcp23016Setup = _wiringpi.mcp23016Setup

def mcp23017Setup(pinBase, i2cAddress):
    return _wiringpi.mcp23017Setup(pinBase, i2cAddress)
mcp23017Setup = _wiringpi.mcp23017Setup

def mcp23s08Setup(pinBase, spiPort, devId):
    return _wiringpi.mcp23s08Setup(pinBase, spiPort, devId)
mcp23s08Setup = _wiringpi.mcp23s08Setup

def mcp23s17Setup(pinBase, spiPort, devId):
    return _wiringpi.mcp23s17Setup(pinBase, spiPort, devId)
mcp23s17Setup = _wiringpi.mcp23s17Setup

def mcp3002Setup(pinBase, spiChannel):
    return _wiringpi.mcp3002Setup(pinBase, spiChannel)
mcp3002Setup = _wiringpi.mcp3002Setup

def mcp3004Setup(pinBase, spiChannel):
    return _wiringpi.mcp3004Setup(pinBase, spiChannel)
mcp3004Setup = _wiringpi.mcp3004Setup

def mcp3422Setup(pinBase, i2cAddress, sampleRate, gain):
    return _wiringpi.mcp3422Setup(pinBase, i2cAddress, sampleRate, gain)
mcp3422Setup = _wiringpi.mcp3422Setup

def mcp4802Setup(pinBase, spiChannel):
    return _wiringpi.mcp4802Setup(pinBase, spiChannel)
mcp4802Setup = _wiringpi.mcp4802Setup

def pcf8574Setup(pinBase, i2cAddress):
    return _wiringpi.pcf8574Setup(pinBase, i2cAddress)
pcf8574Setup = _wiringpi.pcf8574Setup

def pcf8591Setup(pinBase, i2cAddress):
    return _wiringpi.pcf8591Setup(pinBase, i2cAddress)
pcf8591Setup = _wiringpi.pcf8591Setup

def sn3218Setup(pinBase):
    return _wiringpi.sn3218Setup(pinBase)
sn3218Setup = _wiringpi.sn3218Setup

def softPwmCreate(pin, value, range):
    return _wiringpi.softPwmCreate(pin, value, range)
softPwmCreate = _wiringpi.softPwmCreate

def softPwmWrite(pin, value):
    return _wiringpi.softPwmWrite(pin, value)
softPwmWrite = _wiringpi.softPwmWrite

def softPwmStop(pin):
    return _wiringpi.softPwmStop(pin)
softPwmStop = _wiringpi.softPwmStop

def softServoWrite(pin, value):
    return _wiringpi.softServoWrite(pin, value)
softServoWrite = _wiringpi.softServoWrite

def softServoSetup(p0, p1, p2, p3, p4, p5, p6, p7):
    return _wiringpi.softServoSetup(p0, p1, p2, p3, p4, p5, p6, p7)
softServoSetup = _wiringpi.softServoSetup

def softToneCreate(pin):
    return _wiringpi.softToneCreate(pin)
softToneCreate = _wiringpi.softToneCreate

def softToneStop(pin):
    return _wiringpi.softToneStop(pin)
softToneStop = _wiringpi.softToneStop

def softToneWrite(pin, freq):
    return _wiringpi.softToneWrite(pin, freq)
softToneWrite = _wiringpi.softToneWrite

def sr595Setup(pinBase, numPins, dataPin, clockPin, latchPin):
    return _wiringpi.sr595Setup(pinBase, numPins, dataPin, clockPin, latchPin)
sr595Setup = _wiringpi.sr595Setup

def ds1302rtcRead(reg):
    return _wiringpi.ds1302rtcRead(reg)
ds1302rtcRead = _wiringpi.ds1302rtcRead

def ds1302rtcWrite(reg, data):
    return _wiringpi.ds1302rtcWrite(reg, data)
ds1302rtcWrite = _wiringpi.ds1302rtcWrite

def ds1302ramRead(addr):
    return _wiringpi.ds1302ramRead(addr)
ds1302ramRead = _wiringpi.ds1302ramRead

def ds1302ramWrite(addr, data):
    return _wiringpi.ds1302ramWrite(addr, data)
ds1302ramWrite = _wiringpi.ds1302ramWrite

def ds1302clockRead(clockData):
    return _wiringpi.ds1302clockRead(clockData)
ds1302clockRead = _wiringpi.ds1302clockRead

def ds1302clockWrite(clockData):
    return _wiringpi.ds1302clockWrite(clockData)
ds1302clockWrite = _wiringpi.ds1302clockWrite

def ds1302trickleCharge(diodes, resistors):
    return _wiringpi.ds1302trickleCharge(diodes, resistors)
ds1302trickleCharge = _wiringpi.ds1302trickleCharge

def ds1302setup(clockPin, dataPin, csPin):
    return _wiringpi.ds1302setup(clockPin, dataPin, csPin)
ds1302setup = _wiringpi.ds1302setup

def gertboardAnalogWrite(chan, value):
    return _wiringpi.gertboardAnalogWrite(chan, value)
gertboardAnalogWrite = _wiringpi.gertboardAnalogWrite

def gertboardAnalogRead(chan):
    return _wiringpi.gertboardAnalogRead(chan)
gertboardAnalogRead = _wiringpi.gertboardAnalogRead

def gertboardSPISetup():
    return _wiringpi.gertboardSPISetup()
gertboardSPISetup = _wiringpi.gertboardSPISetup

def gertboardAnalogSetup(pinBase):
    return _wiringpi.gertboardAnalogSetup(pinBase)
gertboardAnalogSetup = _wiringpi.gertboardAnalogSetup

def lcd128x64setOrigin(x, y):
    return _wiringpi.lcd128x64setOrigin(x, y)
lcd128x64setOrigin = _wiringpi.lcd128x64setOrigin

def lcd128x64setOrientation(orientation):
    return _wiringpi.lcd128x64setOrientation(orientation)
lcd128x64setOrientation = _wiringpi.lcd128x64setOrientation

def lcd128x64orientCoordinates(x, y):
    return _wiringpi.lcd128x64orientCoordinates(x, y)
lcd128x64orientCoordinates = _wiringpi.lcd128x64orientCoordinates

def lcd128x64getScreenSize(x, y):
    return _wiringpi.lcd128x64getScreenSize(x, y)
lcd128x64getScreenSize = _wiringpi.lcd128x64getScreenSize

def lcd128x64point(x, y, colour):
    return _wiringpi.lcd128x64point(x, y, colour)
lcd128x64point = _wiringpi.lcd128x64point

def lcd128x64line(x0, y0, x1, y1, colour):
    return _wiringpi.lcd128x64line(x0, y0, x1, y1, colour)
lcd128x64line = _wiringpi.lcd128x64line

def lcd128x64lineTo(x, y, colour):
    return _wiringpi.lcd128x64lineTo(x, y, colour)
lcd128x64lineTo = _wiringpi.lcd128x64lineTo

def lcd128x64rectangle(x1, y1, x2, y2, colour, filled):
    return _wiringpi.lcd128x64rectangle(x1, y1, x2, y2, colour, filled)
lcd128x64rectangle = _wiringpi.lcd128x64rectangle

def lcd128x64circle(x, y, r, colour, filled):
    return _wiringpi.lcd128x64circle(x, y, r, colour, filled)
lcd128x64circle = _wiringpi.lcd128x64circle

def lcd128x64ellipse(cx, cy, xRadius, yRadius, colour, filled):
    return _wiringpi.lcd128x64ellipse(cx, cy, xRadius, yRadius, colour, filled)
lcd128x64ellipse = _wiringpi.lcd128x64ellipse

def lcd128x64putchar(x, y, c, bgCol, fgCol):
    return _wiringpi.lcd128x64putchar(x, y, c, bgCol, fgCol)
lcd128x64putchar = _wiringpi.lcd128x64putchar

def lcd128x64puts(x, y, str, bgCol, fgCol):
    return _wiringpi.lcd128x64puts(x, y, str, bgCol, fgCol)
lcd128x64puts = _wiringpi.lcd128x64puts

def lcd128x64update():
    return _wiringpi.lcd128x64update()
lcd128x64update = _wiringpi.lcd128x64update

def lcd128x64clear(colour):
    return _wiringpi.lcd128x64clear(colour)
lcd128x64clear = _wiringpi.lcd128x64clear

def lcd128x64setup():
    return _wiringpi.lcd128x64setup()
lcd128x64setup = _wiringpi.lcd128x64setup

def lcdHome(fd):
    return _wiringpi.lcdHome(fd)
lcdHome = _wiringpi.lcdHome

def lcdClear(fd):
    return _wiringpi.lcdClear(fd)
lcdClear = _wiringpi.lcdClear

def lcdDisplay(fd, state):
    return _wiringpi.lcdDisplay(fd, state)
lcdDisplay = _wiringpi.lcdDisplay

def lcdCursor(fd, state):
    return _wiringpi.lcdCursor(fd, state)
lcdCursor = _wiringpi.lcdCursor

def lcdCursorBlink(fd, state):
    return _wiringpi.lcdCursorBlink(fd, state)
lcdCursorBlink = _wiringpi.lcdCursorBlink

def lcdSendCommand(fd, command):
    return _wiringpi.lcdSendCommand(fd, command)
lcdSendCommand = _wiringpi.lcdSendCommand

def lcdPosition(fd, x, y):
    return _wiringpi.lcdPosition(fd, x, y)
lcdPosition = _wiringpi.lcdPosition

def lcdCharDef(fd, index, data):
    return _wiringpi.lcdCharDef(fd, index, data)
lcdCharDef = _wiringpi.lcdCharDef

def lcdPutchar(fd, data):
    return _wiringpi.lcdPutchar(fd, data)
lcdPutchar = _wiringpi.lcdPutchar

def lcdPuts(fd, string):
    return _wiringpi.lcdPuts(fd, string)
lcdPuts = _wiringpi.lcdPuts

def lcdPrintf(fd, message):
    return _wiringpi.lcdPrintf(fd, message)
lcdPrintf = _wiringpi.lcdPrintf

def lcdInit(rows, cols, bits, rs, strb, d0, d1, d2, d3, d4, d5, d6, d7):
    return _wiringpi.lcdInit(rows, cols, bits, rs, strb, d0, d1, d2, d3, d4, d5, d6, d7)
lcdInit = _wiringpi.lcdInit

def maxDetectRead(pin, buffer):
    return _wiringpi.maxDetectRead(pin, buffer)
maxDetectRead = _wiringpi.maxDetectRead

def readRHT03(pin, temp, rh):
    return _wiringpi.readRHT03(pin, temp, rh)
readRHT03 = _wiringpi.readRHT03

def piGlow1(leg, ring, intensity):
    return _wiringpi.piGlow1(leg, ring, intensity)
piGlow1 = _wiringpi.piGlow1

def piGlowLeg(leg, intensity):
    return _wiringpi.piGlowLeg(leg, intensity)
piGlowLeg = _wiringpi.piGlowLeg

def piGlowRing(ring, intensity):
    return _wiringpi.piGlowRing(ring, intensity)
piGlowRing = _wiringpi.piGlowRing

def piGlowSetup(clear):
    return _wiringpi.piGlowSetup(clear)
piGlowSetup = _wiringpi.piGlowSetup

def setupNesJoystick(dPin, cPin, lPin):
    return _wiringpi.setupNesJoystick(dPin, cPin, lPin)
setupNesJoystick = _wiringpi.setupNesJoystick

def readNesJoystick(joystick):
    return _wiringpi.readNesJoystick(joystick)
readNesJoystick = _wiringpi.readNesJoystick

def piFaceSetup(pinBase):
    return _wiringpi.piFaceSetup(pinBase)
piFaceSetup = _wiringpi.piFaceSetup

# wiringPi modes

WPI_MODE_PINS = 0;
WPI_MODE_GPIO = 1;
WPI_MODE_GPIO_SYS = 2;
WPI_MODE_PHYS = 3;
WPI_MODE_PIFACE = 4;
WPI_MODE_UNINITIALISED = -1;

# Pin modes

INPUT = 0;
OUTPUT = 1;
PWM_OUTPUT = 2;
GPIO_CLOCK = 3;
SOFT_PWM_OUTPUT = 4;
SOFT_TONE_OUTPUT = 5;
PWM_TONE_OUTPUT = 6;

LOW = 0;
HIGH = 1;

# Pull up/down/none

PUD_OFF = 0;
PUD_DOWN = 1;
PUD_UP = 2;

# PWM

PWM_MODE_MS = 0;
PWM_MODE_BAL = 1;

# Interrupt levels

INT_EDGE_SETUP = 0;
INT_EDGE_FALLING = 1;
INT_EDGE_RISING = 2;
INT_EDGE_BOTH = 3;

# Shifting (from wiringShift.h)

LSBFIRST = 0;
MSBFIRST = 1;



class nes(object):
  def setupNesJoystick(self,*args):
    return setupNesJoystick(*args)
  def readNesJoystick(self,*args):
    return readNesJoystick(*args)

class Serial(object):
  device = '/dev/ttyAMA0'
  baud = 9600
  serial_id = 0
  def printf(self,*args):
    return serialPrintf(self.serial_id,*args)
  def dataAvail(self,*args):
    return serialDataAvail(self.serial_id,*args)
  def getchar(self,*args):
    return serialGetchar(self.serial_id,*args)
  def putchar(self,*args):
    return serialPutchar(self.serial_id,*args)
  def puts(self,*args):
    return serialPuts(self.serial_id,*args)
  def __init__(self,device,baud):
    self.device = device
    self.baud = baud
    self.serial_id = serialOpen(self.device,self.baud)
  def __del__(self):
    serialClose(self.serial_id)

class I2C(object):
  def setupInterface(self,*args):
  	return wiringPiI2CSetupInterface(*args)
  def setup(self,*args):
    return wiringPiI2CSetup(*args)
  def read(self,*args):
    return wiringPiI2CRead(*args)
  def readReg8(self,*args):
    return wiringPiI2CReadReg8(*args)
  def readReg16(self,*args):
    return wiringPiI2CReadReg16(*args)
  def write(self,*args):
    return wiringPiI2CWrite(*args)
  def writeReg8(self,*args):
    return wiringPiI2CWriteReg8(*args)
  def writeReg16(self,*args):
    return wiringPiI2CWriteReg16(*args)

class GPIO(object):
  WPI_MODE_PINS = 0
  WPI_MODE_GPIO = 1
  WPI_MODE_GPIO_SYS = 2
  WPI_MODE_PHYS = 3
  WPI_MODE_PIFACE = 4
  WPI_MODE_UNINITIALISED = -1

  INPUT = 0
  OUTPUT = 1
  PWM_OUTPUT = 2
  GPIO_CLOCK = 3

  LOW = 0
  HIGH = 1

  PUD_OFF = 0
  PUD_DOWN = 1
  PUD_UP = 2

  PWM_MODE_MS = 0
  PWM_MODE_BAL = 1

  INT_EDGE_SETUP = 0
  INT_EDGE_FALLING = 1
  INT_EDGE_RISING = 2
  INT_EDGE_BOTH = 3

  LSBFIRST = 0
  MSBFIRST = 1

  MODE = 0
  def __init__(self,pinmode=0):
    self.MODE=pinmode
    if pinmode==self.WPI_MODE_PINS:
      wiringPiSetup()
    if pinmode==self.WPI_MODE_GPIO:
      wiringPiSetupGpio()
    if pinmode==self.WPI_MODE_GPIO_SYS:
      wiringPiSetupSys()
    if pinmode==self.WPI_MODE_PHYS:
      wiringPiSetupPhys()
    if pinmode==self.WPI_MODE_PIFACE:
      wiringPiSetupPiFace()

  def delay(self,*args):
    delay(*args)
  def delayMicroseconds(self,*args):
    delayMicroseconds(*args)
  def millis(self):
    return millis()
  def micros(self):
    return micros()

  def piHiPri(self,*args):
    return piHiPri(*args)

  def piBoardRev(self):
    return piBoardRev()
  def wpiPinToGpio(self,*args):
    return wpiPinToGpio(*args)
  def setPadDrive(self,*args):
    return setPadDrive(*args)
  def getAlt(self,*args):
    return getAlt(*args)
  def digitalWriteByte(self,*args):
    return digitalWriteByte(*args)

  def pwmSetMode(self,*args):
    pwmSetMode(*args)
  def pwmSetRange(self,*args):
    pwmSetRange(*args)
  def pwmSetClock(self,*args):
    pwmSetClock(*args)
  def gpioClockSet(self,*args):
    gpioClockSet(*args)
  def pwmWrite(self,*args):
    pwmWrite(*args)

  def pinMode(self,*args):
    pinMode(*args)

  def digitalWrite(self,*args):
    digitalWrite(*args)
  def digitalRead(self,*args):
    return digitalRead(*args)
  def digitalWriteByte(self,*args):
    digitalWriteByte(*args)

  def analogWrite(self,*args):
    analogWrite(*args)
  def analogRead(self,*args):
    return analogRead(*args)

  def shiftOut(self,*args):
    shiftOut(*args)
  def shiftIn(self,*args):
    return shiftIn(*args)

  def pullUpDnControl(self,*args):
    return pullUpDnControl(*args)

  def waitForInterrupt(self,*args):
    return waitForInterrupt(*args)
  def wiringPiISR(self,*args):
    return wiringPiISR(*args)

  def softPwmCreate(self,*args):
    return softPwmCreate(*args)
  def softPwmWrite(self,*args):
    return softPwmWrite(*args)

  def softToneCreate(self,*args):
    return softToneCreate(*args)
  def softToneWrite(self,*args):
    return softToneWrite(*args)

  def lcdHome(self,*args):
    return lcdHome(self,*args)
  def lcdCLear(self,*args):
    return lcdClear(self,*args)
  def lcdSendCommand(self,*args):
    return lcdSendCommand(self,*args)
  def lcdPosition(self,*args):
    return lcdPosition(self,*args)
  def lcdPutchar(self,*args):
    return lcdPutchar(self,*args)
  def lcdPuts(self,*args):
    return lcdPuts(self,*args)
  def lcdPrintf(self,*args):
    return lcdPrintf(self,*args)
  def lcdInit(self,*args):
    return lcdInit(self,*args)
  def piGlowSetup(self,*args):
    return piGlowSetup(self,*args)
  def piGlow1(self,*args):
    return piGlow1(self,*args)
  def piGlowLeg(self,*args):
    return piGlowLeg(self,*args)
  def piGlowRing(self,*args):
    return piGlowRing(self,*args)

# This file is compatible with both classic and new-style classes.


