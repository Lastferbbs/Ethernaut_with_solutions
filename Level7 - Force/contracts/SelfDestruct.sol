// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;

contract SelfDestruct {
    function destroy(address payable addr) public payable {
        selfdestruct(addr);
    }
}
