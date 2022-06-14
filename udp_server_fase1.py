import socket

SERVER_IP_ADRESS = ''
SERVER_PORT_NO = 8080
ADDR = (SERVER_IP_ADRESS, SERVER_PORT_NO)
BUFFER_SIZE = 1024
ENCODING = 'utf-8'

udpServer = socket.socket(type=socket.AF_INET, family=socket.SOCK_DGRAM)
udpServer.bind(ADDR)
print('[START] Servidor inicializado...')

while True:
    msg, adress = udpServer.recvfrom(BUFFER_SIZE)
    print(f'[{adress[0]}]: {msg.decode(ENCODING)}')
    if msg.decode(ENCODING) == '!Encerrar':
        break
    udpServer.sendto(msg, adress)

print(f'[END] Comunicação com [{adress[0]}] encerrada!')
