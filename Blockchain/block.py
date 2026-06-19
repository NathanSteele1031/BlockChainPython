import hashlib

class Block:
    def __init__(self, infomation: str, previous_hash):
        """
        Stores information and the previous hash to be solved and stores it's own hash for the chain.\n
        INSTANCE VARIABLES\n
        previous_hash: str - This is the previous hash of another Block isntance.\n
        info: str - This is infomation that is being stored on this block.
        key: int - This is the key that satisfies the conditions for proof of work.
        hash: str - This is the hash after solving the proof of work of the block.
        """
        self.previous_hash = previous_hash
        self.info = infomation
        self.key = None
        self.hash = None

    def test_key(self, given_key: int):
        """
        This function takes an intager and tests if it satisfies a condtion in the hash of SHA256. If it does then the key is stored on the block along with the hash.
        """
        h = hashlib.new("sha256")
        h.update(str(self.previous_hash).encode())
        h.update(self.info.encode())
        h.update(str(given_key).encode())
        if h.hexdigest()[-6:] == "000000":
            self.key = given_key
            self.hash = h.hexdigest()
            return True
        return False
    
    def show(self):
        """
        Shows the info, key, and hash of the block in a structure way.
        """
        print(f"""
---------------------------------
Data: {self.info}
Key: {self.key}
Hash: {self.hash}
---------------------------------
              """)