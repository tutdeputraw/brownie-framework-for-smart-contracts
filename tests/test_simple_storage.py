from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    expected = 0

    assert expected == simple_storage.retrieve()


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    expected = 15
    simple_storage.store(expected, {"from": account})

    assert expected == simple_storage.retrieve()
