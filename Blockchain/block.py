import hashlib

class Block:
    def __init__(self, infomation: str, previous_hash):
        self.previous_hash = previous_hash
        self.info = infomation
        self.key = None
        self.hash = None

    def test_key(self, given_key: int):
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
        print(f"""
---------------------------------
Data: {self.info}
Key: {self.key}
Hash: {self.hash}
---------------------------------
              """)