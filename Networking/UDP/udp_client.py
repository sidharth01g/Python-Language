import socket


def main():
    # Client IP and port
    # Note: In this experiment, the server and client programs are running on
    # the localhost, i.e. 127.0.0.1
    client_host = "127.0.0.1"
    client_port = 5001
    client_tuple = (client_host, client_port)

    # Server
    server_host = "127.0.0.1"
    server_port = 5000
    server_tuple = (server_host, server_port)

    # Create socket object
    socket_x = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind socket to client port
    socket_x.bind(client_tuple)

    message = None

    while(message != 'q'):
        # Get user input and send message to server
        message = raw_input("Message: ")
        socket_x.sendto(message, server_tuple)

        # Receive data from server
        receive_buffer_size = 1024  # bytes
        received_data, server_address = socket_x.recvfrom(receive_buffer_size)
        print("Received from {}:\n{}".format(
            str(server_address), str(received_data)))

    # Close socket
    socket_x.close()


if __name__ == "__main__":
    main()
