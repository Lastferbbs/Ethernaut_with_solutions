// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ExternalCall {
    address externalContract = 0xbE7ACa394B73E1483C5B2B9276cF1Df057328A4b;

    function calling(address _receiver, uint256 _value) public {
        externalContract.call(
            abi.encodeWithSignature(
                "fastSafeTransfer(address, uint)",
                _receiver,
                _value
            )
        );
    }
}
