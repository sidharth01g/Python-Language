import socket


def main():

    # Set server a host address and port
    host = "127.0.0.1"
    port = 5000

    # Create socket object
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind socket object to port
    host_port_tuple = (host, port)
    socket_obj.bind(host_port_tuple)

    print("Server started")

    while True:
        receive_buffer_size = 1024  # bytes

        # Receive data, client address
        received_data, client_address = socket_obj.recvfrom(receive_buffer_size)
        print("Message from {}:\n{}".format(
            str(client_address), str(received_data)))

        data_reversed = str(received_data)[::-1]
        # UDP is connectionless. Need to specify "sendto" address
        print("Sending {} to {}".format(
            str(data_reversed), str(client_address)))
        socket_obj.sendto(data_reversed, client_address)

    socket_obj,close()


if __name__ == "__main__":
    main()
