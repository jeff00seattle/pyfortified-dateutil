#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

from pprintpp import pprint
import datetime as dt
import pyfortified_dateutil

start_dt = dt.date(2016, 12, 20)
end_dt = dt.date(2018, 1, 11)

print(type(pyfortified_dateutil.dates_months_generator(start_dt, end_dt)))

for month in pyfortified_dateutil.dates_months_generator(start_dt, end_dt):
    pprint(month)