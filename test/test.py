from sys import path as python_path
from os import path, fork
from socket import AF_UNIX, SOCK_STREAM, socket
from time import sleep

lib_path = path.realpath(path.join(__file__, '..', '..'))
python_path.insert(0, lib_path)

import lib as uds

uri = 'test.sock'
server = uds.Server(uri, timeout=5)

if fork() == 0:

  sleep(1)
  for i in range(3):
    if fork() == 0:
      client = uds.Client(uri)
      request, response = client.send({'force':'powers', 'index': i+1})
      print 'I GOT:', response, type(response)
      break

  pass
else:
  server.listen()
  pass