# 1. Import the gas strategy
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from web3 import Web3

# 2. Add the Web3 provider logic here:
# {...}

# 3. Create address variables
account_from = {
    "private_key": "0xb4ca9bf25e7d6f11ae795d693e2c72fa3f0aedc619e107466e66aafc96e17fa0",
    "address": "0xC5fb2eF9582Ec5bCCF5BB8f7F6EbD6c94843f10f",
}
address_to = "0x0000000000000000000000000000000000000000"

print(
    f'Attempting to send transaction from { account_from["address"] } to { address_to }'
)
web3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/83497ae5682b40678d5e9a61a26701aa")
)

# 4. Set the gas price strategy
web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

# 5. Sign tx with PK
tx_create = web3.eth.account.sign_transaction(
    {
        "nonce": web3.eth.get_transaction_count(account_from["address"]),
        "gasPrice": web3.eth.generate_gas_price(),
        "gas": 100000,
        "to": address_to,
        "data": "0x60406080526080602a608052602090f3",
    },
    account_from["private_key"],
)

# 6. Send tx and wait for receipt
tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction successful with hash: { tx_receipt.transactionHash.hex() }")
