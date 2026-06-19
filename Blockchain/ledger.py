import block

class Ledger:
    def __init__(self):
        """
        A class that stores Block instances and allows adding, solving, and showing blocks.
        """
        self.blocks = []
        self.length = 0

    def add_block(self, infomation: str):
        """
        Creates a block then appends it to the blocks instance variable along with adding passed information into the newly created block instance. 
        """
        if self.length == 0:
            self.blocks.append(block.Block(infomation, None))
            self.length += 1
        else:
            self.blocks.append(block.Block(infomation, self.blocks[-1].hash))
            self.length += 1
    
    def solve(self):
        """
        Takes the last block that has been added and attempts to solve the hash for it.
        """
        solve_key = 0
        while not self.blocks[-1].test_key(solve_key):
            solve_key += 1
        print("Sovled")

    def show(self):
        """
        Takes all the blocks in the instance and calls the show function of each block instanced stored. 
        """
        for selected_block in self.blocks:
            selected_block.show()