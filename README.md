# python-binance-data-exporter

That's a Crypto Trader Program that allows users to export all coins data to a MySQL database. 

You can easily export the data from MySQL to excel so, you can easily analyse the data to guess which coin will go UP or DOWN. 

Here is a screenshot below.

![alt text](https://github.com/goksinenki/python-binance-data-exporter/blob/master/binance_data_sample.PNG)

INSTALLATION (Windows/Linux)

Installation

Just download binance.py to your python project directory

(Thanks to JesseCorrington for binance.py // https://github.com/JesseCorrington/binance-api-python)

You will also need to install the websockets library. Python 3.6 or newer is required.

pip install websockets

Open trades.py and replace database connection string with your database information. (dbhost, dbusername, dbpassword, dbname)

Then trades.py will read the file coins.txt and connect to Binance.

It gets the coins data and insert them to Mysql database (in 5 minutes period)

Do not forget schedule to execute that script every 5 minutes...
