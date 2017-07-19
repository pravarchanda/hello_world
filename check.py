import smtplib
import requests
import sqlalchemy
from urllib import urlencode as encode
from json import dumps
engine = sqlalchemy.create_engine('mysql://root:123@localhost/mysql') # connect to server
engine.execute("use openx")
val_in_cache = engine.execute("select count(*) from ox_data_summary_ad_hourly_report")
for row in val_in_cache:
  val = row['count(*)']
if val>1000:
  print "hello"
  '''server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("pravar.c@tyroo.com", "helloworld")
  msg = "Reporting delay , please check ox_data_summary_ad_hourly_report"
  server.sendmail("pravar.c@tyroo.com","pravar.c@tyroo.com",msg)'''
  _requests = "syncRequest"
  _payload = {             
  "text": "Testing",             
  "channel": "#images",             
  "username": "damei.py",             
  "icon_emoji": ":damei:"         
  }
  payload = encode({'payload':dumps(_payload)})
  headers = { 'content-type': "application/x-www-form-urlencoded"}         
  response = requests.post(             
  "https://hooks.slack.com/services/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",
  data=payload,             
  headers=headers         
  )