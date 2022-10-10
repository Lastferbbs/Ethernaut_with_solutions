Tx.origin and msg.sender aren't the same things. 
Tx.origin is never a contract, it is a origin of transaction - user address it was originally sent from.
msg.sender - gives the direct sender of the emmsage, so for example a contract that passed it along.