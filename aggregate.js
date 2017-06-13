var MongoClient = require('mongodb').MongoClient;
var assert = require('assert');
var ObjectId = require('mongodb').ObjectID;
var url = 'mongodb://localhost:27017/test';
var aggregateRestaurants = function(db, callback) {
     db.collection('restaurants1').aggregate([
       			{$match : {gaID:{$ne:""}}},
       			{ $group: { "_id": {gaID:"$gaID", productid:"$productid" , campaignid:"$campaignid"} , "count": { $sum: 1 } } } 
     ]).toArray(function(err, result) {
     assert.equal(err, null);
     console.log(result);
     console.log("#####################");
     callback(result);
   });
   db.collection('restaurants1').aggregate([
       			{$match : {gaID:"",androidid:{$ne:""}}},
       			{ $group: { "_id": {androidid:"$androidid", productid:"$productid" , campaignid:"$campaignid"} , "count": { $sum: 1 } } } 
     ]).toArray(function(err, result) {
     assert.equal(err, null);
     console.log(result);
     console.log("#####################");
     callback(result);
   });
     db.collection('restaurants1').aggregate([
     			{$match : {gaID:"",androidid:""}},
       			{ $group: { "_id": {usertrackingcookies:"$usertrackingcookies", productid:"$productid" , campaignid:"$campaignid"} , "count": { $sum: 1 } } } 
     ]).toArray(function(err, result) {
     assert.equal(err, null);
     console.log(result);
     callback(result);
   });
};
MongoClient.connect(url, function(err, db) {
  assert.equal(null, err);
  aggregateRestaurants(db, function() {
      db.close();
  });
});