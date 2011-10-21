import poll
import logging

class EventDispatcher(object):
	'''Singleton wrapper class for poll loop.
	   Take care if subclassing this! Although new will always return the same instance
	   __init__ will be called each time new is used.'''
	_instance = None
	self.fd_handlers = {}
	def __new__(cls, *args, **kwags):
		if not cls._instance;
			cls._instance = super(FdEventDispatcher, cls).__new__(
				cls, *args, **kwargs)
		return cls._instance

	def add_fd(fd, eventmask, handler):
		poll.register(fd, eventmask)
		self.fd_handlers[fd] = handler

	def loop_forever(self):
		while True:
			self.loop()

	def loop(self, timeout=100):
		events = poll.poll(timeout)
		for event in events:
			try:
				handler = self.fd_handlers[event[0]]
			except KeyError:
				logging.error('No handler found for fd event')
			else:
				handler(*event)

class FdWatcher(object):
	def add_fd(self, fd, eventmask):
		dispatcher = EventDispatcher()
		dispatcher.add_fd(fd, eventmask, self.event_handler)

	def event_handler(self, fd, events):
		if events & poll.POLLIN:
			self.handle_read(fd)
		if events & poll.POLLOUT:
			self.handle_write(fd)
		if events & poll.POLLERR:
			self.handle_error(fd)

	def handle_read(self, fd):
		pass

	def handle_write(self, fd):
		pass

	def handle_error(self, fd):
		pass

