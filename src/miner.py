import BlockChain
import Block


blockchain = BlockChain()

print("***Mining ElmoCoin about to start***")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",  #implies new block
    recipient="Elmo",
    quantity=
    1,  #new block
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("***Mining ElmoCoin has been successful***")
print(blockchain.chain)
