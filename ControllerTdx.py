# -*- coding: utf-8 -*-
"""
@Author Andon
@Time 2021/3/11

"""
import json

import flask
from mootdx import consts
from mootdx.consts import MARKET_SH
from mootdx.quotes import Quotes

server = flask.Flask(__name__)


# 获取指数K线行情
# frequency K线种类 0 5分钟K线 1 15分钟K线 2 30分钟K线 3 1小时K线 4 日K线 5 周K线 6 月K线 7 1分钟 8 1分钟K线 9 日K线 10 季K线 11 年K线
# symbol    标的代码
# start     开始位置
# offset    用户要请求的 K 线数目，最大值为 800
@server.route("/getPriceTdx", methods=["get"])
def getPriceTdx():
    frequency = flask.request.values.get("frequency")
    symbol = flask.request.values.get("symbol")
    start = flask.request.values.get("start")
    offset = flask.request.values.get("offset")
    client = Quotes.factory(market='std')
    price = client.index(frequency=frequency, market=MARKET_SH, symbol=symbol, start=start, offset=offset)
    columns = price.columns
    print(type(columns))
    print(columns)
    to_json = price.to_json(orient="records", force_ascii=False)
    return to_json


# 获取标的列表
@server.route("/getCodeTdx", methods=["get"])
def getCodeTdx():
    client = Quotes.factory(market='std')
    symbol = client.stocks(market=consts.MARKET_SH)
    columns = symbol.columns
    print(type(columns))
    print(columns)
    to_json = symbol.to_json(orient="records", force_ascii=False)
    return to_json


@server.route("/hello", methods=["get"])
def hello():
    res = {"msg": "这是一个接口", "msg_code": 0}
    print(type(res))
    json_str = json.dumps(res, ensure_ascii=False)
    print(type(json_str))
    print(json_str)
    return json_str


@server.route("/postTest", methods=["post"])
def postTest():
    key = flask.request.values.get("key")
    value = flask.request.values.get("value")
    print(type(key))
    print(key)
    print(value)
    return value


server.run(host="0.0.0.0", port=9999, debug=True)  # 改了代码之后,不用重启服务,会自动重启
