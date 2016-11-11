from os import environ

if 'DEBUG' in environ:
  import logging
  logger = logging.getLogger('util.io')
  logger = logging.getLogger('timer.ActivityTimer')

from io import touchp, \
  touch, \
  mkdirp

from timers import ActivityTimer