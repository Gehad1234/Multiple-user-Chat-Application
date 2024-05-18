import tkinter as tk
import socket
import threading

def start_server():
    global server_socket
    global server_running
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 59000))
    server_socket.listen(5)
    server_running = True
    while server_running:
        client_socket, client_address = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
                broadcast(message)
        except:
            break

def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

def stop_server():
    global server_running
    server_running = False
    server_socket.close()

clients = []

def server_gui():
    root = tk.Tk()
    root.title("Chat Server")

    start_button = tk.Button(root, text="Start Server", command=start_server)
    start_button.pack()

    stop_button = tk.Button(root, text="Stop Server", command=stop_server)
    stop_button.pack()

    root.mainloop()

server_gui()
