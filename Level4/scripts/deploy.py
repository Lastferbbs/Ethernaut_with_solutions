from brownie import TelephoneHack, accounts
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    hack = TelephoneHack.deploy(
        "0xC5fb2eF9582Ec5bCCF5BB8f7F6EbD6c94843f10f", {"from": account}
    )
