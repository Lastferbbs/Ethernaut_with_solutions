Level 1 - Fallback
 https://medium.com/@lastferbbs/ethernaut-web3-solidity-based-wargame-level-1-with-solution-471788454082

Level 2 -Fallout
In older version of solidity (up to 0.4.21) consturctor was defined as a function with the same name as a contract
Since version 0.4.22 constructor keyword exists.
Problem with this level is that contract name is Fallout and the function name is Fal1out - if u call the function Fal1out u become contract owner.

Level 3 - Coin flip
In solidity, there is no native way to generate random number, safe and popular method is a chainlink oracle.
Contract that we are given use blockhash to generate random number.
To exploit it we use similar contract that check right answer and from our contract we call exploided contract with answer.

Level 4 - Telephone
Tx.origin and msg.sender aren't the same things. 
Tx.origin is never a contract, it is a origin of transaction - user address it was originally sent from.
msg.sender - gives the direct sender of the emmsage, so for example a contract that passed it along.

Level 5 - Token
In older version of solidity overflow and underflow could happened.
So if u subract 1 from uint = 0 u would get max positive value of that uint. - underflow

Level 6 - Delegation
By using delegatecall it is pretty easy to override value of your main contract.
More research needed, there will be article about it soon.

Level 7 - Force
To force ether to the contract that won't accept transfer, there are 2 ways, as a block mining reward and by using selfdestruct, which deletes contract from blockchain and sends remaining ether to designated address.

Level 8 - Vault
Blockchain is a public database, even if private quantifier it only means that variables and functions can only be used internally and not even by derived contracts. But value still can be readed.

To do it we will use python module named web3py and its function eth.get_storage_at()

Level 9 - King
This level use standard transfer function (23000 gas limit) which use 21000 gas, when our receive function use more than 2k gas, it will break this contract


things to note: can only use call, because of gas limit, also has to set gas, both? in contract? and in brownie

Level 10 - Reentrancy
We are using call inside withdraw function to call withdraw function again and again, this way we can empty whole contract without problems and because if call failed it won't revert whole transaction we are able get all ether.

Level 11 - Elevator
Dwa rozwiązania, jedno, które zastosowałem, czyli zaleznie od zapytania funkcja zwraca inną wartość.
Drugie, co call funkcja zmienia wartość boola, wtedy raz zwraca true raz false

Two possible solutions
1. depending on the query, the function returns a different value - I used this
2. every call function changes the boolean value, then it returns true once and false next time

Level 12 - Privacy
Rather easy task, if u can find rules how elements are stored in storage e. g. every element in array has its own slow.
https://medium.com/@dariusdev/how-to-read-ethereum-contract-storage-44252c8af925
Read more about padding and truncating

Level 13 - Gatekeeper One
This level needs good debug to know how much gas we have left. To calculate key we take 8 bytes of our address (16 chars), then we take last 4 chars from address then we add 4 zeros then we add 4 chars and 1 must be non zero, then we add 4 random bytes. 

Level 14 - Gatekeeper Two
First gate is opened by external contract, second is opened by putting contract code in constructor, then extcodesize is 0, to get key to third gate we need calculate this -  (uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey) == uint64(0) - 1)

It can be done this way - bytes8(uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^0xffffffffffffffff

so after using _gateKey in third gate we will get max value of uint64

Level 15  - Naught Coin
To complete level we need to use transferFrom and let other contract approve to transfer our coins.

Level 16 - Preservation
To complete this level we need to take advantage of context-preserving in delegatecall. First we insert our library inside timezome1library by putting address to this library in integer format. It will overwrite this variable (instead of storedTime, because it is using first slot and first slot is address to library. Then we need use to our library to override 3rd slot, using same method.

Level 17 - Recovery
Level which is very simple using etherscan, there is also another way to find lost address, by calculating it using nonce and address.

Level 18 - Magic Number
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

Level 19 - Alien Codex
Things to do, in order:
1. Delete elements from array to underflow its value (=0xfff...)
2. Find last space in storage (2^256-1) and add one to it. This is index of storage 0
3. Change value of this storage to 0x + 000000000000000000000000 + your address
4. Done

This level exploits the fact that the EVM doesn't validate an array's ABI-encoded length vs its actual payload. - why?

Level 20 - Denial
Im my opinion, level should be deleted from Ethernaut:
1. Bug can be easy reverted by changing partner, even for owner address
2. It is almost the same as reentrancy level, which method can also be used here
3. Can use infinite loop or assert to use all the gas, but still description doesn't make sense cuz it will use all the gas, not less than milion

Nodes:
1. External call use max 63/64 of all gas
2. Gas for external calls can be specified {gas: 100000}
3. https://docs.soliditylang.org/en/latest/security-considerations.html#use-the-checks-effects-interactions-pattern

Level 21 - Shop
Level very similar to elevator, my solution will be the same.

Level 22 - Dex
It's easy, expoit how price is calculated and use your tokens to drain liquidity of one of them.

Level 23 - Dex Two
Almost the same level as Dex, but there is no token check, it means that we can use any token to trade for one we want, just send it to contract
calculate ratio to drain all 100 and trade.