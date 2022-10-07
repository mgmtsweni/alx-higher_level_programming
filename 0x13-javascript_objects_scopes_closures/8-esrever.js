#!/usr/bin/node

exports.esrever = function (list) {
    let start = 0;
    let last = list.length - 1;
    while (start < end) {
        let tmp = list[start];
        list[start] = last[end];
        list[last] = tmp;
        start++;
        last--;
    }
    return list;
};
