import socket
import time

SERVER_IP_ADDRESS = '127.0.0.1'
SERVER_PORT_NO = 8080
ADDR = (SERVER_IP_ADDRESS, SERVER_PORT_NO)
BUFFER_SIZE = 1024
MSG = '1'
ENCODING = 'utf-8'
INTERVAL = 1
PING_COUNT = 20
TIMEOUT = 0.25

udpClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udpClient.settimeout(TIMEOUT)
print('[START] Cliente inicializado...')

timeAux = 0.00
pkgLost = int(0)
for i in range(PING_COUNT):
    try:
        udpClient.sendto(MSG.encode(ENCODING), ADDR)
        t_msg_sent = time.time()
        print(f'Mensagem {i + 1} enviada...')
        udpClient.recv(BUFFER_SIZE)
        t_msg_rcv = time.time()
        print(f'Mensagem {i + 1} retornada em {(t_msg_rcv - t_msg_sent) * 1000: .2f} ms...')
        timeAux += (t_msg_rcv - t_msg_sent) * 1000
    except socket.timeout:
        print(f'[TIMEOUT] Mensagem para {ADDR[0]} perdida')
        pkgLost += 1
    time.sleep(INTERVAL)

udpClient.sendto('!Encerrar'.encode(ENCODING), ADDR)
timeAux /= (PING_COUNT - pkgLost)
print('[END] Cliente encerrado...')
print(f'[RESULT] RTT médio: {timeAux: .1f} ms')
print(f'[RESULT] Perda de pacotes: {(100 * pkgLost / PING_COUNT): .1f} %')
