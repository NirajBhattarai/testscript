from datetime import datetime
import pywaves as pw
import requests
import time
import json
import datetime


def getData():
   res = requests.get('https://tokenrating.wavesexplorer.com/api/v1/token?assetId=DHgwrRvVyqJsepd32YbBqUeDH4GJ1N984X8QoekjgH8J')
   data = res.json()
   token = data.get(u'tokens')
   val = token[0]
   
   details = val.get(u'details')
   quote = details.get(u'quote')
   usdValue = quote.get(u'usd')
   return usdValue
   
   


def cronjob(x):
    pw.setNode('https://testnode1.wavesnodes.com', 'testnet')
    address =  pw.Address(seed = 'staff asset buzz august fog easy cube ginger tray album cheese used adult power budget')
    print(x)
    now = round(time.time() * 1000)
    value =x*1000000
    print(value)
    date = datetime.datetime.now()
  
    data =[
        
        { "key": "lastPrice", "value": value, "type": "integer" },
        { "key": "date", "value": str(date), "type": "string" }
        
    ]
    
    tx =  address.dataTransaction(data,0)
    print(tx)
    
        
    
    
x = getData()
cronjob(x)

