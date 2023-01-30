# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    con, _ = server_socket.accept() # wait for client

    while True:
        _ = con.recv(1024)
        con.send(bytes('+PONG\r\n', 'utf-8'))

        # con.send(bytes("+OK\r\n", 'utf-8'))
        # server_socket.close()


if __name__ == "__main__":
    main()
