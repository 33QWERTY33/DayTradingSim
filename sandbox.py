from yfinance.base import TickerBase

PEY = TickerBase("123")

from pprint import pprint

pprint(PEY.get_info(), indent=2)
