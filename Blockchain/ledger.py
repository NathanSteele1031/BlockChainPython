import block

class Ledger:
    def __init__(self):
        self.blocks = []
        self.length = 0

    def add_block(self, infomation: str):
        if self.length == 0:
            self.blocks.append(block.Block(infomation, None))
        else:
            self.blocks.append(block.Block(infomation, self.blocks[-1].hash))
    
    def solve(self):
        pass

    def show(self):
        for selected_block in self.blocks:
            selected_block.show()