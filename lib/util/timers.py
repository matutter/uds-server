from time import time as now
from threading import Timer
from SocketServer import BaseServer
import logging

logger = logging.getLogger('timer.ActivityTimer')
debug = logger.debug

"""
A timer that calls BaseServer.handle_timeout when there is no
activity recorded within the servers 'timeout' variable.

Invoke ActivityTimer.notify to extend server's TTL.
"""
class ActivityTimer():

  def __init__(self, server):
    if not isinstance(server, BaseServer):
      raise TypeError('Object does not extend SocketServer.BaseServer')

    self.server = server
    self._activity = 0
    self._timer = None

  """
  Gets the duration of the server's timeout variable.
  """
  def getTimeout(self):
    return self.server.timeout

  """
  Notifies the timer that there was activity, extending the TTL of the server.
  """
  def notify(self):
    self._activity = now()

  """
  Calls the BaseServer's handle_timeout method if it didn't notify any
  activity within it's timeout duration.
  """
  def checkForTimeout(self):
    debug('')
    if (now() - self._activity) > self.getTimeout():
      self.server.handle_timeout()
    else:
      self.restart()

  """
  Cancels the internal Timer and restarts the timer thread.
  """
  def restart(self):
    try:
      self._timer.cancel()
    except Exception, e:
      debug('%s', e)
    finally:
      self._timer = None
    self.start()

  """
  Starts the timer that will call the BaseServer.handle_timeout method if there is no
  activity recorded by ActivityTimer.notify within the duration of BaseServer.timeout.
  """
  def start(self):
    debug('timeout=%d', self.getTimeout())

    if self._timer:
      raise Exception('Timer already set.')

    self._timer = Timer(self.getTimeout(), self.checkForTimeout)
    self._timer.start()

