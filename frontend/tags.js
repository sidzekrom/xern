var MongoClient = require('mongodb').MongoClient,
    assert = require('assert');

//connection URL
xern = 'mongodb://localhost:27017/xernbase'

var arrayToReturn = 2;
/* toFind is a dictionary, toSearch is a collection
    (referred to by its name in a string) */
var findElem = function(toSearch, toFind, callback) {
                    var arrayToReturn = 6;
                    MongoClient.connect(xern, function (err, db) {
                        coll = db.collection(toSearch);
                        tempCurs = coll.find(toFind);
                        tempCurs.toArray(function(err, docs) {
                            arrayToReturns = docs;
                            callback(docs);
                        });
                        console.log(arrayToReturn);
                    });
                    return arrayToReturn;
               };
//findElem('userCollection', {});
console.log(findElem('userCollection', {}, function(docs) {
    return docs;}));
