import logging

class Logger():



    def __init__(self):
        self.logger = logging.getLogger()
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s",
                                      "%Y-%m-%d %H:%M:%S")
        # create console handler (ch) and set level to debug
        ch = logging.StreamHandler()
        # add formatter to console handler
        ch.setFormatter(formatter)
        # add console handler to logger
        self.logger.addHandler(ch)

    def Info(self,message: str):
        self.logger.setLevel(logging.INFO)
        self.logger.info(message)

    def Error(self, message: str):
        self.logger.setLevel(logging.ERROR)
        self.logger.error(message)
