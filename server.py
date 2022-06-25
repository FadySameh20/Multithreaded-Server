from email import message
from socket import *
import datetime
import threading
from urllib import response


def threadedServer(connectionSocket, addr):
    # while True:
    try:
        # getting header
        print(threading.active_count())
        message=b""
        while True:
            tempmessage = connectionSocket.recv(1024)
            message = message+tempmessage
            if not tempmessage or len(tempmessage) <1024:
                break
        # if not message:
        # break
        print(b"message:\n", message)
        #######Getting request type#######
        line = message.splitlines()[0]
        print(line.split()[0])
        request = line.split()[0]
        if request == b"GET":
            filename = message.split()[1]
            f = open(filename[1:],"rb")
            outputdata = f.read()
            print(outputdata)
            first_header = "HTTP/1.0 200 OK"
            header_info = {
                "Content-Length": len(outputdata),
                "Keep-Alive": "timeout=%d,max=%d" % (200, 200),
                "Connection": "Keep-Alive",
                "Content-Type": "text/html"
            }
            following_header = "\r\n".join("%s:%s" % (item, header_info[item]) for item in header_info)
            print("following_header:", following_header)
            responseMessage = "%s\r\n%s\r\n\r\n" % (first_header, following_header)
            # outputdata = responseMessage.encode() + outputdata + "\r\n".encode()
            outputdata = responseMessage.encode() + outputdata 

            connectionSocket.sendall(outputdata)
            print("sending")

        elif request == b"POST":
            final = message
            print(final)
            print("aho")
            print("lol")
            
            header = message.split(b"\r\n\r\n")[0]
            header=header+b"\r\n\r\n"
            outputdata = message.split(b"\r\n\r\n",1)[1]
            filename = header.split()[1].split(b"/")[1]
            print(filename)
            f = open(b"server_"+filename,"wb")
            f.write(outputdata)
            print(outputdata)
            connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n".encode())
            f.close()
    except IOError:
        print("exiting")
        connectionSocket.send("HTTP/1.0 404 Not Found\r\n\r\n".encode())


if __name__ == '__main__':
    # print('hi')
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Prepare a sever socket
    # Fill in start
    serverPort = 1234
    serverSocket.bind(('', serverPort))
    serverSocket.listen(5)
    threads = []
    # Fill in end
    while True:
        # Establish the connection
        print('\nReady to serve...')
        connectionSocket, addr = serverSocket.accept()
        # connectionSocket.settimeout(none)
        print("addr:\n", addr)
        # Fill in start
        # Fill in end
        client_thread = threading.Thread(target=threadedServer, args=(connectionSocket, addr))
        client_thread.daemon = True
        client_thread.start()
        threads.append(client_thread)

        print("Length", threading.active_count() - 1)
        # for t in threads:
        #     if not t.is_alive():
        #         threads.remove(t)
        # print("Lengthhhhh")
        # print(len(threads))
        # for thread in threads:
        #     thread.join()
        # threads.remove(client_thread)
        # client_thread

        # connectionSocket.close()

    # main thread wait all threads finish then close the connection
    """
    # for thread in threads:
    # 	thread.join()
    # If I put this, Chrome will not gonna work, safari will work.
    """
    serverSocket.close()


 # kill -9 $(ps -A | grep python | awk '{print $1}')
