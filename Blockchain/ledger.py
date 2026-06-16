import block

class Ledger:
    def __init__(self):
        self.blocks = []
        self.length = 0

    def add_block(self, infomation: str):
        if self.length == 0:
            self.blocks.append(block.Block(infomation, None))
            self.length += 1
        else:
            self.blocks.append(block.Block(infomation, self.blocks[-1].hash))
            self.length += 1
    
    def solve(self):
        solve_key = 0
        while not self.blocks[-1].test_key(solve_key):
            solve_key += 1
        print("Sovled")

    def show(self):
        for selected_block in self.blocks:
            selected_block.show()