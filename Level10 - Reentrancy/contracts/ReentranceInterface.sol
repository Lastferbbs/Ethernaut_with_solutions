pragma solidity ^0.8.0;

interface ReentranceInterface {
    function balanceOf(address _who) external view returns (uint256 balance);
}
