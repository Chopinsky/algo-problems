/**
 * 2721. Execute Asynchronous Functions in Parallel
 * 
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
  return new Promise((res, rej) => {
    if (!functions || !functions.length) {
      return res([]);
    }
    
    let counter = 0;
    const array = Array(functions.length);
    
    try {
      for (let i = 0; i < functions.length; i++) {
        functions[i]()
          .then((ans) => {
            array[i] = ans;
            counter++;
          
            if (counter === functions.length) {
              return res(array);
            }
          }).catch((err) => rej(err));
      }
    } catch (err) {
      return rej(err);
    }
  });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */