import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    request_line = client_socket.recv(1024).decode()
    if (not request_line) or ('favicon.ico' in request_line):
        client_socket.close()
        continue

    path_and_params = request_line.splitlines()[0]

    http_method = path_and_params[:3]
    query_string_start = path_and_params.find('?')
    path = path_and_params[4:query_string_start]
    query_string = path_and_params.split()[1].lstrip("/?").split('&')
    query_params = {}
    for param in query_string:
        key, value = param.split('=')
        query_params[key] = value
    
    rolls = [random.randint(1, int(query_params['sides'])) for roll in range(int(query_params['rolls']))]

    response = ("HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html\r\n"
            "\r\n"
            "<html><head><title>Dice Rolls</title></head><body>"
            f"<h1>HTTP Request Information:</h1>"
            f"<p><strong>Request Line:</strong> {path_and_params}</p>"
            f"<p><strong>HTTP Method:</strong> {http_method}</p>"
            f"<p><strong>Path:</strong> {path}</p>"
            f"<p><strong>Parameters:</strong> {query_params}</p>"
            "<h2>Rolls:</h2>"
            "<ul>")

    for num in rolls:
        response += f"<li>Roll: {num}</li>"
    response += "</ul></body></html>"

    client_socket.sendall(response.encode())
    client_socket.close()


# Your next task is to:

# Parse the string GET /?rolls=2&sides=6 HTTP/1.1 into several variables:

# http_method with a value 'GET'
# path with a value '/'
# params should be a dictionary with the rolls and sides properties and the appropriate values {'rolls': '2', sides: '6'}`. Notice that the values are strings. This is typical for web applications.
# Roll as many dice as specified in the query parameters, with the value of each die specified by the sides parameter. Print them consecutively.

# You may assume that the a properly formatted query string is always present in the URL.