from web3 import Web3

w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/83497ae5682b40678d5e9a61a26701aa")
)

# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 0))
# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 1))
# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 2))
# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 3))
password = w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 5).hex()
password = password[2:]
print(password)
start = len(password) / 2
print(start)
password = password[int(start) :]
print(password)
# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 5))
# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 6))
# print(w3.eth.get_storage_at("0x43F4c1cCb0D6Bddde721CA223B51E1E12c9BBd42", 7))
def main():
    pass
