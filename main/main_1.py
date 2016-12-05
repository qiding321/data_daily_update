# -*- coding: utf-8 -*-
"""
Created on 2016/12/5 9:18

@author: qiding
"""

import my_path.my_path
import log.log as log
import util.util

import data.data_dvd
import data.data_index_and_future
import data.data_px
import data.data_weight


log_today = log.log_today


def main():
    date_today_str = util.util.today_date_ymd_str
    data_dvd_today = data.data_dvd.DataDvd(date_today_str)
    data_index_and_future_today = data.data_index_and_future.DataIndexFuture(date_today_str)
    data_px_today = data.data_px.DataPx(date_today_str)
    data_weight_today = data.data_weight.DataWeight(date_today_str)

    for data_tmp in [data_dvd_today, data_index_and_future_today, data_px_today, data_weight_today]:
        data_tmp.download()
        data_tmp.check_valid()
        data_tmp.merge_pre_data()
        data_tmp.backup()


if __name__ == '__main__':
    main()
