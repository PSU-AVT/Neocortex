import serial

import controlgw

if __name__=='__main__':
	controller = serial.Serial('/dev/ttyACM0', 38400)
	server = controlgw.ControlGw('', 8080, controller)
	asyncore.loop()

