import socket

class ConnectionManager:
    def __init__(self):
        self.peer_connections = []
        self.service_node_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def get_active_peers(self):
        service_node = "127.0.0.1"
        service_port = "6000"