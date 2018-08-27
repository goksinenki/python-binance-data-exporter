#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from time import time, sleep
import threading
from decimal import *
import binance
import datetime
import time
from datetime import datetime
from queue import Queue
from threading import Thread
import telebot
import pymysql

#start = time()
my_file = open("coins.txt", "rb")
ilk_sira = Queue()



def coinokuyan():
    while True:
        coin = ilk_sira.get()
        last_24hr = binance.ticker_24hr("%s" % (coin))
        i = datetime.now()
        tson = int(time.time())*1000
        tilk = (tson-300000)
        srtime = i.strftime('%Y/%m/%d %H:%M:%S')
        change_24hr = last_24hr["priceChangePercent"]
        dipfiyat = round (Decimal (last_24hr["lowPrice"]), 8)
        tavanfiyat = round (Decimal (last_24hr["highPrice"]), 8)
        islemhacmi = round(Decimal(last_24hr["quoteVolume"]), 2)
        priceanlik = last_24hr["lastPrice"]
        candles = binance.candlesticks('%s' % (coin), "5m" , "2")
        candlevolume = round(Decimal(candles[0][5]), 2)
        candleopen = Decimal(candles[0][1])
        candleclose = Decimal(candles[0][4])
        order_book = binance.order_book ('%s' % (coin), 5)
        # buradan asagi bids ve asks kuyrukta bekleyen teklifler
        bids = order_book[0]
        asks = order_book[1]
        buyvolume0 = bids[0][1]
        buyvolume1 = bids[1][1]
        buyvolume2 = bids[2][1]
        buyvolume3 = bids[3][1]
        buyvolume4 = bids[4][1]
        sellvolume0 = asks[0][1]
        sellvolume1 = asks[1][1]
        sellvolume2 = asks[2][1]
        sellvolume3 = asks[3][1]
        sellvolume4 = asks[4][1]
        buyprice0 = bids[0][0]
        buyprice1 = bids[1][0]
        buyprice2 = bids[2][0]
        buyprice3 = bids[3][0]
        buyprice4 = bids[4][0]
        sellprice0 = asks[0][0]
        sellprice1 = asks[1][0]
        sellprice2 = asks[2][0]
        sellprice3 = asks[3][0]
        sellprice4 = asks[4][0]
        buypricetoplam = (buyvolume0 * buyprice0) + (buyvolume1 * buyprice1) + (buyvolume2 * buyprice2) + (buyvolume3 * buyprice3) + (buyvolume4 * buyprice4)
        buybtctoplam = round (buypricetoplam, 2)
        sellpricetoplam = (sellvolume0 * sellprice0) + (sellvolume1 * sellprice1) + (sellvolume2 * sellprice2) + (sellvolume3 * sellprice3) + (sellvolume4 * sellprice4)
        sellbtctoplam = round (sellpricetoplam, 2)
        if sellbtctoplam == 0:
            yuzdefark = 10000
        else:
            yuzdefark = round (((buybtctoplam * 100 / sellbtctoplam) - 100), 2)
        # buradan asagi yapılan tradeler
        trades = binance.aggregate_trades ('%s' % (coin), start_time='%s' % (tilk), end_time='%s' % (tson))
        tbtcbuytoplamlist = []
        tbtcselltoplamlist = []
        for i in range(len(trades)):
                tradei = trades[i]
                tpricei = (tradei["p"])
                tquantityi = (tradei["q"])
                tbuyorselli = (tradei["m"])
                if tbuyorselli == True:
                    tsellpricei = tpricei
                    tsellquantityi = tquantityi
                    tbuypricei = int ('0')
                    tbuyquantityi = int ('0')
                elif tbuyorselli == False:
                    tbuypricei = tpricei
                    tbuyquantityi = tquantityi
                    tsellpricei = int ('0')
                    tsellquantityi = int ('0')
                tbtcbuytoplami = (tbuypricei * tbuyquantityi)
                tbtcselltoplami = (tsellpricei * tsellquantityi)
                tbtcbuytoplamlist.append(tbtcbuytoplami)
                tbtcselltoplamlist.append(tbtcselltoplami)
        tbtcbuytoplamlist = round (sum(tbtcbuytoplamlist), 2)
        tbtcselltoplamlist = round (sum(tbtcselltoplamlist), 2)
        if tbtcselltoplamlist == 0:
            tradebtcyuzdefark = 0
        else:
            tradebtcyuzdefark = round (((tbtcbuytoplamlist * 100 / tbtcselltoplamlist) - 100), 2)
        # buradan asagisi artik kosullar
        #        thstrades.write('ALARM, %s, #%s, 24hr %%%s, volume %s, price %s BTC, Lprice %s BTC, Hprice %s BTC, vol %%%s, b%s BTC, s%s BTC;\n'%(srtime,coin,change_24hr,islemhacmi,priceanlik,dipfiyat,tavanfiyat,yuzdefark,buybtctoplam,sellbtctoplam))
        sql = """INSERT INTO trades (date,coinname,24hr,price,volume,dipfiyat,tavanfiyat,yuzdefark,buybtctoplam,sellbtctoplam,tbtcbuytoplam,tbtcselltoplam,tradebtcyuzdefark,candlevolume,candleopen,candleclose,buyprice0,buyvolume0,sellprice0,sellvolume0)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
        srtime, coin, change_24hr, priceanlik, islemhacmi, dipfiyat, tavanfiyat, yuzdefark, buybtctoplam, sellbtctoplam,
        tbtcbuytoplamlist, tbtcselltoplamlist, tradebtcyuzdefark,candlevolume,candleopen,candleclose,buyprice0,buyvolume0,sellprice0,sellvolume0)
        db = pymysql.connect ("Host/IPAddress", "databaseuser", "databasepassword", "databasename")
        cursor = db.cursor ()
        try:
            # Execute the SQL command
            cursor.execute (sql)
            # Commit your changes in the database
            db.commit ()
        except:
            # Rollback in case there is any error
            db.rollback ()
        db.close ()
        #liste = [srtime, change_24hr, islemhacmi, priceanlik]
        ilk_sira.task_done()
        #print(coin, liste)


if __name__ == "__main__":
    #basla = time()
    for i in range(15):
        t = Thread(target = coinokuyan)
        t.daemon = True
        t.start()

    for line in my_file:
       l = [i.strip() for i in line.decode().split(' ')]
       coin = l[0]
       ilk_sira.put(coin)



    ilk_sira.join()
sleep(1)
#gecenzaman = (time() - start)
#print(("%s" % gecenzaman), "saniye surdu")
