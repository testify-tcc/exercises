"use strict";

export function substringsBetween(
  str: string | null,
  open: string | null,
  close: string | null
): string[] | null {
  if (str == null || open == null || open.length == 0 || close == null || close.length == 0) {
    return null;
  }
  const strLen = str.length;
  if (strLen === 0) {
    return [];
  }
  const closeLen = close.length;
  const openLen = open.length;
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
