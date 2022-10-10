In solidity, there is no native way to generate random number, safe and popular method is a chainlink oracle.

Contract that we are given use blockhash to generate random number.

To exploit it we use similar contract that check right answer and from our contract we call exploided contract with answer.