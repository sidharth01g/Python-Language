#!/usr/bin/python3
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
import socket
import time

no_of_tasks = 0


def get(url, port, path, selector):
    global no_of_tasks
    no_of_tasks += 1
    # Create socket
    socket_x = socket.socket()
    # Set non blocking socket
    socket_x.setblocking(False)
    host_tuple = (url, port)

    # Catch "BlockingIOError"
    try:
        socket_x.connect(host_tuple)
    except Exception as error:
        print("Caught %s: %s" % (type(error), str(error)))
        pass

    # Create a lambda for connected operations
    callback = lambda: do_connected_operations(socket_x, selector, request)

    # Wait for socket to be writeable
    selector.register(socket_x.fileno(), EVENT_WRITE, data=callback)
    selector.select()

    request = "GET %s HTTP/1.0\r\n\r\n" % path


def do_connected_operations(socket_x, selector, request):

    selector.unregister(socket_x.fileno())  # now socket_x is writeable
    # Prepare http get request
    request_encoded = request.encode()
    print("Sending: " + str(request_encoded))
    socket_x.send(request_encoded)

    # Receive chunksize
    chunksize = 1024
    chunks_list = []

    callback = lambda: do_readable_operations(selector, socket_x, chunks_list,
                                              chunksize)
    selector.register(socket_x.fileno(), EVENT_READ, data=callback)


def do_readable_operations(selector, socket_x, chunks_list, chunksize):
    global no_of_tasks
    selector.unregister(socket_x.fileno())
    chunk = socket_x.recv(chunksize)
    if chunk:
        chunks_list.append(chunk)
        callback = lambda: do_readable_operations(selector, socket_x,
                                                  chunks_list, chunksize)
        selector.register(socket_x.fileno(), EVENT_READ, data=callback)
    else:
        # join the chunks with empty bytes (b'')
        received_data = b''.join(chunks_list)
        received_data_decoded = received_data.decode()
        print("Received data:")
        print(received_data_decoded)
        no_of_tasks -= 1


selector = DefaultSelector()
start = time.time()
get("www.google.com", 80, "/", selector)
get("www.gmail.com", 80, "/", selector)

while(no_of_tasks):
    events = selector.select()
    print(dir(events))
    for event, mask in events:
        callback = event.data
        callback()

end = time.time()
print("Took %.1f seconds " % (end - start))
