Things to do, in order:
1. Delete elements from array to underflow its value (=0xfff...)
2. Find last space in storage (2^256-1) and add one to it. This is index of storage 0
3. Change value of this storage to 0x + 000000000000000000000000 + your address
4. Done

This level exploits the fact that the EVM doesn't validate an array's ABI-encoded length vs its actual payload. - why?