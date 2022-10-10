from brownie import GateTwo, accounts, interface, network
from scripts.helpful_scripts import get_account
from web3 import Web3


# network.gas_limit(200000)


def main():
    account = get_account()
    hack = GateTwo.deploy(
        {
            "from": account,
        }
    )
