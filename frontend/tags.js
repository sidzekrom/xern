var MongoClient = require('mongodb').MongoClient,
    assert = require('assert');
    async = require('async');

//connection URL
xern = 'mongodb://localhost:27017/xernbase'

var answer;
/* toFind is a dictionary, toSearch is a collection
    (referred to by its name in a string) */

function findElem(toSearch, toFind, continuation){
/* findElem declared in global env. for use throughout script*/
    async.waterfall([
    /* waterfall used to process findElem sequentially and then push to
        desired function using "continuation" */
        function (callback){
        /*first function -- returns a temporary cursor into db */
            MongoClient.connect(xern, function(err, db) {
                callback(null, db.collection(toSearch).find(toFind));
            })
        },
        function (tempCurs, callback){
        /* second function -- returns the required docs as array upon querying */
            tempCurs.toArray(function(err, docs) {
                callback(null, docs);
                });
            }
        ],
        function (err, docs) {
        /* the waterfall is pushed onto this functions and it sets the value
            for the continuation. Can't return continuation directly because
            continuation is declared as function and a floating return is an
            invalid token */
            continuation(null, docs);
            }
        );
    }

function printresult(string_input){
/* example of how findElem can be passed into other functions in the main thread
    without asynchronous screwups */
    findElem("userCollection", {"age":{$gte:1}}, function(err, ans){
        var crew = [];
        for (var i = 0; i < ans.length; i++) {
            crew.push(ans[i][string_input])
        }
        console.log(crew);
    });
    }

printresult('first_name');
/* example function executed */
