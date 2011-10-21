import socket
import struct

import afproto
import evloop

class ControlGw(evloop.FdWatcher):
	def __init__(self, host, port, controller):
		evloop.FdWatcher.__init__(self)
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.socket.bind((host, port)) 
		self.controller = controller
		self.setup_fd(self.socket, 0)
		self.set_readable()

	def handle_read(self, fd):
		data, addr = self.recvfrom(2048)
		cmd_id, arg = struct.unpack('BB', data)
		self.controller.write(afproto.serialize_payload(data))

	def handle_write(self, fd):
		pass

