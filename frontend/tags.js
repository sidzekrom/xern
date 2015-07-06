var MongoClient = require('mongodb').MongoClient,
   assert = require('assert');

//connection URL
xern = 'mongodb://localhost:27017/xernbase'


/* toFind is a dictionary, toSearch is a collection
    (referred to by its name in a string) */

function findElem(toSearch, toFind) {
    var placeholder = 12;
    MongoClient.connect(xern, function(err, db) {
        coll = db.collection(toSearch);
        tempCurs = coll.find(toFind)
        tempCurs.toArray(function(err, docs) {
            placeholder = docs;
        });   
    });
    setTimeout(function() {
        return placeholder;
    }, 1000);
}

var latios = findElem("userCollection", {});
console.log(latios);
