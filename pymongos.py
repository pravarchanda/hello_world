from collections import Counter
import json
import datetime
from flask import Flask,request
from flask import jsonify
from json import loads, dumps
import pymongo
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/")
def my_responses():
	finalval = {}
	myarray = []
	eventid = request.args.get("stdEventId")
	campaign_id = request.args.get("campaignid")
	inputt = request.args.get("inputs")
	temp = json.loads(str(inputt))
	startdate = temp['startDate']
	enddate = temp['endDate']
	client = MongoClient('52.88.68.199',27017)
	db = client['openx']
	collection = db['ox_raw_conversions']
	count = 0
	result = collection.find({"campaignid":int(campaign_id),"date_time":{"$gte":str(startdate),"$lte":str(enddate)}})
	for doc in result:
		if (str(doc['stdEventId'])==eventid):
			myarray.append("affiliateid : " + str(doc['affiliateid']))
	c = Counter(myarray)
	finalval[str(campaign_id)] = c.items()
	return jsonify(finalval)

if (__name__ == "__main__"):
    app.run(host='0.0.0.0',port=5001)