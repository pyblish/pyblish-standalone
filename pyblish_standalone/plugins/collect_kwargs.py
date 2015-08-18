import pyblish.api
import pyblish_standalone


class CollectKwargs(pyblish.api.Collector):
    """ Collects all keyword arguments passed from the terminal """

    order = pyblish.api.Collector.order - 0.1

    def process(self, context):
        kwargs = pyblish_standalone.kwargs.__dict__.copy()

        self.log.info("Storing kwargs: %s" % kwargs)
        context.set_data("kwargs", kwargs)

        self.log.info("Adding data from command-line into Context..")
        data = dict(kwargs.pop("data", list()))
        for key, value in data.iteritems():
            self.log.info("%s = %s" % (key, value))
            context.set_data(key, value)
