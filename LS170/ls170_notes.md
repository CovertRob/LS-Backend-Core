# Notes from Networking Foundations

## The Internet

- The internet is a vast network of networks. It is comprised of both the network infrastructure itself (devices, routers, switches, cables, etc) and the protocols that enable that infrastructure to function.

- Protocols are systems of rules. Network protocols are systems of rules governing the exchange or transmission of data over a network.

- Different types of protocol are concerned with different aspects of network communication. It can be useful to think of these different protocols as operating at particular 'layers' of the network.

- Encapsulation is a means by which protocols at different network layers can work together.

- Encapsulation is implemented through the use of Protocol Data Units (PDUs). The PDU of a protocol at one layer, becomes the data payload of the PDU of a protocol at a lower layer.

- The physical network is the tangible infrastructure that transmits the electrical signals, light, and radio waves which carry network communications.

- Latency is a measure of delay. It indicates the amount of time it takes for data to travel from one point to another.

- Bandwidth is a measure of capacity. It indicates the amount of data that can be transmitted in a set period of time.

- Ethernet is a set of standards and protocols that enables communication between devices on a local network.

- Ethernet uses a Protocol Data Unit called a Frame.

- Ethernet uses MAC addressing to identify devices connected to the local network.

- The Internet Protocol (IP) is the predominant protocol used for inter-network communication.

- There are two versions of IP currently in use: IPv4 and IPv6.

- The Internet Protocol uses a system of addressing (IP Addressing) to direct data between one device and another across networks.

- IP uses a Protocol Data Unit called a Packet.

## The Transport Layer

- Multiplexing and demultiplexing provide for the transmission of multiple signals over a single channel

- Multiplexing is enabled through the use of network ports

- Network sockets can be thought of as a combination of IP addresses and port number

- At the implementation level, network sockets can also be socket objects

- The underlying network is inherently unreliable. If we want reliable data transport we need to implement a system of rules to enable it

- TCP is a connection-oriented protocol. It establishes a connection using the Three-way handshake

- TCP provides relaibility through message acknowledgement and retransmission, and in-order delivery

- TCP also provides Flow Control and Congestion Avoidance

- The main downsides of TCP are the latency overhead of establishing a connection, and the poential Head-of-line blocking as a result of in-order delivery

- UDP is a very simple protocol compared to TCP. It provides multiplexing, but no reliability, no in-order delivery, and no congrestion or flow control.

- UDP is connectionless, and so doesn't need to establish a connection before it starts sending data

- Although it is unreliable, the advantage of UDP is speed and flexibility

## Intro to HTTP

- The Domain Name System (DNS) is a distributed database which maps a doman name such as `google.com` to an IP address such as `216.58.213.14`.

- A URI is an identifier for a particular resource within an information space

- A URL is a subset of a URI, but the two terms are often used interchangeably

- URL components include the scheme, host (or hostname), port, path, and query string

- Query strings are used to pass additinal data to the server during an HTTP request. They take the form of name/value pairs separated by an `=` sign. Multiple name/value pairs are separated by an `&` sign. The start of the query string is indicated by a `?`.

- URL encoding is a technique whereby certain characters in a URL are replaced with an ASCII code.

- URL encoding is used if a character has no corresponding character in the ASCII set, is unsafe because it is used for encoding other characters, or is reserved for a special use within the URL (like the characters mentioned above).

- A single HTTP message exchange consists of a Request and a Response. The exchange generally takes place between the Client and a Server. The client sends a request to the server and the server sends back a response.

- An HTTP request consists of a request line, headers, and an optional body.

- An HTTP response consists of a status line, optional headers, and an optional body.

- Status codes are part of the status line in a response. They indicate the status of the request. There are various categories of status code. 200 OK is the most frequent.

- HTTP is a stateless protocol. This means that each Request / Response cycle is independent of a Request and Responses that came before or those that come after.

- Statefulness can be simulated through techniques which use session IDs, cookies, and AJAX.

- HTTP is inherently unsecure. Security can be increased by using HTTPS, enforcing Same-origin policy, and using techniques to prevent Session Hijacking and Cross-site Scripting.

## Working with HTTP

- HTTP is a text-based protocol. HTTP Request and Responses involve sending text between the client and server

- In order for the protocol to work, the Request and Response must be structurd in such a way that both the client and the server can understand them

- With HTTP/1.1, the end of the headers is indicated by an empty line.

- The Content-Length header can be used to indicate the size of the body. This can help determine where the HTTP message should end.

## Transport Layer Security (TLS)

- HTTP Requests and Responses are transferred in plain text; as such they are essentially insecure

- We can use the Transport Layer Security (TLS) Protocol to add security to HTTP communications

- TLS encryption allows us to encode messages so that they can only be read by those with an authorized means of decoding the message

- TLS encryption uses a combination of Symmetric Key Encryption and Asymmetric Key Encryption. Encryption of the initial key exchange is performed asymmetrically, and subsuquent communications are symmetrically encrypted

- The TLS handshake is the process by which a client and a server exchange encryption keys

- The TLS handshake must be performed before security data exhange can begin; it involves several round-trips of latency and therefore has an impact on performance

- A cipher suite is the agreed set of algorithms used by the client and server during the secure message exchange

- TLS authentication is a means of verifying the identity of a participant in a message exhange

- TLS authentication is implemented through the use of Digital Certificates

- Certificates are signed by a Certificate Authority, and word on the basis of a Chain of Trust which leads to one of a small group of highly trusted Root CAs.

- The server's certificate is sent during the TLD handshake process

- TLS integrity provides a means of checkking whether a message has been altered or interfered with in transit

- TLS integrity is implemented through the use of a Message Authentication Code (MAC)\

## Evolution of Network Technologies

- HTTP has changed considerably over the years, and is continuing to change

- Many of the changes to HTTP are focused on imporving performance in response to the ever increasing demands of modern networked applications

- Latency has a big immpact on the performance of networked applications. As developers and software engineeers we need to be aware of this impact, and try to mitigate against it through the use of various optimizations

- In building networked applications, there are tools and techniques avaialble to us that work around or go beyond the limitations of basic HTTP request-response functionality

- For certain use cases a peer-to-peer architecture may be more appropriate than a client-server architecture

## Written Test Study Guide

### Internet

- Have a broad understanding of what the internet is and how it works
  1. What makes up the entirety of the internet put together?
  The internet, also called the world-wide web, is made up of a bunch of interconnected networks. These networks are able to talk to each other and share resources across eachother.
  2. What are the networks called that make up the internet?
  The networks that make up the internet are local area networks and inter-connected networks. Local area networks that talk to other local area networks are what combine to create the inter-connectedness that makes up what we know as the internet.
  3. What are the pieces of equipment that enable the network communication? At which part do they work in?
  The two primary pieces of equipment that enable network communcations are routers and switches. Switches primarly work within a local area network by directing network traffic to a specific device using a routing table which contains the MAC addresses of the devices in the LAN. A router on the other hand utilizes IP address ranges to direct traffic and is what enables LANs to talk to other LANs.
  4. In your own words, provide a definition for what protocols are. Why were they developed and still developed today?
  Protocols are an agreed upon standardization for the way in which to conduct a certain process. This could include data transfer between network or the encryption of that data. Protocols define how these processes are conducted and enable it to be reproduced across multiple different networks by multiple different machines and still be able to talk to each other. Protocols were developed to address specific problems with regards to the web and its communication needs. They are still developed today to continue iterating on the improvment of previous designs and to address new problems with the web as technology develops and new needs arise.
  5. What are some common protocols and the things they address for the internet?
  Some common protocols are as follows: Ethernet, HTTP, TCP, UDP, TLS, IP
  6. What aspects of communication do protocols address and how does this lead to protocol grouping?
  Different types of protocols address different aspects of how networks communicate with each other. These lead us into groupings where certain protocols deal with syntactical rules and govern structure of messages and others deal with the flow and order of messages, aka message transfer rules. TCP and UDP address the flow and order but in different ways. HTTP defines the structure of said messages. You add a combination of these protocols up to create an overall network communication system. Which ones you choose is up to the programmer based on what kind of system you are making.
  7. What are the layers of the OSI model?
  The Open Systems Interconnection model from top to bottom are as follows: (7 in total)
  - Application
  - Presentation
  - Session
  - Transport
  - Network
  - Data Link
  - Physical
  8. What are the layers of the TCP/IP model?
  - Application
  - Transport
  - Internet
  - Link
  9. How do OSI/TCPIP models differ from each other in how they approach defining the internets layers?
  The TCP/IP suite divides the layers by the scope of communcations within each layer. At the top is the application within a local area network, as it expands out to other networks is where the transport, internet, and link come into play. The OSI model divides the layers in terms of function that each layer provides for LANs and the internet as a whole. Putting multiple OSI models together is what makes up the internet.
  10. How do the two models relate to eachother?
  The TCP/IP application layer mostly maps to the top three layers of the OSI model: application, presentation, and session. The TCP/IP transport layer mostly maps to the fourth OSI layer, transport. The second TCP/IP layer, internet, mostly maps to the third layer of the OSI model, network. The first layer of TCP/IP, link, maps to the bottom two OSI layers, data link and physical.
  10. What are the components of a PDU? How does a PDU fit into the previously mentioned models?
  A protocol data unit is an amount or block of data transferred over a network. Each protocl has a different anme for its PDUs. However, the idea of encapsulation remains the same across all PDUs. The data from one layer is encapsulated within a data unit of the layer below it. The basic concept of each PDU consists of a header, a data payload (the layer above), and in some cases a trailer or footer which contain meta data specific to that protocols PDU. For example: *(Ethernet Frame ( IP Packet ( TCP segment (HTTP R/R))))*. This break down of encapsulating PDU's allows us to remain a high level of abstraction at the application level of the models where many various protocols are used depending on our system design.
  11. Describe both models in full detail with the protcols that belong in each layer.
  The OSI model:
    7. Application: high level resource sharing protocols - HTTP, FTP, SMTP
    6. Presentation: translation of data between networking service and an application, character encoding, data compression, encryption/decryption - *format of data, TLS is encapsulated by TCP*
    5. Session: managing communication sessions, back and forth transmissions between nodes - *User authentication and connection, a session connection is separate from the transport connection, a session can have multiple transport connections and transport connections can be reused after a session close*
    4. Transport (Segment/Datagram): reliable data transmission of data segments - *TCP/UDP*
    3. Network (Packet): Structuring and managing multi-node network, addressing, routing, and traffic control - *Internet Protocol*
    2. Data Link (Frame): Transmission of data frames between two nodes connected by physical layer - *Ethernet protocol*
    1. Physical (Bit, signal): Transmission and reception of raw bit streams over a physical medium - *Electricity, light, RF*
  
  The TCP/IP model:
    4. Application: HTTP, FPT, SMTP, TLS handshake takes place after the TCP handshake
    3. Transport:TCP/UDP
    2. Internet: Internet protocol
    1. Link: Ethernet, MAC addressing

- Understand the characteristics of the physical network, such as latency and bandwidth
  1. Define latency in your own words
  Latency is how long it takes a piece of data to be transmitted from one point to another point. It also includes the processing time at all the intermediate hops along the way from the start point to the end point. 
  2. Define bandwidth in your own words
  Bandwidth is the amount of data that can be transmitted along the network without having reliability and transmission issues causes by issues such as bottlenecking. Bandwidth is constrained by both transmission protocols and the physical implementation of the network. It also varies across various points of the network.
  3. What are the different mediums at the physical layer for transporting information and what do they transport?
  The information is transmitted as bits, which is binary data. This transmission is carried by signals in the form of electrical signals, light signals, or radio waves. This is generally coax cables, fiber optic cables, and Wi-Fi.
  4. What are the different elements of latency?
  The different elements of latency are propagation delay, transmission delay, processing delay, and queing delay. Propagation delay is a function of distance and speed for the amount of time it takes the signal to travel from sender to receiver. Transmission delay involves all of the various hops on the various wires, cables, switches, routers etc that the signal travels between from sender to final receiver. All these things add up to a transmission delay. Processing delay is the time it takes to translate the data between different elements at each stage of its transmission. Queuing delay is the time a device buffers incoming data when there is too much data at once. This is synonomous to traffic on a road. Add all of these up and you get latency.
  5. How do network hops fit into the elements of latency?
  Network hops are the various nodes of the network path that the data needs to take to get from the sender to the receiver its being directed to. The amount of hops will widely vary.
  6. How does bandwidth vary across a physical network?
  Bandwidth at the core of a network, such as in a data center server, will be very different than at the edge of the network, such as in a home office network.

- Have a basic understanding of how lower level protocols operate
  1. What layers are responsible for lower level protcols?
  The OSI model places lower level protocols in layer 2, the data link layer. In the TCP/IP model, lower level protcols take place in layer 1, the link layer. These layers govern identifying the device on the network to send data to and moving that data to it.
  2. What does an ethernet PDU accomplish?
  An ethernet protocol data unit is the frame. It encapsulates data from the network/internet layers which are internet protocol packets. The ethernet protocol is the last, or lowest, protocol at which encapsulation takes place. The ethernet frame adds logical structure to the binary data being transmitted so that it can be understood on both ends.
  3. What are the three most important parts of an ethernet frame?
  An ethernet frame structures the binary data by using various fields of data that are specific length bytes and appear in a set order. The key fields are the Source and Destination MAC address and the data payload. 
  4. What allows us to accomplish device addressing within a network? What is another name for this?
  A common way we accomplish device addressing within a network is by having all devices with a network identification card assigned a permanent Media Access Control address. This address is a physical address assigned to the devices network card and allows switches to identify devices on the network.
  5. How does a hub and a switch utilize MAC address differently?
  A hub sends data received to every device on the network that is connected to it. Each receiving device would check if its MAC address matches the destination MAC address in the ethernet frame to see if it is the intended recipient. Switches however, use a routing table with ethernet port numbers assigned to specific device MAC addresses. The switch checks the destination address for us and forwards it to the correct receipient based on said table.
  6. Why does using MAC addresses not scale well? Are they physical or logical? Flat or hierarchical?
  MAC addressing does not scale well past a local are network level because it is not feasibly to have a database with all the MAC addresses everywhere. Also, since the addresses stay with their physical device, it would be near impossible to track when they move networks, such as laptops. MAC addresses are not logical in nature. They do not follow a pattern that can be broken down into sub-components. This makes them flat and not hierarchical in nature like IP addresses in the Internet protocol are.

- Know what an IP address is and what a port number is
  1. What layer do IP addresses belong in for both models? What does this enable for the internet?
  In the OSI model, IP addresses belong to the Internet protocol which is a part of the network layer. In the TCP/IP model, they belong in the internet layer. The internet protocol and IP addresses enables the internet to easily direct traffic based on the hierarchical set of rules that IP addresses follow. They are also logical in nature, meaning they are not tied to specific devices. This allows networks to assign IP addresses as devices join a network.
  2. What are the two primary features of the internet protocol?
  The two primary features are routing capability via IP addressing and encapsulation of data into packets. The modularity that IP addressing provides through creating logical subnetworks makes it very powerful and easy to route data.
  3. What makes up the protocol data unit of the IP protocol?
  The PDU for the internet protocl is the packet.A packet is comprised of a data payload and various headers. The headers are split into logical fields determined by set size and order within the packet. Some of the headers include Version, source address, and destination address.
  4. What is usually the data payload of an IP packet?
  The data payload of an IP packet is from the transport layers in both models which consists of either a TCP segment or UDP datagram.
  5. Describe what it means for IP addresses to be logical in nature. How does hierarchy work? Subnetting?
  The idea that IP addresses are logical in nature means that they are abstracted away from the physical hardware. IP addresses can be changed or reassigned based on network configurations and protocols. The idea of hierarchy is where a network is split into logical subnetworks where each have their own range of IP addresses that devices are allowed to be assigned if they try to join that specific subnetwork. The hierarchical nature is split into two parts, the network and host portion of the IP address.
  6. What is the difference between IPV4 and IPV6? 
  IPV4 addresses are 32 bits in length divided into four sections of eight bits. This allows for a range of numbers from 0 to 255. IPV6 on the other hand utilizes 128 bit length that are separated into 8 16-bit hexadecimals. This expansion allows for a lot more address space.
  7. What is a port and what are some common example ranges?
  A port is used on a network device to identify a process (application) that is running on a host. A common example is a web browser which by default runs on port 80, which is the port that HTTP requests are communicated through. 0-1023 are the ranges for well known ports such as HTTP, FPT, SMTP etc.
  8. What is a communication end point? Another name for this?
  A communication endpoint can be thought of as the combination of an IP address and the port number for a process. This communication endpoint is commonly refered to as a socket. The format for this endpoint follows the format: `XXX.XXX.XXX.XXX:Port`
  9. Talk about the importance of sockets and their involvement in the different kinds of communication.
  In general, a socket is a mechanism for communication between both local processes and networked processes. How these sockets are implemented on a code level is what determines their involvement in the communication of said network devices. Sockets can be treated as objects and are what allow us to create the kind of communcation styled system we want. Whether that is connection orientd or connectionless is up to our implementation.
  10. What is multiplexing and demultiplexing?
  Multiplexing is the idea of transmitting multiple signals over a single channel. Demultiplexing is the reverse process where the multiple signals are decoded on the receiving side. At the transport layer of our models the protocols there utilize assigned ports to accomplish this. This takes place on both the client and server sides.

- Have an understanding of how DNS works
  1. What is the purpose of the Domain Name System? What is it?
  The domain name system (DNS) is a distributed database across the world-wide web that allows users to access websites by their domain name instead of their IP address. The DNS maps the domain name to its IP address, encapsulating it so that it is more user friendly for users to type in a name of a website instead of IP addresses. 
  2. Describe the request response cycle with regards to a DNS request. How does the hierarchy work?
  A user first types in a domain name in their web browser. When they hit enter to go to the website, the browser first checks if the domain is in its cache of domains on device. If it is not, it then reaches out to the DNS. The DNS follows a hierarchy where not all IP addresses are contained in one database. If one DNS datbase does not contain the mapping that we are looking for, the request is forwarded to the next DNS database. Once the request reaches the server that contains the information we are looking for, it returns a response with that domains IP address for our web browser to make the connection.

- Understand the client-server model of web interactions, and the role of HTTP as a protocol within that model
    1. What protocol enables the web and its various applications to interact with eachother?
    The Hyper Text Transfer Protocol (HTTP) enables web applications to interact with each other. This protocol enables clients to make requests to servers, and those servers to then issue responses back with the requested information to be rendered by the browser.
    2. What layer does HTTP belong to? What markup language does HTTP primarily interact with?
    HTTP belongs in the application layer in both the web models. It is the transfer protocol for Hypertext Markup Language (HTML) and its various other elements that aid in rendering a put together web page.
    3. Describe how the client-server model interation works with regards to HTTP and accessing resources. How is state involved? What application element usually serves as the client? How is the server found for the client?
    The client-server model of web interaction is what defines the two sides that make up the wordl-wide web. On the client side you have a user interacting with a machine which contains various running applications. Each time these applications need to get resources from the internet to build what the user is asking for, such as images, videos, web pages, and various files, it reaches out to a server. Servers are a specialized computer that retrieve and send back the resources the user's applications are asking for. HTTP is the protocol with which the web browser makes these requests to the server and is also how the server sends its response and resources back to the user's application. This client-server interaction is also stateless. Meaning that each HTTP request/response pair is completely independent.

### TCP & UDP

- Have a clear understanding of the TCP and UDP protocols, their similarities and differences
    1. What are the key characteristics of TCP? Mention reliability, data recovery, data abstraction and encapsulation, performance, connection type
    The key characteristics of the Transport Control Protocol (TCP) are to provide a means to reliably transport data over an inherently unreliable connection. The protocol is an abstraction of reliable network communication on top of an unreliable channel. TCP allows for reliability through the re-transmission of lost or corrupted data through its connection oriented transmission protocol. This abstraction of the underlying channel is what ensures applications are guranteed reliable data. However, this amount of complexity can lead to performance issues since it can involve multiple RTT's and repeat transmissions and processing.
    2. What are TCP segments? What is contained within their data payload?
    The abstraction created by TCP in which its characteristics are implemented through is known as a TCP segment. In the context of the web and a web browser, a TCP segment's data payload would be an HTTP request. Other fields include source and destination port headers. For implementing reliability important headers are the checksum and sequence number.
    3. Describe the 3 most important header fields in a TCP segment.
    For reliability purposes these are the checksum, sequence number, and acknowledgement number. Checksum provides a means for the receiver to perform error detection. The sequence number and acknowledgement number allows for in-order delivery, handling data loss and duplication.
    4. Discuss latency and head-of-line blocking. How do TCP and UDP handle these differently?
    Due to the intensive overhead in establishing and maintaining the TCP connection inherent with the three-way handshake it implements, latency can become an issue. The various characteristics it implements for reliable data transfer also contribute to its latency causing. A major one is head-of-line blocking. TCP messages have a sequence number that enable in-order message delivery. If a segment is lost or corrupted and needs to be re-transmitted, this can block the rest of the line of data from being processed. It tries to prevent this trhough various congestion avoidance feedback mechanisms.
    5. What is the PDU for UDP?
    The PDU for the User Datagram Protocol is called a datagram. The header has four fields: Source Port, Destination port, UDP length, and a checksum field. The UDP datagram is extremely simple by design.
    6. Describe UDP connection type and describe it by what it doesn't do.
    The UDP connection is a connectionless oriented one. It does not guarantee message delivery or delivery order, provides no built-in congestion avoidance or flow-control, and has no connection state tracking. 
    7. How does UDP relate to all the charcteristics of TCP in the first question?
    UDP provides multiplexing on the same channel using port numbers in the same way that TCP does. It also provides a checksum for error detection similar to how TCP does. However, UDP has no other built-in methods for reliability, error detection, or data recovery. It uses the same idea of abstracting the data transmission ontop of an unreliable channel, but UDPs abstraction is built more for performance and latency prevention in mind. It encapsulates the same kind of data from the layer above, but it does so in a connectionless manner.
    8. Describe the idea of using UDP as a template to build upon.
    Due to the way in which the UDP transmission abstraction is implemented, or rather the lack of implementation in comparision to TCP, it is a prime choice for developers that want to build specific protocol characteristics on top of it for their specific application and its needs. Use cases for this are applications that need to prioritize low latency and do not have data loss prevention as their primary concern.
- Have a broad understanding of the three-way handshake and its purpose
    1. What does the three-way handshake relate to in regards to connection type?
    The three way handshake is the implementation of a connection oriented protocol. 
    2. What flags play a role in the handshake?
    The flags that are used in the handshake are the `SYN` and `ACK` flags. Note that this is different than the four-way handshake that takes place for terminating connections.
    3. Provide an overview of the three-way handshake using a client-server interaction model
    In the three-way handshake you have a sender and a receiver. The client is the sender and the server is the receiver. The client sends a TCP segment with the `SYN` flag set to 1, upon receiving it, the server sends back a `SYN ACK` message, which is a TCP segment with the `SYN` and `ACK` flags both set to 1. Once the client receives the sever's `SYN ACK` message, the client sends another `ACK` segment to the server. Once the client sends the last `ACK` message, it can start sending data because this last TCP segment is used to synchronize the segments.
    4. Does UDP have a handshake? Why not?
    UDP does not have a handshake. Applications using UDP can start sending data without waiting for a connection to be established with the server.

- Have a broad understanding of flow control and congestion avoidance
    1. Why are flow control and congestion avoidance major topics with regards to TCP?
    Flow control is the means by which the TCP protocol prevents the sender from overwhelming the receiver with too much data at once. This data flow amount is modulated by the WINDOW field of the TCP segment header. This is different than congestion avoidnce, which is a limitation of the physical underlying network to process and transmit data. Data loss can happen when at a network hop the router's buffer is full and data packets are dropped. TCP uses this data loss as a feedback mechanism to avoid congestion and reduce/increase transmission window limits as needed.
    2. Is this implementd in UDP?
    Flow control and congestion avoidance are not native to the base UDP protocol. However, it is choice that a developer can make to implement.

### URLs

- Be able to identify the components of a URL, including query strings
    1. Provide an example of a URL and describe each of the 2 required components. What are the other 3 optional component?
    2. What is the default port used for normal HTTP requests?
    3. Provide a query string example consisting of 3 different parts. What characters are special in a URL?
    4. What type of HTTP requests most commonly use query strings?
    5. What are the limitations to query strings?
    6. What is URL encoding and what are the cases requring its use?
- Be able to construct a valid URL
- Have an understanding of what URL encoding is and when it might be used

### HTTP and the Request/Response Cycle

- Be able to explain what HTTP requests and responses are, and identify the components of each
  1. What is an HTTP method?
  2. What are the most common HTTP methods?
  3. What is an HTTP GET request used for and what is an HTTP POST request used for?
  4. How do headers apply to requests and responses?
  5. What does a request consist of?
  6. What does a response consist of?
  7. What are some common request headers?
  8. What are some common response headers?

- Be able to describe the HTTP request/response cycle
  1. Describe the HTTP request/response cycle with the following steps: client, server process, server send, client process

- Be able to explain what status codes are, and provide examples of different status code types
  1. What is a status code in regards to a response?
  2. What are the most common codes and their meaning?
- Understand what is meant by 'state' in the context of the web, and be able to explain some techniques that are used to simulate state
  1. What is state and what makes the web stateless? Think HTTP and the server.
  2. What are the three primary approaches to emulate statefullness?
  3. How is a session identifier used to emulate state?
  4. Where do cookies belong in regards to managing state and session? Are they included in the request response cycle?
  5. What does AJAX stand for? What does it enable? How are callbacks involved?
- Explain the difference between `GET` and `POST`, and know when to choose each
  1. Provide three examples of each and when you would use them.
- Have a basic understanding of the asynchronous nature of AJAX, and the kinds of features that it enables for web apps
  1. How does AJAX slightly alter the request response cycle that you see?

### Security

- Have an understanding of the various security risks that can affect HTTP, and be able to outline measures that can be used to mitigate against these risks
  1. Why is HTTP inherintly unsecure? What is packet sniffing? What can hackers use to identify you?
  2. What cryptographic protocol does HTTPS use? What about certificates?
  3. What is the definition of origin in context of same-origin policy? What does this policy restrict?
  4. What is CORS? How does it guard against session hi-jacking? Other ways to prevent session hi-jacking?
  5. What are the concerns of cross-site scripting? Methods for preventing it? What is escaping?
- Be aware of the different services that TLS can provide, and have a broad understanding of each of those services
  1. What are the three services that TLS provides and their definitions?
  2. What is symmetric and asymmetric key encryption? How are each used in the TLS handshake?
  3. What are the 4 steps to the TLS handshake?
  4. What is a cipher suite?
  5. How are certificates and public keys utilized in the handshake?
  6. Describe what certificate authorities are and the chain of trust
  7. What layer does TLS operate in with regards to HTTP and TCP/UDP?
  8. What is a MAC? What is it used for? What is it similar to in other PDUs? What does it accomplish for integrity?


### Questions

1. Where does TLS belong in the model architecture?
2. Transmission delay vs processing delay? Basically the same thing?
3. 
