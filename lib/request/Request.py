import logging
from SocketServer import BaseRequestHandler
from json import loads, dumps
from time import sleep
from os import getpid

logger = logging.getLogger('Request')
debug = logger.debug

class Request(BaseRequestHandler, object):

  def handle(self):
    # self.request is the TCP socket connected to the client
    data = self.request.recv(1024).strip()
    debug('data=%s', data)
    try:
      data = loads(data)
      data['force'] = 'AWAKENS'
      data['pid'] = getpid()
    except Exception, e:
      debug('Error %s', e)
      data = e.message
    finally:
      sleep(data['index'])
      self.request.sendall(dumps(data))
      self.request.close()
