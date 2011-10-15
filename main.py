import asyncore, socket
import afproto

class NeocortexHandler(asyncore.dispatcher_with_send):
	pass

class Neocortex(asyncore.dispatcher):
	def __init__(self, host, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(5)
	def handle_accept(self):
		pair = self.accept()
		if pair is None:
			pass
		else:
			sock, addr = pair
			print 'Incoming connection from %s' % repr(addr)
			handler = NeocortexHandler(sock)

if __name__=='__main__':
	server = Neocortex('', 8080)
	asyncore.loop()

