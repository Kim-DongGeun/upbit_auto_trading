import pyupbit
import time
import datetime

K = 0.5
targetTicker = "KRW-BTC"

def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, 'day')
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterdayRange = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterdayRange * K
    print("시가 : ", today['open'])
    return target

f = open("upbit.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret) # 객체 생성

target = cal_target(targetTicker) # 목표가
op_mode = False # 목표가 갱신 여부
hold = False # 코인 보유 여부
buy_price = 0

print("목표가 : ", datetime.datetime.now(), target)

while True:
    now = datetime.datetime.now()

    # 목표가 갱신
    if now.hour == 9 and now.minute == 0 and 20 <= now.second <= 30:
        target = cal_target(targetTicker)
        op_mode = True
        print("목표가 : ", now, target)


    price = pyupbit.get_current_price(targetTicker)

    # 매수 시도
    if op_mode is True and hold is False and price is not None and price <= target:
        krw_blance = upbit.get_blance("KRW")
        upbit.buy_market_order(targetTicker, krw_blance * 0.95)
        hold = True
        print("매수 : ",now, price) 

    # 장마감시 매도
    if now.hour == 8 and now.minute == 59 and (50 <= now.second <= 59):
        if op_mode is True and hold is True:
            btc_balance = upbit.get_blance(targetTicker)
            res = upbit.sell_market_order(targetTicker, btc_balance)
            hold = False
            print("매도 : ", now, res['price'])

        op_mode = False
        time.sleep(10)


    time.sleep(1)