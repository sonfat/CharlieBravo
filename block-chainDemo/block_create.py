import datetime as date
from block_chain_demo import Block

def create_genesis_block():
    return Block(0, date.datetime.now(), "sonfat", "0")
    # return block

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "record the laat one." + str(this_index)
    this_pre_hash = last_block.hash 
    return Block(this_index, this_timestamp, this_data,this_pre_hash)

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print ("Hash: {}\n".format(block_to_add.hash))