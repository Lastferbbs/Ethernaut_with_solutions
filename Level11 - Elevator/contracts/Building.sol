// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;

interface Elevator {
    function floor() external view returns (uint256);

    function goTo(uint256 _floor) external;
}

contract Building {
    Elevator elevator = Elevator(0xfef886bbB3f2e4eF6B352850fFA8338a494c02d5);

    function isLastFloor(uint256 _floor) public returns (bool) {
        uint256 floor = elevator.floor();

        if (_floor == floor) {
            return true;
        } else {
            return false;
        }
    }

    function ride(uint256 space) public {
        elevator.goTo(space);
    }

    function getFloor() public view returns (uint256) {
        return elevator.floor();
    }
}
