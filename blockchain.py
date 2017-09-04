import hashlib 
import datetime 

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block(self):
		hash = hashlib.sha256()
		hash.update(str(self.index) +
					str(self.timestamp) +
					str(self.data) + 
					str(self.previous_hash))

		return hash.hexdigest()

def genesis_block():
	return Block(0, datetime.datetime.now(), "Genesis Block", "0")

def next_block(previous_block):
	index = previous_block.index + 1
	timestamp = datetime.datetime.now()
	data = "I am block #" + str(index)
	previous_hash = previous_block.hash
	return Block(index, timestamp, data, previous_hash)

blockchain = [genesis_block()]
previous_block = blockchain[0]

for i in range(0, 50):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add

	print("Block #" + str(block_to_add.index) + " has been added to the blockchain")
	print("Timestamp: " + str(block_to_add.timestamp))
	print("Data: " + str(block_to_add.data))
	print("Previous Hash: " + str(block_to_add.previous_hash))
	print("Hash: " + str(block_to_add.hash) + "\n")



# Resources: https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d

