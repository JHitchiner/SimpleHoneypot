#!/usr/bin/python

import time
import socket
import random

PORTMIN = 49152
PORTMAX = 65535

def logevent(address):
	with open("./honeypotlog.txt", "a") as f:
		f.write("%s - Connection from %s\n", time.ctime(), address[0])

def main(PORT):
	print("Established Honeyport on port", PORT)
	print("Listening for connections...")

	# Set up socket to listn on
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('localhost', PORT))
	s.listen(100)

	# Begin main listening loop
	while True:
		connect = None
		try:
			c, address = s.accept()
			print("Here")
			c.send(":O")
			c.close()
			logevent(address)
		except KeyboardInterrupt:
			if conection:
				connection.close()
			print("Shutting down...")
			exit(0)

if __name__ == "__main__":
	PORT = 0
	# Create random port, check if open, if not use for honey pot
	while True:
		PORT = random.randint(PORTMIN, PORTMAX)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		response = s.connect_ex(('localhost', PORT))
		s.close()
		if response == 10061: # Error number 10061, port is not open and can not be connected to
			# Port is closed and can be used
			break
	try:
		main(PORT)
	except KeyboardInterrupt:
		print("Shutting down...")
		exit(0)
	except BaseException as error:
		print("Error:", error)
		exit(0)