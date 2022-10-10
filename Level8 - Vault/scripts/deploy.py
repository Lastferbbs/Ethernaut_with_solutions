from brownie import PasswordHack, accounts, interface
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    account = get_account()
    hack = PasswordHack.deploy({"from": account})
    hack.unlock({"from": account})
