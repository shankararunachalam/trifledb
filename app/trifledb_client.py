import socket

class TrifleDBClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        return

    def connect(self):
        conn = socket.socket()
        try:
            conn.connect((self.ip, self.port))
        except socket.error as e:
            print(str(e))
        return conn

    def get(self, key):
        conn = self.connect()
        command = "get " + key
        conn.sendall(command.encode())
        response = conn.recv(1024)
        conn.close()
        return response.decode()
    
    def put(self, key, value):
        conn = self.connect()
        command = "put " + key + " " + value
        conn.sendall(command.encode())
        response = conn.recv(1024)
        conn.close()
        return response.decode()
