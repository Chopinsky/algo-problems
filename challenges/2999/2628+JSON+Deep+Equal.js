/**
2628. JSON Deep Equal

Given two objects o1 and o2, check if they are deeply equal.

For two objects to be deeply equal, they must contain the same keys, and the associated values must also be deeply equal. Two objects are also considered deeply equal if they pass the === equality check.

You may assume both objects are the output of JSON.parse. In other words, they are valid JSON.

Please solve it without using lodash's _.isEqual() function.

Example 1:

Input: o1 = {"x":1,"y":2}, o2 = {"x":1,"y":2}
Output: true
Explanation: The keys and values match exactly.
Example 2:

Input: o1 = {"y":2,"x":1}, o2 = {"x":1,"y":2}
Output: true
Explanation: Although the keys are in a different order, they still match exactly.
Example 3:

Input: o1 = {"x":null,"L":[1,2,3]}, o2 = {"x":null,"L":["1","2","3"]}
Output: false
Explanation: The array of numbers is different from the array of strings.
Example 4:

Input: o1 = true, o2 = false
Output: false
Explanation: true !== false

Constraints:

1 <= JSON.stringify(o1).length <= 10^5
1 <= JSON.stringify(o2).length <= 10^5
maxNestingDepth <= 1000
 */

/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
  if (o1 === o2) {
    return true;
  }
  
  let t1 = typeof o1;
  let t2 = typeof o2;
  if (t1 !== t2) {
    return false;
  }
  
  if (t1 === 'string' || t1 === 'number' || t1 === 'boolean' || t1 === null || t2 === null) {
    return false;
  }
  
  let a1 = Array.isArray(o1);
  let a2 = Array.isArray(o2);
  if (a1 !== a2) {
    return false;
  }
  
  // is array
  if (a1) {
    if (o1.length != o2.length) {
      return false;
    }
    
    for (let i = 0; i < o1.length; i++) {
      if (!areDeeplyEqual(o1[i], o2[i])) {
        return false
      }
    }
    
    return true;
  }
  
  // is object
  let k1 = Object.keys(o1);
  let k2 = Object.keys(o2);
  if (k1.length != k2.length) {
    return false;
  }
  
  for (let i = 0; i < k1.length; i++) {
    let key = k1[i];
    if (!(key in o2)) {
      return false;
    }
    
    if (!areDeeplyEqual(o1[key], o2[key])) {
      return false;
    }
  }
  
  return true;
};