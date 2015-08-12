import sys

import pyblish.api

class CollectKwargs(pyblish.api.Collector):
    """ Collects all keyword arguments passed from the terminal """

    order = pyblish.api.Collector.order - 0.1

    def process(self, context):

        data = {}
        for count in range(0, len(sys.argv)):
            if sys.argv[count].startswith('--'):

                subcount = count + 1
                args_data = []
                while True:
                    if subcount >= len(sys.argv):
                        break

                    if sys.argv[subcount].startswith('--'):
                        break
                    args_data.append(sys.argv[subcount])
                    subcount += 1

                if len(args_data) == 1:
                    data[sys.argv[count][2:]] = args_data[0]

                if len(args_data) == 2:

                    if sys.argv[count][2:] in data:
                        data[sys.argv[count][2:]][args_data[0]] = args_data[1]
                    else:
                        data[sys.argv[count][2:]] = {args_data[0]: args_data[1]}

                if len(args_data) > 2:
                    data[sys.argv[count][2:]] = args_data

        context.set_data('kwargs', value=data)
