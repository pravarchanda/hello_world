var redis = require('redis');
var client = redis.createClient();
var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
var url = 'mongodb://172.31.32.99:27017/openx';


var aggregateRawClicksNew = function(db, callback) {
 var key_value = [];
 var final_value = [];
 var main_json = {};

 var today = new Date();
 var yesterday = new Date(today);
 yesterday.setDate(today.getDate()-1);
 var prevdate = String(yesterday.getFullYear()+"-"+("0"+(yesterday.getMonth()+1)).slice(-2)+"-"+("0"+yesterday.getDate()).slice(-2)+" "+("0"+today.getHours()).slice(-2)+":"+("0"+today.getMinutes()).slice(-2)+":"+("0"+today.getSeconds()).slice(-2));
 console.log(prevdate);
 db.collection('ox_raw_ckt_new').aggregate([
  { $match : { gaId : { $ne:"" } , date_time:{ $gte: prevdate }, click_source : {$ne:'random-ckt'}, product_id:{$ne:""}, affiliateid:{$ne:'1907'} } },
  { $group: { "_id": "$gaId",product_id:{$addToSet:{$concat:["$product_id","##camp##","$campaignid"]} } }}
  ]
  ,{allowDiskUse : true}
  ).toArray(function(err, result) {
   assert.equal(err, null);
   for (var i = 0; i < result.length; i++) {
    console.log("result------gaid-",result[i]);
    key_value.push(result[i]);
  };
  callback(result);
});


  db.collection('ox_raw_ckt_new').aggregate([
   {$match : {gaId:"",androidId:{$ne:""}, date_time:{ $gte: prevdate }, click_source : {$ne:'random-ckt'}, product_id:{$ne:""}, affiliateid:{$ne:'1907'}  } },
   { $group: { "_id": "$androidId",product_id:{$addToSet:{$concat:["$product_id","##camp##","$campaignid"]} } } },
   ],{allowDiskUse : true}
   ).toArray(function(err, result) {
     assert.equal(err, null);
     for (var i = 0; i < result.length; i++) {
      console.log("result-----andr-",result[i]);
      key_value.push(result[i]);
    };
    callback(result);
  });



   db.collection('ox_raw_ckt_new').aggregate([
    {$match : {gaId:"",androidId:"",IDFA:{$ne:""}, date_time:{ $gte: prevdate }, click_source : {$ne:'random-ckt'}, product_id:{$ne:""}, affiliateid:{$ne:'1907'} }},
    { $group: { "_id": "$IDFA",product_id:{$addToSet:{$concat:["$product_id","##camp##","$campaignid"] } } } },
    ],{allowDiskUse : true}
    ).toArray(function(err, result) {
     assert.equal(err, null);
     for (var i = 0; i < result.length; i++) {
      console.log("result-----idfa-",result[i]);
      key_value.push(result[i]);
    };
    callback(result);
  });


    db.collection('ox_raw_ckt_new').aggregate([
     {$match : {gaId:"",androidId:"",IDFA:"", date_time:{ $gte: prevdate }, click_source : {$ne:'random-ckt'}, product_id:{$ne:""}, affiliateid:{$ne:'1907'} }},
     { $group: { "_id": "$userTrackingCookie",product_id:{$addToSet:{$concat:["$product_id","##camp##","$campaignid" ] } } } }
     ],{allowDiskUse : true}
     ).toArray(function(err, result) {
       assert.equal(err, null);
       for (var i = 0; i < result.length; i++) {
        console.log("result-----utcookie-",result[i]);
        key_value.push(result[i]);
      };

      for (var i = 0; i <key_value.length; i++) {
        var jsondata = {};
        for (var j = 0; j < key_value[i].product_id.length; j++){
          var key = key_value[i].product_id[j];
          jsondata[key] = key_value[i].product_id[j].split("##camp##").pop();
        };
      //var myarr = [];
      //myarr.push(jsondata);
      var upload_json = JSON.stringify(jsondata);
      //upload_json = upload_json.replace(/[{}]/g, '');
      client.select(38, function(err, reply) {
      });
      console.log(upload_json);
      client.set(key_value[i]._id, upload_json, function(err, reply) {
      });
    };
    process.exit();
    callback(result);
  });
   };
   MongoClient.connect(url, function(err, db) {
    assert.equal(null, err);
    aggregateRawClicksNew(db, function() {
     // db.close();
   });
  });