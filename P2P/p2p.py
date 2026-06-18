import socket, json

class ConnectionManager:
    def __init__(self):
        # The first connection is the service node always
        self.peer_connections = []
        self.service_node_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def get_active_peers(self):
        service_node = "127.0.0.1"
        service_port = "6000"
        self.service_node_connection.connect((service_node, service_port))
        self.peer_connections.append(self.service_node_connection)
        self.service_node_connection.sendall("GET peer")

        # Will get json structure of all service nodes.
        peer_data_json = self.service_node_connection.recv(1024)
        while peer_data_json[-3:] != "~~~": # This will be the ending string of the transmisson
            peer_data_json += self.service_node_connection.recv(1024)
        peer_data_json = peer_data_json[:-3] # Strips the ~~~ tag
        peer_data = json.load(peer_data_json)
        """
        How the peer data should be structured
        {
        "peers" : [*peer ip addresses*],
        "connections : *number*
        }
        """
        # Creates active connections of all ip addresses and add them to the list
        for ip_address in peer_data["peers"]:
            new_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_connection.connect((ip_address, 6001))