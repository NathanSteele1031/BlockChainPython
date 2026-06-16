from Blockchain.block import Block

class Ledger:
    def __init__(self):
        self.blocks = []
        self.length = 0

    def add_block(self, infomation: str):
        if self.length == 0:
            self.blocks.append(Block(infomation, None))
        else:
            self.blocks.append(Block(infomation, self.blocks[-1].hash))
    
    def solve(self):
        pass

    def show(self):
        pass