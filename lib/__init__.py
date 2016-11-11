from os import path, environ

if 'DEBUG' in environ:
  import logging
  from sys import stdout
  logging.basicConfig(
    format='%(asctime)s | %(process)s | %(name)s.%(funcName)s %(message)s',
    datefmt="%H:%M:%S",
    stream=stdout)
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  logger.debug('DEBUG ENABLED')

from server.Server import Server
from request import Request
from client import Client

__all__ = [
  'Server', 'Request', 'Client'
]
