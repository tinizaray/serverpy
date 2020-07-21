import socket
import struct
import sys

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Crear el socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enlace a la dirección del servidor
sock.bind(server_address)

# Indique al sistema operativo que agregue el socket al grupo de multidifusión
# en todas las interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print('\nEsperando recibir mensages')
    data, address = sock.recvfrom(1024)

    print('Recibido %s bytes desde %s ' % (len(data), address))
    print(data)

    print('Enviando la contestación de lo recibido', address)
    sock.sendto('ack'.encode(), address)