from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    # 1 // print out the account
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    # 2 // deploy the contract
    # account = accounts[0]
    # simple_storage = SimpleStorage.deploy({"from": account})
    # print(simple_storage)

    # 3 // access the retrieve and store function inside the contract
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
