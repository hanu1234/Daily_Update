from LoggingLorning.Logging import Logging
from LoggingLorning.module2 import M2
from LoggingLorning.module3 import M3


class M1(object):
    def __init__(self):
        self.logger = Logging(__name__)   # create the logging object
        self.logger.log_info("Module1_say HI")
        self.m3 = M3()
        self.m2 = M2()


obj = M1()
