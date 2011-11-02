import afprotowatcher

class CarControl(afprotowatcher.SerialAfprotoWatcher):
	def __init__(self, path):
		afprotowatcher.SerialAfprotoWatcher.__init__(self, path)

	def handle_msg(self, msg):
		print 'Got %s' % msg

