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
