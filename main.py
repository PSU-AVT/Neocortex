import struct
import evloop

import controlgw
import carcontrol
import pubsub

class CarStatePublisher(object):
	def __init__(self, car, pubsub_server):
		self.car = car
		self.pubsub_server = pubsub_server

		self.car.add_response_handler(2, self.publish_state)

		self.request_state()

	def publish_state(self, msg):
		self.pubsub_server.publish('carState:'+msg)

	def request_state(self):
		self.car.send_msg(''+chr(3))
		evloop.EventDispatcher().add_timer(1, self.request_state)

if __name__=='__main__':
	controller = carcontrol.CarControl('/dev/ttyACM0')

	cg = controlgw.ControlGw('', 8080, controller)

	ps = pubsub.PubSubServer('', 8081)

	state_publisher = CarStatePublisher(controller, ps)

	evloop.EventDispatcher().loop_forever()

