from config import XCC_API
import http.client
import json
import time

ids = dict()
conn = http.client.HTTPSConnection("api.commerce.coinbase.com")

def e(m):
  if (m > 1):
    return "s"
  return ""

def paygen(m, uid, nick):
  if (m == 1):
    sum = 10
  elif (m == 3):
    sum = 25
  elif (m == 6):
    sum = 40
  elif (m == 12):
    sum = 70
  payload = json.dumps({
    "name": "Web Scanner payment",
    "description": f"{m} month{e(m)}",
    "local_price": {
      "amount": sum*3,
      "currency": "BYN"
    },
    "metadata": {
      "customer_id": str(uid),
      "customer_name": nick
    },
    "pricing_type": "fixed_price"
  })
  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-CC-Version': '2018-03-22',
    'X-CC-Api-Key': XCC_API
  }
  conn.request("POST", "/charges", payload, headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data.decode("utf-8"))
  print(data)
  url = data["data"]["hosted_url"]
  ids[uid] = data["data"]["id"]
  return url

def check(uid):
  payload = ''
  headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-CC-Version': '2018-03-22',
    'X-CC-Api-Key': XCC_API
  }
  conn.request("GET", f"/charges/{ids[uid]}", payload, headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data.decode("utf-8"))
  stat = data["data"]["timeline"][-1]["status"]
  return stat