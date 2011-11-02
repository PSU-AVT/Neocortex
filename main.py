import evloop

import controlgw
import carcontrol

if __name__=='__main__':
	controller = carcontrol.CarControl('/dev/ttyACM0')
	server = controlgw.ControlGw('', 8080, controller)
	evloop.EventDispatcher().loop_forever()

