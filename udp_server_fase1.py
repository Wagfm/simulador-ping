import socket

SERVER_IP_ADDRESS = ''
SERVER_PORT_NO = 8080
ADDR = (SERVER_IP_ADDRESS, SERVER_PORT_NO)
BUFFER_SIZE = 1024
ENCODING = 'utf-8'

udpServer = socket.socket(type=socket.AF_INET, family=socket.SOCK_DGRAM)
udpServer.bind(ADDR)
print('[START] Servidor inicializado...')

while True:
    msg, address = udpServer.recvfrom(BUFFER_SIZE)
    print(f'[{address[0]}]: {msg.decode(ENCODING)}')
    if msg.decode(ENCODING) == '!Encerrar':
        break
    udpServer.sendto(msg, address)

print(f'[END] Comunicação com [{address[0]}] encerrada!')
