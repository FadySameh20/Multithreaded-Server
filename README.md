# Multithreaded-Server
Applying socket programming and multi-threading/multi-processing techniques to make a multi-threaded server with some features such as: persistent connections, pipelining, HTTP 1.1 protocol with timeout and caching.

Procedures:
1. Client's requests are included in the input file 'input.txt'.
2. The program parses the client's requests and processes them in a pipelined manner.
3. The program checks if the request is already cached or not. If it is in cache then return the requested item directly, otherwise, contact the server.
4. If timeout occurs, connection will close.
