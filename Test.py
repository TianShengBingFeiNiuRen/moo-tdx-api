# -*- coding: utf-8 -*-
"""
@Author Andon
@Time 2021/3/11

"""
from mootdx import consts
from mootdx.consts import MARKET_SH
from mootdx.quotes import Quotes


# 指数K线行情
def getPriceTdx():
    client = Quotes.factory(market='std')
    price = client.index(frequency=9, market=MARKET_SH, symbol='000001', start=1, offset=2)
    to_json = price.to_json(orient="records", force_ascii=False)
    print(type(to_json))
    print(to_json)


# 查询股票列表
def getCodeTdx():
    client = Quotes.factory(market='std')
    symbol = client.stocks(market=consts.MARKET_SH)

    print(type(symbol))
    print(symbol)
    print("================")
    columns = symbol.columns
    print(type(columns))
    print(columns)
    print("================")
    code = symbol["code"]
    print(type(code))
    print(code)
    print("================")
    to_json = symbol.to_json(orient="records", force_ascii=False)
    print(type(to_json))
    print(to_json)


if __name__ == '__main__':
    getPriceTdx()
