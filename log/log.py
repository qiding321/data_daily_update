# -*- coding: utf-8 -*-
"""
Created on 2016/12/5 9:25

@version: python3.5
@author: qiding
"""

import util.util
import my_path.my_path
import logging


class Logger(logging.Logger):
    def __init__(self):
        logger_name = 'log' + util.util.today_date_ymd_str
        logging.Logger.__init__(self, name=logger_name, level=logging.INFO)
        self.log_path = my_path.my_path.log_path_root + logger_name
        self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        file_log = logging.FileHandler(self.log_path)
        file_log.setFormatter(self.formatter)
        self.addHandler(file_log)

        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        console.setFormatter(self.formatter)
        self.addHandler(console)

        self.info('logger begin @ '.format(self.log_path))

    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR


log_today = Logger()
