import pyblish.api
import pyblish_standalone


class CollectKwargs(pyblish.api.Collector):
    """ Collects all keyword arguments passed from the terminal """

    order = pyblish.api.Collector.order - 0.1

    def process(self, context):
        kwargs = pyblish_standalone.kwargs.__dict__.copy()

        self.log.info("Converting kwargs from tuple to dict")
        kwargs["data"] = dict(kwargs.pop("data"))

        self.log.info("Storing kwargs: %s" % kwargs)
        context.set_data("kwargs", kwargs)
