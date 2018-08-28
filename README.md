# python-binance-data-exporter

That's a Crypto Trader Program that allows users to export all coins data to a MySQL database

Just download binance.py to your python project directory

(Thank you to JesseCorrington for binance.py // https://github.com/JesseCorrington/binance-api-python)

Open trades.py and replace database connection string with your database information. (dbhost, dbusername, dbpassword, dbname)

Then trades.py will read the file coins.txt and connect to Binance.

It gets the coins data and insert them to Mysql database (in 5 minutes period)
