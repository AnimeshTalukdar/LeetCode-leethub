/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var counter = init;
    var curValue = init;
    return {
        increment: function() {
            
            return ++curValue;
        },
        reset: function() {
            curValue = counter;
            return counter;
        },
        decrement: function() {
            
            return --curValue;
        }
    }
}

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */