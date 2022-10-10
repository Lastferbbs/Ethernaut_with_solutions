from brownie import PreservationHack, accounts, interface
from scripts.helpful_scripts import get_account
from web3 import Web3


def main():
    account = get_account()
    hack = PreservationHack[-1].deploy({"from": account})
    # hack.unlock({"from": account})
