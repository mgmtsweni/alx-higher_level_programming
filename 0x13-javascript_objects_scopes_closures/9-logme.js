#!/usr/bin/node

let i = -1;
exports.logMe = function (item) {
    i++;
    console.log(i + '; ' + item);
};
