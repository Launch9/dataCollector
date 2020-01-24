import requests
import time
import json
import os
def makeRequest(url, storeAt):
    curTime = time.time()
    try:
        result = requests.get(url = url)
    except:
        print("Lost connection!")
        return 0
    result = {"data":result.json(), "date":curTime}
    
    with open(storeAt + str(curTime) + '.json', 'w') as f:
        json.dump(result, f)
coins = []
products = requests.get(url = "https://api.pro.coinbase.com/products").json()
for i in products:
    if(not os.path.isdir("./coinbase/orderBook/" + i['id'])):
        os.mkdir("./coinbase/orderBook/" + i['id'])
    if(not os.path.isdir("./coinbase/tradeHist/" + i['id'])):
        os.mkdir("./coinbase/tradeHist/" + i['id'])
    coins.append(i['id'])
while(True):
    for i in coins:
        makeRequest("https://api.pro.coinbase.com/products/" + i + "/book?level=3", "coinbase/orderBook/" + i + "/coinbaseB:")
        #time.sleep(1.2)
        makeRequest("https://api.pro.coinbase.com/products/" + i + "/trades", "coinbase/tradeHist/" + i + "/coinbaseH:")
        #time.sleep(1.2)
        print("Requesting " + i)
    print("Sleeping for 60 secs")
    time.sleep(60)
    