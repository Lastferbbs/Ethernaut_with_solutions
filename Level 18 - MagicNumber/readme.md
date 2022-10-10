Level looks very hard, but with this resource https://blog.openzeppelin.com/deconstructing-a-solidity-contract-part-vi-the-swarm-hash-70f069e22aef/faswz
it is manageable.

Plan is:
1. Write normal solidity code
2. Debug it with knowledge what popular opcodes do
3. Try to write simple bytecode, skipping wrapper, checks and even function - pure return
4. Function is PUSH1 2a PUSH1 80 MSTORE PUSH1 20 PUSH1 80 RETURN 0x602a60805260206080f3
5. What code is doing: PUSH1 2a PUSH1 80 MSTORE - value is in hex - Store in memory value 2a, at address 80
PUSH1 20 PUSH1 80 RETURN - Return value from memory address 80 that is 20 long (32 bytes)
6. Pretty simple, needed 2 days of research!
7. Also worth to mention that at first values to go stack, which is First In Last Out, then is added to memory, and returned from memory also.