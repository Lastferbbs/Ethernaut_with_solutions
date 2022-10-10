from brownie import Contract, accounts, interface
from scripts.helpful_scripts import get_account
import web3


def main():
    cont = interface.InterfaceToken("0x08eeEe982fd99190CbdEeA9E73B199a449a3F2a1")
    account = get_account()
    cont.transfer("0x31a3801499618d3c4b0225b9e06e228d4795b55d", 1000, {"from": account})
    print(Web3.toHex(Web3.keccak(text="balanceOf(address)"))[0:10])
