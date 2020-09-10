import requests

def getData():
   res = requests.get('https://tokenrating.wavesexplorer.com/api/v1/token?assetId=EjcnbEJppadGgUx9NuqNbB5MPPKxMqNCebxb1ejaWBut')
   data = res.json()
   token = data.get(u'tokens')
   val = token[0]
   
   details = val.get(u'details')
   quote = details.get(u'quote')
   usdValue = quote.get(u'usd')
   print(usdValue)
   
   

getData()