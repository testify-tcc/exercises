"use strict";

export function substringsBetween(
  str: string | null,
  open: string,
  close: string
): string[] | null {
  if (str === null || open === null || close === null) {
    return null;
  }
  const strLen = str.length;
  const openLen = open.length;
  const closeLen = close.length;
  if (closeLen === 0 || openLen === 0) {
    return null;
  }
  if (strLen === 0) {
    return [];
  }
  const list: string[] = [];
  let pos = 0;
  while (pos < strLen - closeLen) {
    let start = str.indexOf(open, pos);
    if (start < 0) {
      break;
    }
    start += openLen;
    let end = str.indexOf(close, start);
    if (end < 0) {
      break;
    }
    list.push(str.substring(start, end));
    pos = end + closeLen;
  }
  if (list.length === 0) {
    return null;
  }
  return list;
}
