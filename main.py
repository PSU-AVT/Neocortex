import asyncore, socket
import afproto

class Neocortex(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.set_reuse_addr()
		self.bind((host, port)) 

	def handle_read(self):
		data, addr = self.recvfrom(2048)
		print str(addr)+" >> "+data 

	def writable(self):
		return False

	def handle_write(self):
		pass

if __name__=='__main__':
	server = Neocortex('', 8080)
	asyncore.loop()

