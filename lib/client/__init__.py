from os import environ

if 'DEBUG' in environ:
  import logging
  logger = logging.getLogger('Client')

from Client import Client

__all__ = [
  'Client'
]