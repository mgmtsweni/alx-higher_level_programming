#!/usr/bin/node

exports.esrever = function (list) {
  const rev = [];
  for (const i = 0; i < list.length; i++) {
    rev.unshift(list[i]);
  }
  return rev;
};
