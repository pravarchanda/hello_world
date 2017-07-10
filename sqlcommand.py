import json
import datetime
import sqlalchemy
from dogpile.cache import make_region
from dogpile.cache.api import NO_VALUE
from flask import Flask,request


app = Flask(__name__)
region = make_region().configure('dogpile.cache.memory')


def save(key, value):
  """
  general purpose method to save data (value) in the cache

  :param key (string) key of the value to be saved in cache
  :param value (any type) the value to be saved
  """
  region.set(key, value)


def get(key):
  """
  general purpose method to get data from the cache

  :param key (string) key of the data to be fetched
  :return value (any type) data to be returned from the cache
  """
  return region.get(key)


@app.route("/")
def hello():
    finaljson = {}
    myarray = []
    val = {}
    affiliate_id = request.args.get("affiliate_id")
    inputt = request.args.get("inputs")
    temp = json.loads(inputt)
    startdate = temp['startDate']
    enddate = temp['endDate']
    campaign_id = request.args.get("campaign_id")
    print startdate
    day = datetime.timedelta(days=1)
    d = datetime.datetime.strptime(startdate, '%Y-%m-%d')
    d1 = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    day_string = d.strftime('%Y-%m-%d')
    # val has values from get request parameter
    val_in_cache = get(affiliate_id)
    # val_in_cache checks if this value is present in cache or not
    if val_in_cache is NO_VALUE:
        # if value is not in cache take it out from mysql
        engine = sqlalchemy.create_engine('mysql://root:123@localhost/mysql') # connect to server
        engine.execute("use openx")
        if(campaign_id==None):
          val_in_cache = engine.execute("select affiliate_id,date_time,sum(clicks),sum(impressions),sum(total_conversions),sum(total_cost+total_conversions_commission) from ox_data_summary_ad_hourly_report group by affiliate_id,date_time having affiliate_id="+str(affiliate_id)+";")
          #for date in range(startdate,enddate):
        #append in array
        else:
          val_in_cache = engine.execute("select affiliate_id,date_time,sum(clicks),sum(impressions),sum(total_conversions),sum(total_cost+total_conversions_commission) from ox_data_summary_ad_hourly_report group by affiliate_id,date_time having affiliate_id="+str(affiliate_id)+";")
          #for date in range(startdate,enddate):
        #append in array
        for row in val_in_cache:
          check = datetime.datetime.strptime(str(row['date_time']), '%Y-%m-%d')
          if (check>=d) and (check<=d1):
            print check
            val['date']= check.strftime('%Y-%m-%d')
            val['clicks'] = str(row['sum(clicks)'])
            myarray.append(val)
        finaljson['stats'] = myarray
    else:
        finaljson = val_in_cache

    data = json.dumps(finaljson)
    return data

if (__name__ == "__main__"):
    app.run(port=5000)