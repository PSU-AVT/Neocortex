import serial

import controlgw
import evloop

if __name__=='__main__':
	#controller = serial.Serial('/dev/ttyACM0', 38400)
	controller = None
	server = controlgw.ControlGw('', 8080, controller)
	evloop.EventDispatcher().loop_forever()

