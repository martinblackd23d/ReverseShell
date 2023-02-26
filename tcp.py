import socket

class tcpserver():
	def __init__(self, port, mode, host = '', encoding = 'ascii', buffer = 65536):
		self.port = port
		self.host = host
		self.encoding = encoding
		self.buffer = buffer
		self.mode = mode
		return


	def estconn(self, host, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((host, port))
		s.listen()
		print('listening')
		conn, address = s.accept()
		print('accepted')
		return conn, address, s