from os import environ

if 'DEBUG' in environ:
  import logging
  logger = logging.getLogger('Request')

from Request import Request

__all__ = [
  'Request'
]