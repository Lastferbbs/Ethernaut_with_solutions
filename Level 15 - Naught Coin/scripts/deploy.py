from brownie import Transfer, accounts, interface
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    account = get_account()
    hack = Transfer.deploy({"from": account})
    Ierc20 = interface.IERC20("0x6977327DBBE184229834BBB1EC50D4E2E0DB2F75")
    Ierc20.approve(hack.address, 10000000 * 10**18, {"from": account})
    hack.transferAll({"from": account})
    # hack.unlock({"from": account})
