import socket


def main():

    # Host IP address and port of the server to connect to
    server_host = "127.0.0.1"
    server_port = 5000

    # Create a socket
    server_socket = socket.socket()
    connect_tuple = (server_host, server_port)

    # Connect to server
    server_socket.connect(connect_tuple)

    message = None
    # Quit on 'q'
    while message != 'q':
        # Get user input message
        message = raw_input("Message: ")

        # Send message
        server_socket.send(message)

        # Set receive buffer size
        receive_buffer_size = 1024  # bytes
        received_data = server_socket.recv(receive_buffer_size)
        print("Received from server: ", received_data)

    server_socket.close()


if __name__ == "__main__":
    main()
