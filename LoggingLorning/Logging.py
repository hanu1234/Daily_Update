import logging
import sys
from logging.handlers import RotatingFileHandler


class Logging(object):

    # logger constants
    DEBUG = logging.DEBUG   # 10
    INFO = logging.INFO     # 20
    WARN = logging.WARN     # 30
    CRITICAL = logging.CRITICAL  # 40
    ERROR = logging.ERROR  # 50
    CLI = 22
    logging.addLevelName(CLI, "CLI")

    def __init__(self, logger_name):
        self.primary_log_file = "robot_log.log"
        self.cli_file = "cli_commands.log"
        self.max_log_size = 40000
        self.backup_count = 10
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(self.DEBUG)
        self.formatter = logging.Formatter("%(asctime)s -  %(levelname)s - %(message)s")
        self.__init_logger(logger_name)

    def __init_logger(self, logger_name):
        # adding the stream handler
        ch = logging.StreamHandler(sys.__stdout__)
        ch.setLevel(level=logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def __update_handlers(self, level):
        if "cli" not in [i.name for i in self.logger.handlers] and level == self.CLI:
            handler = RotatingFileHandler(self.cli_file, maxBytes=self.max_log_size,
                                          backupCount=self.backup_count)
            handler.name = "cli"
            handler.setLevel(self.CLI)
            handler.setFormatter(self.formatter)
            self.logger.addHandler(handler)

        elif "primary" not in [i.name for i in self.logger.handlers]:
            handler = RotatingFileHandler(self.primary_log_file, maxBytes=self.max_log_size,
                                          backupCount=self.backup_count)
            handler.name = "primary"
            handler.setFormatter(self.formatter)
            handler.setLevel(logging.INFO)
            self.logger.addHandler(handler)

    def log_messages(self, level, msg):
        if not isinstance(msg, str):
            msg = str(msg)
        self.__update_handlers(level)
        self.logger.log(level, msg)

    def log_cli(self, msg):
        self.log_messages(self.CLI, msg)

    def log_info(self, msg):
        self.log_messages(self.INFO, msg)