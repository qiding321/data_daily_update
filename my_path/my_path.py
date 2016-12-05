# -*- coding: utf-8 -*-
"""
Created on 2016/12/5 9:25

@version: python3.5
@author: qiding
"""


import socket

name = socket.gethostname()


if name == '2013-20151201LG':
    log_path_root = 'F:\DataDailyUpdate\log_files'+'\\'
else:
    print('error host')
    raise ValueError
