import logging


class Logger:
    """Logger class for setting up a logger with a specific name and level"""
    def __init__(self, logger_name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name=logger_name)
        self.logger.setLevel(level)
        if not self.logger.hasHandlers():
            self._logger_setup()

    def _logger_setup(self):
        """
        Sets up the logging handler and formatter.
        """
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(name)s] | %(levelname)s -> %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
