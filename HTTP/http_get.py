import socket


def get(url, port, path):
    # Create socket
    socket_x = socket.socket()
    host_tuple = (url, port)
    # Connect
    socket_x.connect(host_tuple)

    # Prepare http get request
    request = "GET %s HTTP/1.0\r\n\r\n" % path
    request_encoded = request.encode()
    print("Sending: " + str(request_encoded))
    socket_x.send(request_encoded)

    # Receive chunksize
    chunksize = 1024
    chunks_list = []
    while True:
        chunk = socket_x.recv(chunksize)
        if chunk:
            chunks_list.append(chunk)
        else:
            # join the chunks with empty bytes (b'')
            received_data = b''.join(chunks_list)
            received_data_decoded = received_data.decode()
            print("Received data:")
            print(received_data_decoded)
            break
    socket_x.close()


get("www.google.com", 80, "/")
get("www.facebook.com", 80, "/")
