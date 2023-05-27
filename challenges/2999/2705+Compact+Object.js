/**
2705. Compact Object

Given an object or array obj, return a compact object. A compact object is the same as the original object, except with keys containing falsy values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered falsy when Boolean(value) returns false.

You may assume the obj is the output of JSON.parse. In other words, it is valid JSON.

Example 1:

Input: obj = [null, 0, false, 1]
Output: [1]
Explanation: All falsy values have been removed from the array.
Example 2:

Input: obj = {"a": null, "b": [false, 1]}
Output: {"b": [1]}
Explanation: obj["a"] and obj["b"][0] had falsy values and were removed.
Example 3:

Input: obj = [null, 0, 5, [0], [false, 16]]
Output: [5, [], [16]]
Explanation: obj[0], obj[1], obj[3][0], and obj[4][0] were falsy and removed.

Constraints:

obj is a valid JSON object
2 <= JSON.stringify(obj).length <= 10^6

 * @param {Object} obj
 * @return {Object}
 */
const compactObject = function(obj) {
  const compact = (o) => {
    const t = typeof o;
    if (t !== 'object' || o === null) {
      return Boolean(o) ? o : null;
    }
    
    if (Array.isArray(o)) {
      const res = [];
      
      o.forEach((val) => {
        const c = compact(val);
        if (Boolean(c)) {
          res.push(c);
        }
      });
      
      return res;
    }
    
    const res = {};
    // console.log(o);
    
    Object.keys(o).forEach((key) => {
      const c = compact(o[key]);
      if (Boolean(c)) {
        res[key] = c;
      }
    });
    
    return res;
  };
  
  return compact(obj);
};