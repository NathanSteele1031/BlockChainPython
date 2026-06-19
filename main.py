from Blockchain.block import Block
from Blockchain.ledger import Ledger
from P2P.p2p import ConnectionManager

def main():
    print("Loading ledger")
    ledger = Ledger()
    connection_manager = ConnectionManager()
    # Load the whole or part of the ledger here

    print("1.Mine on the blockchain\n2.Create a block")
    user_input = input(": ")
    if user_input == "1":
        # confirm the chain is up to date and start listening for new blocks and work on them.
        pass

    if user_input == "2":
        block_info = input("Type the data that will go into the blockchain: ")
        ledger.add_block(block_info)
        # Broadcast block through p2p connections

if __name__ == "__main__":
    main()