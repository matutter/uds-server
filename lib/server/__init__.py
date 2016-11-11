from os import path, environ
from sys import path as python_path, stdout

lib_path = path.realpath(path.join(__file__, '..', '..'))
python_path.insert(0, lib_path)

if 'DEBUG' in environ:
  import logging
  logger = logging.getLogger('Server')
  
import Server