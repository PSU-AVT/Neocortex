import afprotowatcher
import logging

class CarControl(afprotowatcher.SerialAfprotoWatcher):
	def __init__(self, path):
		afprotowatcher.SerialAfprotoWatcher.__init__(self, path)
		self.response_handlers = {}
		self.global_response_handlers = []

	def handle_msg(self, msg):
		logging.debug('Got %d command from car' % ord(msg[0]))

		for handler in self.global_response_handlers:
			handler(msg)

		try:
			handlers = self.response_handlers[ord(msg[0])]
			for handler in handlers:
				handler(msg)
		except KeyError:
			pass

	def add_response_handler(self, response_id, handler):
		try:
			self.response_handlers[response_id].append(handler)
		except KeyError:
			self.response_handlers[response_id] = [handler]

	def add_global_response_handler(self, handler):
		self.global_response_handlers.append(handler)

