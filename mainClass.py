#
#   Server
#

import socket,sys,os

def binario_a_decimal(numeromagicoBin):
    numero_binario = invertirCadena(numeromagicoBin)
    numero_decimal = 0
    for posicion, digito_string in enumerate(numero_binario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion
    return numero_decimal

def invertirCadena(cadena):
    cadenaInvertida = cadena[::-1]
    return cadenaInvertida


os.system("cls")
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

numeromagicoBin = ""

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data == b"isconected":
        mensaje = b"conected"
        sent = sock.sendto(mensaje, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
    elif data == b'dato1':
        numeromagicoBin += '1'
        mensaje = b"saved"
        sent = sock.sendto(mensaje, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
        print(numeromagicoBin)
    elif data == b'dato0':
        numeromagicoBin += '0'
        mensaje = b"saved"
        sent = sock.sendto(mensaje, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
        print(numeromagicoBin)
    elif data == b'pleaseSendTheNumber':
        print(binario_a_decimal(numeromagicoBin))
        mensaje = str(binario_a_decimal(numeromagicoBin))
        print(type(mensaje))
        sent = sock.sendto(mensaje.encode(), address)
        print('sent {} bytes back to {}'.format(
            sent, address))
        numeromagicoBin = ''
    elif data == b'close':
        print('No hay clientes conectados')
        print('Cerrando servidor')
        break
    