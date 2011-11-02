import evloop
import serial
import afproto

class SerialAfprotoWatcher(evloop.FdWatcher):
	def __init__(self, path):
		evloop.FdWatcher.__init__(self)
		self.open_path(path)
		self.in_buff = ''
		self.out_buff = ''

	def open_path(self, path):
		self.device = serial.Serial('/dev/ttyACM0', 38400, timeout=0)
		self.setup_fd(self.device.fd, 0)
		self.set_readable()

	def send_msg(self, msg):
		frame = afproto.serialize_payload(msg)
		if len(self.out_buff) == 0:
			self.set_writable()
		self.out_buff += frame

	def handle_write(self, fd):
		ch = self.out_buff[0]
		self.out_buff = self.out_buff[1:]
		if len(self.out_buff) == 0:
			self.set_writable(False)
		self.device.write(ch)

	def handle_read(self, fd):
		self.in_buff += self.device.read(10)
		msg, self.in_buff = afproto.extract_payload(self.in_buff)
		if msg != None:
			self.handle_msg(msg)


