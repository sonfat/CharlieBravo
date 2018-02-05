import hashlib as hashder

class Block():
    def __init__(self, index, timestamp, data, pre_hash):
        self.index = index          #serial number
        self.timestamp = timestamp  #timestamp
        self.data = data            #block data
        self.pre_hash = pre_hash    #hash of the pre-block
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashder.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.pre_hash)).encode("utf8"))
        return sha.hexdigest()