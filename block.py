# import json
# from web3 import Web3

# ganache_url = "HTTP://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))


# abi=json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"company","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"freelancer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_freelancer","type":"address"}],"name":"getFreelancer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_delay","type":"uint256"}],"name":"paySalary","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_hourlyPay","type":"uint256"},{"internalType":"uint256","name":"_maxDuration","type":"uint256"},{"internalType":"uint256","name":"_penaltyPerHour","type":"uint256"}],"name":"setVals","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# # abi=json.loads('[{"inputs":[{"internalType":"address","name":"_sender","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"company","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"freelancer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_freelancer","type":"address"}],"name":"getFreelancer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_delay","type":"uint256"}],"name":"paySalary","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_hourlyPay","type":"uint256"},{"internalType":"uint256","name":"_maxDuration","type":"uint256"},{"internalType":"uint256","name":"_penaltyPerHour","type":"uint256"}],"name":"setVals","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# # abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"company","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"freelancer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_freelancer","type":"address"}],"name":"getFreelancer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_delay","type":"uint256"}],"name":"paySalary","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_hourlyPay","type":"uint256"},{"internalType":"uint256","name":"_maxDuration","type":"uint256"},{"internalType":"uint256","name":"_penaltyPerHour","type":"uint256"}],"name":"setVals","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
# # bytecode = "608060405234801561001057600080fd5b5060405161037e38038061037e8339818101604052602081101561003357600080fd5b8101908080519060200190929190505050806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506000600481905550600060038190555060006005819055506064600281905550506102ca806100b46000396000f3fe608060405234801561001057600080fd5b50600436106100625760003560e01c806312065fe01461006757806320c4c1e81461008557806358768831146100c757806364df6ab1146101095780636904c94d1461014d578063a37dda2c14610181575b600080fd5b61006f6101b5565b6040518082815260200191505060405180910390f35b6100b16004803603602081101561009b57600080fd5b81019080803590602001909291905050506101bf565b6040518082815260200191505060405180910390f35b610107600480360360608110156100dd57600080fd5b810190808035906020019092919080359060200190929190803590602001909291905050506101ec565b005b61014b6004803603602081101561011f57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610206565b005b61015561024a565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b61018961026e565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000600254905090565b60008160055402600454600354020360025403600281905550816005540260045460035402039050919050565b816004819055508260038190555080600581905550505050565b80600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168156fea26469706673582212204321821152848134ba6f8a08cd85ebe136117f4457995edc976cc361f39f598064736f6c634300060c0033"


# # bytecode = '608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060006004819055506000600381905550600060058190555060646002819055506102ca806100806000396000f3fe608060405234801561001057600080fd5b50600436106100625760003560e01c806312065fe01461006757806320c4c1e81461008557806358768831146100c757806364df6ab1146101095780636904c94d1461014d578063a37dda2c14610181575b600080fd5b61006f6101b5565b6040518082815260200191505060405180910390f35b6100b16004803603602081101561009b57600080fd5b81019080803590602001909291905050506101bf565b6040518082815260200191505060405180910390f35b610107600480360360608110156100dd57600080fd5b810190808035906020019092919080359060200190929190803590602001909291905050506101ec565b005b61014b6004803603602081101561011f57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610206565b005b61015561024a565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b61018961026e565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000600254905090565b60008160055402600454600354020360025403600281905550816005540260045460035402039050919050565b816004819055508260038190555080600581905550505050565b80600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168156fea264697066735822122024ef0da860d07923d202f59ba3d9f00ecd16066f3f499e005dcb5ee5a50fb9a964736f6c634300060c0033'
# # abi = json.loads('[{"inputs": [{"internalType": "uint256", "name": "_hourlyPay", "type": "uint256"}, {"internalType": "uint256", "name": "_maxDuration", "type": "uint256"}, {"internalType": "uint256", "name": "_penaltyPerHour", "type": "uint256"}], "stateMutability": "nonpayable", "type": "constructor"}, {"inputs": [], "name":"company", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"freelancer", "outputs":[{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name":"getBalance", "outputs":[{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "_freelancer", "type": "address"}], "name": "getFreelancer", "outputs": [], "stateMutability":"nonpayable", "type":"function"}, {"inputs": [{"internalType": "uint256", "name": "_delay", "type": "uint256"}], "name": "paySalary", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "nonpayable", "type": "function"}]')
# # bytecode = "608060405234801561001057600080fd5b5060405161032a38038061032a8339818101604052606081101561003357600080fd5b81019080805190602001909291908051906020019092919080519060200190929190505050336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508160048190555082600381905550806005819055506064600281905550505050610263806100c76000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c806312065fe01461005c57806320c4c1e81461007a57806364df6ab1146100bc5780636904c94d14610100578063a37dda2c14610134575b600080fd5b610064610168565b6040518082815260200191505060405180910390f35b6100a66004803603602081101561009057600080fd5b8101908080359060200190929190505050610172565b6040518082815260200191505060405180910390f35b6100fe600480360360208110156100d257600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061019f565b005b6101086101e3565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b61013c610207565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000600254905090565b60008160055402600454600354020360025403600281905550816005540260045460035402039050919050565b80600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168156fea264697066735822122085dec3e0ea8a42b7691b27d7f98557495b493364f2b2aad3289904e1ba98f6ab64736f6c63430007040033"
# # Wallet = web3.eth.contract(address=address, abi=abi)
# address = web3.toChecksumAddress('0x383D61B79a3Be2AA20f78f0EbE7cb892dA651Cce')
# contract = web3.eth.contract(address=address, abi=abi)

# # web3.eth.defaultAccount = "0x2Dc03C5287fFeDC2b8d344987635125207f5b988"

# HourlyPay = 1
# MaxDuration = 2
# PenaltyPerHour = 3


# def callconstructor(hourlypay, maxDuration, penaltyperhour):
#     global HourlyPay
#     global MaxDuration
#     global PenaltyPerHour
#     HourlyPay = hourlypay
#     MaxDuration = maxDuration
#     PenaltyPerHour = penaltyperhour


# # print("YOOOOOOOOOOOO", HourlyPay, MaxDuration, PenaltyPerHour)
# # # tx1_hash = Wallet.constructor("0x2Dc03C5287fFeDC2b8d344987635125207f5b988").transact()
# # # tx_receipt = web3.eth.waitForTransactionReceipt(tx1_hash)

# # tx1_hash = Wallet.constructor("0x2Dc03C5287fFeDC2b8d344987635125207f5b988").transact()
# # tx_receipt = web3.eth.waitForTransactionReceipt(tx1_hash)
# # wallet = web3.eth.contract(address=tx_receipt.contractAddress, abi=abi)


# # print(tx_receipt.contractAddress)

# # wallet = web3.eth.contract(
# #     address=tx_receipt.contractAddress,
# #     abi=abi
# # )

# constructorMade = contract.functions.setVals(HourlyPay, MaxDuration, PenaltyPerHour).transact()
# print(constructorMade)


# # def transaction(account1, account2, privateKey, money):
# #     nonce = web3.eth.getTransactionCount(account1)
# #     tx = {
# #         'nonce': nonce,
# #         'to': account2,
# #         'value': web3.toWei(money, 'ether'),
# #         'gas': 2000000,
# #         'gasPrice': web3.toWei('50', 'gwei'),
# #     }
# #     signed_tx = web3.eth.account.signTransaction(tx, privateKey)
# #     tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# #     return web3.toHex(tx_hash)
# # #   print(web3.toHex(tx_hash))


# # def transferMoneyToFreelancer(companyAddress, freelancerAddress, privateKey, delay):
# #     amountToPay = wallet.functions.paySalary(delay).call()
# #     transaction(companyAddress, freelancerAddress, privateKey, amountToPay)


# # def transferMoneyToFamilyMember(freelancerAddress, familyMemberAddress, privateKey, amount):
# #     transaction(freelancerAddress, familyMemberAddress, privateKey, amount)


# # def getContractBalance():
# #     return wallet.functions.getBalance().call()


# # def getAccountBalance(address):
# #     return web3.eth.getBalance(address)


# # def addFreelancerToContract(freelancerAddress):
# #     wallet.functions.getFreelancer(web3.toChecksumAddress(freelancerAddress))


# import json
# from web3 import Web3
# ganache_url = "HTTP://127.0.0.1:7545"
# web3 = Web3(Web3.HTTPProvider(ganache_url))

# MaxDuration = 1
# HourlyPay = 2
# PenaltyPerHour = 3
# # employerAddress=#


# def callconstructor(hourlypay, maxDuration, penaltyperhour):
#     global HourlyPay
#     global MaxDuration
#     global PenaltyPerHour
#     HourlyPay = hourlypay
#     MaxDuration = maxDuration
#     PenaltyPerHour = penaltyperhour


# web3.eth.defaultAccount = web3.eth.accounts[0]
# abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"company","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"freelancer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_freelancer","type":"address"}],"name":"getFreelancer","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_delay","type":"uint256"}],"name":"paySalary","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_hourlyPay","type":"uint256"},{"internalType":"uint256","name":"_maxDuration","type":"uint256"},{"internalType":"uint256","name":"_penaltyPerHour","type":"uint256"}],"name":"setVals","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

# address = web3.toChecksumAddress('0x4E73186C7425ca644aBA07d519a88D5d9ec9d328')
# contract = web3.eth.contract(address=address, abi=abi)

# constructorMade = contract.functions.setVals(
#     HourlyPay, MaxDuration, PenaltyPerHour).transact()
# print(constructorMade)


# def transaction(account1, account2, privateKey, money):
#     nonce = web3.eth.getTransactionCount(account1)
#     tx = {
#         'nonce': nonce,
#         'to': account2,
#         'value': web3.toWei(money, 'ether'),
#         'gas': 2000000,
#         'gasPrice': web3.toWei('50', 'gwei'),
#     }
#     signed_tx = web3.eth.account.signTransaction(tx, privateKey)
#     tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#     return web3.toHex(tx_hash)
# #   print(web3.toHex(tx_hash))


# def transferMoneyToFreelancer(companyAddress, freelancerAddress, privateKey, delay):
#     amountToPay = contract.functions.paySalary(delay).call()
#     transaction(companyAddress, freelancerAddress, privateKey, amountToPay)


# def transferMoneyToFamilyMember(freelancerAddress, familyMemberAddress, privateKey, amount):
#     transaction(freelancerAddress, familyMemberAddress, privateKey, amount)


# def getContractBalance():
#     return contract.functions.getBalance().call()


# def getAccountBalance(address):
#     return web3.eth.getBalance(address)


# def addFreelancerToContract(freelancerAddress):
#     contract.functions.getFreelancer(web3.toChecksumAddress(freelancerAddress))

# transaction("0x2Dc03C5287fFeDC2b8d344987635125207f5b988","0xE3A6C42F9F406a54a27E8F240c778E08F2995243","b6c1c2e89ed113e1f629dbb6fd2e801f1931024e91b07e229241ebb4a5acf8d6",1)
