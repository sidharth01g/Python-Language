#!/usr/bin/python3
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
import time


def get(url, port, path, selector=None):
    # Create socket
    socket_x = socket.socket()
    # Set non blocking socket
    if selector:
        socket_x.setblocking(False)
    host_tuple = (url, port)

    # Catch "BlockingIOError"
    try:
        socket_x.connect(host_tuple)
    except Exception as error:
        print("Caught %s: %s" % (type(error), str(error)))
        pass

    if selector:
        # Wait for socket to be writeable
        selector.register(socket_x.fileno(), EVENT_WRITE)
        selector.select()
        selector.unregister(socket_x.fileno())  # now socket_x is writeable

    # Prepare http get request
    request = "GET %s HTTP/1.0\r\n\r\n" % path
    request_encoded = request.encode()
    print("Sending: " + str(request_encoded))
    socket_x.send(request_encoded)

    # Receive chunksize
    chunksize = 1024
    chunks_list = []
    while True:

        if selector:
            # Wait for socket to be readable
            selector.register(socket_x.fileno(), EVENT_READ)
            selector.select()
            selector.unregister(socket_x.fileno())

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


selector = DefaultSelector()
start = time.time()
get("www.google.com", 80, "/", selector)
get("www.gmail.com", 80, "/", selector)
end = time.time()
print("Took %.1f seconds " % (end - start))
