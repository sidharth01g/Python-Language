import socket


def main():
    # Set server host IP address and port
    host = "127.0.0.1"
    port = 5000

    # Create a socket object
    server_socket = socket.socket()

    # Bind the socket to the port on the IP address
    host_port_tuple = (host, port)
    server_socket.bind(host_port_tuple)

    # No. of conections to listen to at a time
    n = 5
    server_socket.listen(n)

    # Accept an incoming connection from a client, get the connection object
    # and client address
    connection_object, client_address = server_socket.accept()
    print("Connection: ", connection_object)
    print("Client address: ", client_address)

    # Keep receiving
    while True:
        # Receive buffer size in bytes
        receive_buffer_size = 1024
        received_data = connection_object.recv(receive_buffer_size)
        print("Received data: ", received_data)

        # End reception if client closes connection
        if not received_data:
            break

        # Reverse the received data and send it back
        data_reversed = str(received_data)[::-1]

        # TCP is connected throughout the client-server interaction
        # No need to specify "sendto" address as in UDP
        connection_object.send(data_reversed)

    # Close connection
    connection_object.close()


if __name__ == "__main__":
    main()
