// SPDX-Library-Identifier: MIT
pragma solidity ^0.8.0;

contract PreservationHack {
    uint256 slot1 = 0;
    uint256 slot2 = 0;
    uint256 slot3;

    function setTime(uint256 _time) public {
        slot3 = _time;
    }
}
