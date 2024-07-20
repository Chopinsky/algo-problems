/**
 * 2637. Promise Time Limit
 * 
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function(fn, t) {
  return async function(...args) {
    return new Promise(async (res, rej) => {
      setTimeout(() => rej("Time Limit Exceeded"), t);
      
      try {
        const result = await fn(...args);
        return res(result);
      } catch (err) {
        return rej(err);
      }
    }).catch((err) => {
      throw err;
    });
  }
};

var timeLimit = function(fn, t) {
  return async function(...args) {
    let result = null;
    let error = null;
    let status = "pending";
    
    await new Promise(async (res, rej) => {
      setTimeout(() => rej("Time Limit Exceeded"), t);
      
      try {
        result = await fn(...args);
        status = "done";
        return res(result);
      } catch (err) {
        return rej(err);
      }
    }).catch((err) => {
      error = err;
      status = "error";
    });
    
    // console.log(status, result, error);
    
    if (status === 'done') {
      return result;
    }
    
    if (status === 'error') {
      throw error;
    }
    
    throw "Time Limit Exceeded";
  }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */