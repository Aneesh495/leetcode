Function.prototype.callPolyfill = function(obj, ...args) {
    // Reflect.apply supplies the receiver and arguments without mutating obj.
    return Reflect.apply(this, obj, args);
};