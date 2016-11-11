from os import path, unlink, access, R_OK, W_OK
from socket import AF_UNIX, SOCK_STREAM, socket as unix_socket
from SocketServer import BaseServer, ForkingMixIn
import logging


# lib
from util import mkdirp, touchp, ActivityTimer
from request import Request

logger = logging.getLogger('Server')
debug = logger.debug

class Server(ForkingMixIn, BaseServer, object):

  def __init__(self, uri, **kwargs):
    Server.testSocketAccess(uri)
    
    self.timeout = kwargs.get('timeout', 5)

    self._uri = uri
    self.socket = None
    self.allow_reuse_address = True
    self.activityTimer = ActivityTimer(self)
    BaseServer.__init__(self, uri, Request)

  def listen(self):
    socket = unix_socket(AF_UNIX, SOCK_STREAM)
    socket.bind(self._uri)
    socket.listen(5)
    self.socket = socket
    self.activityTimer.start()
    debug('entering blocking mode timeout=%ss', self.timeout)
    self.serve_forever(3)

  def get_request(self):
    debug('')
    connection = self.socket.accept()
    if connection:
      self.activityTimer.notify()
      return connection

  def handle_timeout(self):
    debug('Timeout exceeded (%ss). The server is shutting down.', self.timeout)
    self.shutdown()
    self.cleanup()

  def cleanup(self):
    try:
      unlink(self._uri)
    except Exception, e:
      debug('%s', e)

  def handle_error(self, connection, null_addre):
    debug('')

  def fileno(self):
    return self.socket.fileno()

  """
  Checks the access to the UDS by creating the file path, the file, checking access(W_OK|R_OK)
  and unlinking the file, in that order.
  """
  @staticmethod
  def testSocketAccess(uri):
    try:
      touchp(uri)
      access(uri, R_OK | W_OK)
      unlink(uri)
      debug('%s', uri)
    except Exception as e:
      debug('(%s) failed %s', uri, e)
      raise e