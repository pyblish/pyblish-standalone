import sys
import time
import socket

import pyblish.api
import pyblish_integration


class CollectArgs(pyblish.api.Collector):
    """"""

    order = pyblish.api.Collector.order - 0.1

    def process(self, context):

        data = {}
        for count in range(0, len(sys.argv)):
            if sys.argv[count] == '-data':
                if not sys.argv[count + 1].startswith('-'):
                    key = sys.argv[count + 1]
                    value = sys.argv[count + 2]

                    context.set_data(key, value=value)
                    data[key] = value

        context.set_data('args', value=data)


def main():
    # launching pyblish ui
    pyblish_integration.setup()

    pyblish.api.register_plugin(CollectArgs)

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
