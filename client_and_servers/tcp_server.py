import socket
            # 0.0.0.0 - any network interface
HOST, PORT = "0.0.0.0", 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv: # endpoint - server. The with .. as closes auto when the block ends, even when error accures
	srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # restarts the server right away on the same port - without it could result in Address already in use
	srv.bind((HOST, PORT)) # attach to the given address and port
	srv.listen() # ready to accept incoming connections - the OS queues clients that try to connect
	print(f"listening on {HOST}:{PORT}")
	while True: 
		conn, addr = srv.accept() # conn: a new socked used to talk to the client. addr: the clients (ip, port)
		with conn:
			print("connected:", addr)
			while data := conn.recv(1024): # b"" = closed , the walrus operator assigns the result of conn.recv(1024) to the data
				conn.sendall(data) # sendall keeps sending until every byte is sent, (a plain "send" might send only part of it)
			print("closed:", addr) 

