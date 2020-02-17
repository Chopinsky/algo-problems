"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var BFSResultSpread = function (result) {
    return {
        ary: result.ary.slice(),
        score: result.score
    };
};
var ShortestSuperstring = /** @class */ (function () {
    function ShortestSuperstring() {
    }
    ShortestSuperstring.prototype.solve = function () {
        var ans = {
            ary: undefined,
            score: Infinity
        };
        var len = this.dataSet.length;
        for (var i = 0; i < len; i++) {
            var temp = this.bfs(i, i, {
                ary: [],
                score: 0
            }, new Array(len));
            if (this.debug) {
                console.log(temp);
            }
            if (temp.score < ans.score) {
                ans = temp;
            }
        }
        if (this.debug) {
            console.log(ans);
        }
        //todo: create the parsed string...
        var result = this.dataSet[ans.ary[0]];
        for (var i = 1; i < ans.ary.length; i++) {
            var parentIndex = ans.ary[i - 1];
            var index = ans.ary[i];
            var word = this.dataSet[index];
            result += word.substring(word.length - this.g[parentIndex][index]);
        }
        console.log("\n      Answer:   " + result + " (length: " + result.length + ")\n      Expected: " + this.answer + " (length: " + this.answer.length + ")\n    ");
    };
    ShortestSuperstring.prototype.make = function (caseNum, debug) {
        var testCase = this.genTestCase(caseNum);
        if (!testCase || !testCase.data) {
            return;
        }
        this.dataSet = testCase.data;
        this.answer = testCase.target;
        this.debug = debug;
        var len = this.dataSet.length;
        this.g = new Array(len);
        for (var i = 0; i < len; i++) {
            this.g[i] = new Array(len);
            for (var j = 0; j < len; j++) {
                this.g[i][j] =
                    i === j
                        ? this.dataSet[i].length
                        : this.calcOverlap(this.dataSet[i], this.dataSet[j]);
            }
        }
        if (this.debug) {
            console.log(this.g);
        }
    };
    ShortestSuperstring.prototype.genTestCase = function (caseNum) {
        switch (caseNum) {
            case 1:
                return Executor_1.TestCaseFactory(["alex", "loves", "leetcode"], "alexlovesleetcode");
            case 2:
                return Executor_1.TestCaseFactory(["ads", "bad", "dsg", "gg"], "badsgg");
            default:
                return Executor_1.TestCaseFactory(["catg", "ctaagt", "gcta", "ttca", "atgcatc"], "gctaagttcatgcatc");
        }
    };
    ShortestSuperstring.prototype.calcOverlap = function (a, b) {
        if (!a || a.length === 0 || !b || b.length === 0) {
            return 0;
        }
        var ans = b.length;
        var head = a.length >= b.length ? a.length - b.length : 0;
        var len = a.length - head;
        for (var i = head; i < a.length; i++) {
            if (a.substring(i) === b.substr(0, len)) {
                return b.length - len;
            }
            len--;
        }
        return ans;
    };
    ShortestSuperstring.prototype.bfs = function (parent, node, result, visited) {
        if (visited[node] === true) {
            return result;
        }
        result.score += this.g[parent][node];
        result.ary.push(node);
        visited[node] = true;
        var ans = result;
        var minScore = Infinity;
        for (var i = 0; i < this.dataSet.length; i++) {
            if (!visited[i]) {
                var temp = this.bfs(node, i, BFSResultSpread(result), visited.slice());
                if (temp.score < minScore) {
                    ans = temp;
                    minScore = temp.score;
                }
            }
        }
        return ans;
    };
    return ShortestSuperstring;
}());
exports.ShortestSuperstring = ShortestSuperstring;
