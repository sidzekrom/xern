var MongoClient = require('mongodb').MongoClient,
    assert = require('assert');

//connection URL
xern = 'mongodb://localhost:27017/xernbase'

var arrayToReturn = 2;
/* toFind is a dictionary, toSearch is a collection
    (referred to by its name in a string) */

function setOutput(err, docs) {
    arrayToReturn = docs;
}

var findElem = function(toSearch, toFind) {
                    MongoClient.connect(xern, function (err, db) {
                        coll = db.collection(toSearch);
                        tempCurs = coll.find(toFind);
                        tempCurs.toArray(setOutput);
                    });
                    return arrayToReturn;
               };

console.log(findElem('userCollection', {}));
