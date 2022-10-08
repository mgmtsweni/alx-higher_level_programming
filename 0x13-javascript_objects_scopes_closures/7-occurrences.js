#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = 0;
  for (const num in list) {
    if (list[num] === searchElement) {
        count++;
    }
  }
  return count;
};
