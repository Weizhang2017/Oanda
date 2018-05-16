import sys
import json

from oandapyV20.contrib.factories import InstrumentsCandlesFactory
from oandapyV20 import API
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

'''python oandaV20.py 2018-01-01T00:00:00Z 2018-05-30T00:00:00Z M5 EUR_USD'''
client = API(access_token=config['account']['token'])

_from = sys.argv[1]
_to = sys.argv[2]
gran = sys.argv[3]
instr = sys.argv[4]

params = {
    "granularity": gran,
    "from": _from,
    "to": _to
}

def cnv(r, h):
    for candle in r.get('candles'):
        ctime = candle.get('time')[0:19]
        try:
            rec = "{time},{complete},{o},{h},{l},{c},{v}".format(
                time=ctime,
                complete=candle['complete'],
                o=candle['mid']['o'],
                h=candle['mid']['h'],
                l=candle['mid']['l'],
                c=candle['mid']['c'],
                v=candle['volume'],
            )
        except Exception as e:
            print(e, r)
        else:
            h.write(rec+"\n")

with open("/Users/wzhang/Desktop/Oanda/{}.{}.out".format(instr, gran), "w") as O:
    for r in InstrumentsCandlesFactory(instrument=instr, params=params):
        print("REQUEST: {} {} {}".format(r, r.__class__.__name__, r.params))
        rv = client.request(r)
        cnv(r.response, O)
