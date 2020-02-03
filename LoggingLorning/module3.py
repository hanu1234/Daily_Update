from LoggingLorning.Logging import Logging


class M3(object):
    def __init__(self):
        self.logger = Logging(__name__)
        #self.logger.log_cli("cli commands")