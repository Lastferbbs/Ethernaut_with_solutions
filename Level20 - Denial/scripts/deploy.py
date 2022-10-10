from brownie import Denial, accounts, interface, network
from scripts.helpful_scripts import get_account
from web3 import Web3


# network.gas_limit(200000)


def main():
    account = get_account()
    print("aaaaaa")
    hack = Denial.deploy(
        {
            "from": account,
        }
    )
    # print(hack.getFloor())
    # hack.ride(10, {"from": account})
    # print(hack.getFloor())
