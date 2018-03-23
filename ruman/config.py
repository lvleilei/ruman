#!/usr/bin/env python
# coding:utf-8
from db import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#table
TABLE_HOLDERS = 'holders'
TABLE_DAY = 'manipulate_day'
TABLE_WARNING = 'manipulate_warning'
TABLE_MARKET_DAILY = 'market_daily_new'
TABLE_HOLDERS_SHOW = 'holders_show'
TABLE_HOLDERS_PCT = 'holders_pct'

#es
ES_HOST = '219.224.134.214'
ES_PORT = 9202

#db
HOST = "219.224.134.214"
USER = "root"
PASSWORD = ""
DEFAULT_DB = "ruman"
CHARSET = "utf8"
TEST_DB = ""



#index_name
DAY_STOCK_ID = 'stock_id'
DAY_STOCK_NAME = 'stock_name'
DAY_START_DATE = 'start_date'
DAY_IFEND = 'ifend'
DAY_END_DATE = 'end_date'
DAY_MANIPULATE_TYPE = 'manipulate_type'
DAY_INDUSTRY_NAME = 'industry_name'
DAY_INDUSTRY_CODE = 'industry_code'
DAY_INCREASE_RATIO = 'increase_ratio'
DAY_ID = 'id'
WARNING_DATE = 'date'
WARNING_TIMES = 'times'
MARKET_PRICE = 'price'
MARKET_DATE = 'date'
MARKET_INDUSTRY_CODE = 'industry_code'
MARKET_STOCK_ID = 'stock_id'
HOLDERS_SHOW_STOCK_ID = 'stock_id'
HOLDERS_SHOW_DATE = 'date'
HOLDERS_SHOW_HOLDER_NAME = 'holder_name'
HOLDERS_SHOW_ID = 'id'
HOLDERS_SHOW_RANKING = 'ranking'
HOLDERS_PCT_STOCK_ID = 'stock_id'
HOLDERS_PCT_DATE = 'date'
HOLDERS_PCT_ID = 'id'
HOLDERS_PCT_HOLDER_TOP10PCT = 'holder_top10pct'
HOLDERS_PCT_HOLDER_PCTBYINST = 'holder_pctbyinst'