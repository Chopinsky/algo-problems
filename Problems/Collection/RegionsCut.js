"use strict";
exports.__esModule = true;
var Executor_1 = require("../Executor");
var dsu_1 = require("../../Utils/dsu");
var RegionsCut = /** @class */ (function () {
    function RegionsCut() {
    }
    RegionsCut.prototype.genTestCase = function (caseNum) {
        var data;
        var result;
        switch (caseNum) {
            case 1:
                data = [];
                result = "";
            default:
                data = [[" ", "/"], ["/", " "]];
                result = 2;
        }
        return Executor_1.TestCaseFactory(data, result);
    };
    RegionsCut.prototype.make = function (caseNum, debug) {
        var test = this.genTestCase(caseNum);
        this.ans = test.target;
        this.grid = test.data;
        var len = this.grid.length;
        this.dsu = new dsu_1["default"](4 * len * len);
        this.debug = debug;
    };
    RegionsCut.prototype.solve = function () {
        var len = this.grid.length;
        // loop over cubics
        for (var c = 0; c < len; c++) {
            // loop over triangles
            for (var t = 0; t < len; t++) {
                var base = 4 * (c * len + t);
                switch (this.grid[c][t]) {
                    case "/":
                        this.dsu.merge(base + 0, base + 3);
                        this.dsu.merge(base + 1, base + 2);
                        break;
                    case "\\":
                        this.dsu.merge(base + 0, base + 1);
                        this.dsu.merge(base + 2, base + 3);
                        break;
                    case " ":
                        this.dsu.merge(base + 0, base + 1);
                        this.dsu.merge(base + 1, base + 2);
                        this.dsu.merge(base + 2, base + 3);
                        break;
                    default:
                        break;
                }
                if (c + 1 < len) {
                    // merge 2 and 0 from the cubic below
                    this.dsu.merge(base + 2, base + 4 * len + 0);
                }
                if (t + 1 < len) {
                    // merge 1 and 3 from the cubic to the right
                    this.dsu.merge(base + 1, base + 4 + 3);
                }
            }
        }
        if (this.debug) {
            this.dsu.debug();
        }
        var ans = 0;
        for (var i = 0; i < 4 * len * len; i++) {
            if (this.debug) {
                console.log(i + " -- " + this.dsu.find(i));
            }
            if (this.dsu.find(i) === i) {
                ans++;
            }
        }
        console.log("Result: " + ans);
        console.log("Expected: " + this.ans);
    };
    return RegionsCut;
}());
exports.RegionsCut = RegionsCut;
