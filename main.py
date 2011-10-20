import asyncore, socket
import afproto
import serial
import struct

class Neocortex(asyncore.dispatcher):
	def __init__(self, host, port, controller):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.set_reuse_addr()
		self.bind((host, port)) 
		self.controller = controller

	def handle_read(self):
		data, addr = self.recvfrom(2048)
		cmd_id, arg = struct.unpack('BB', data)
		print cmd_id, arg
		self.controller.write(afproto.serialize_payload(data))

	def writable(self):
		return False

	def handle_write(self):
		pass

if __name__=='__main__':
	controller = serial.Serial('/dev/ttyACM0', 38400)
	server = Neocortex('', 8080, controller)
	asyncore.loop()

