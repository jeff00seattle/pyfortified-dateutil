#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import pyfortified_dateutil
from pprintpp import pprint

pprint(pyfortified_dateutil.current_date())

pprint(pyfortified_dateutil.unixtime_to_datetime())
pprint(pyfortified_dateutil.unixtime_to_datetime(tz_name='Australia/Sydney'))
pprint(pyfortified_dateutil.unixtime_to_datetime(tz_name='America/Los_Angeles'))
