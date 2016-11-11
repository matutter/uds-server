from socket import AF_UNIX, SOCK_STREAM, socket as unix_socket
from json import dumps, loads
import logging 

logger = logging.getLogger('Client')
debug = logger.debug

class Client():

  def __init__(self, uri):
    self._uri = uri
    self.socket = unix_socket(AF_UNIX, SOCK_STREAM)

  def send(self, data):
    socket = self.socket

    debug('data=%s', data)

    self.open()
    socket.sendall(dumps(data))
    res = socket.recv(1024)
    socket.close()

    return socket, loads(res)

  def open(self):
    self.socket.connect(self._uri)
