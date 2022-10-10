// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;

contract PasswordHack {
    address externalContract = 0x0c76A3a79E6687967fC1a1517B574287882e3E20;
    string text = "A very strong secret password :)";
    bytes32 stringInBytes32 = bytes32(bytes(text));

    function unlock() public {
        externalContract.call(
            abi.encodeWithSignature("unlock(bytes32)", stringInBytes32)
        );
    }
}
