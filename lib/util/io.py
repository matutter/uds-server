from os import path, makedirs, access, utime, unlink, R_OK, W_OK
from errno import EEXIST

def touchp(filepath):
  dirname = path.dirname(filepath)
  mkdirp(dirname)
  return touch(filepath)

def touch(filepath, times=None):
  if path.exists(filepath):
    utime(filepath, times)
  else:
    open(filepath, 'a').close()
  return filepath

def mkdirp(dirpath):
  if dirpath == '':
    return dirpath

  if not path.exists(dirpath):
    try:
      makedirs(dirpath)
    except OSError as exc:
      if exc.errno != EEXIST:
          raise

  if not path.isdir(dirpath):
    raise NotADirectoryError(dirpath)

  return dirpath
