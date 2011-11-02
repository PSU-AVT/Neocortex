import evloop

import controlgw
import carcontrol

def print_msg(msg):
	print msg

if __name__=='__main__':
	controller = carcontrol.CarControl('/dev/ttyACM0')
	controller.add_global_response_handler(print_msg)

	server = controlgw.ControlGw('', 8080, controller)
	evloop.EventDispatcher().loop_forever()

