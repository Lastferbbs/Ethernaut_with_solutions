Im my opinion, level should be deleted from Ethernaut:
1. Bug can be easy reverted by changing partner, even for owner address
2. It is almost the same as reentrancy level, which method can also be used here
3. Can use infinite loop or assert to use all the gas, but still description doesn't make sense cuz it will use all the gas, not less than milion

Nodes:
1. External call use max 63/64 of all gas
2. Gas for external calls can be specified {gas: 100000}
3. https://docs.soliditylang.org/en/latest/security-considerations.html#use-the-checks-effects-interactions-pattern