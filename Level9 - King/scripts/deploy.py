from brownie import GasKing, accounts, interface, network
from scripts.helpful_scripts import get_account
from web3 import Web3


network.gas_limit(200000)


def main():
    account = get_account()
    print("aaaaaa")
    hack = GasKing.deploy(
        {
            "from": account,
        }
    )
    hack.sending({"from": account, "value": 2000000000001000})
