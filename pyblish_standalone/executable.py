import sys
import time
import socket

import pyblish.api
import pyblish_integration


def main():
    # launching pyblish ui
    pyblish_integration.setup()

    max_tries = 5
    while True:
      try:
        time.sleep(0.5)
        pyblish_integration.show()
      except socket.error as e:
        if not max_tries:
          raise Exception("Couldn't run Pyblish QML: %s" % e)
        else:
          max_tries -= 1
      else:
          break
