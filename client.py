import tkinter as tk
import socket
import threading

def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            message_display.insert(tk.END, message + '\n')
        except:
            break

def send():
    message = alias.get() + ": " + message_entry.get()
    message_display.insert(tk.END, message + '\n')
    client_socket.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)

def connect_to_server():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 59000))
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

def client_gui():
    root = tk.Tk()
    root.title("Chat Client")

    message_display = tk.Text(root, height=20, width=50)
    message_display.pack()

    message_entry = tk.Entry(root, width=40)
    message_entry.pack()

    send_button = tk.Button(root, text="Send", command=send)
    send_button.pack()

    alias_label = tk.Label(root, text="Alias:")
    alias_label.pack()

    global alias
    alias = tk.Entry(root, width=20)
    alias.pack()

    connect_to_server()

    root.mainloop()

client_gui()
