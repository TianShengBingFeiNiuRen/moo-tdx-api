# -*- coding: utf-8 -*-
"""
@Author Andon
@Time 2021/3/11

"""
from mootdx import consts
from mootdx.quotes import Quotes


# getCodeTdx
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
    getCodeTdx()
