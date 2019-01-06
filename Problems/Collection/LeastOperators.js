"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var PairQueue = /** @class */ (function () {
    function PairQueue() {
        this._queue = [];
        this._store = {};
        this._count = 0;
    }
    PairQueue.prototype.insert = function (ops, target) {
        var key = ops + "," + target;
        if (this._store.hasOwnProperty(key)) {
            return;
        }
        this._queue.push(key);
        this._store[key] = true;
        this._count++;
    };
    PairQueue.prototype.remove = function (ops, target) {
        this.removeWithKey(ops + "," + target);
    };
    PairQueue.prototype.removeWithKey = function (key) {
        if (!key || !this._store.hasOwnProperty(key)) {
            return;
        }
        var index = this._queue.indexOf(key);
        this._queue.splice(index, 1);
        delete this._store[key];
        this._count--;
    };
    PairQueue.prototype.isEmpty = function () {
        return this._count === 0;
    };
    PairQueue.prototype.peek = function () {
        if (this._count === 0) {
            return null;
        }
        var raw = this._queue[0].split(",", 2);
        return {
            key: this._queue[0],
            ops: parseInt(raw[0]),
            target: parseInt(raw[1])
        };
    };
    return PairQueue;
}());
var LeastOperators = /** @class */ (function () {
    function LeastOperators() {
    }
    LeastOperators.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [3, 19];
                result = 5;
            case 2:
                data = [100, 1000000];
                result = 3;
            default:
                data = [5, 501];
                result = 8;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    LeastOperators.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        this.base = testCase.data[0];
        this.target = testCase.data[1];
        this.answer = testCase.target;
    };
    LeastOperators.prototype.solve = function () {
        var result = this.dijSearch();
        console.log("Needed operatiors: " + result);
        console.log("Expected operatiors: " + this.answer);
    };
    LeastOperators.prototype.dijSearch = function () {
        var seen = {};
        var queue = new PairQueue();
        queue.insert(0, this.target);
        while (!queue.isEmpty()) {
            var head = queue.peek();
            var target = head["target"];
            var ops = head["ops"];
            queue.removeWithKey(head["key"]);
            if (target === 0) {
                return ops - 1;
            }
            if (seen.hasOwnProperty(target)) {
                continue;
            }
            seen[target] = true;
            var n = Math.floor(Math.log(target) / Math.log(this.base));
            var l = target - Math.pow(this.base, n);
            if (!seen.hasOwnProperty(l)) {
                queue.insert(ops + (n === 0 ? 2 : n), l);
            }
            var r = Math.pow(this.base, n + 1) - target;
            if (!seen.hasOwnProperty(r)) {
                queue.insert(ops + n + 1, r);
            }
        }
        return -1;
    };
    return LeastOperators;
}());
exports.LeastOperators = LeastOperators;
