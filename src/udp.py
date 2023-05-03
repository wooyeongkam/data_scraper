import socket

UDP_IP = "192.168.0.200"  # 수신할 IP 주소를 설정
UDP_PORT = 6501  # 수신할 포트 번호를 설정

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
text = open("./test.log", "w")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        line = data.decode('utf-8')
        text.write(line)
        
    except KeyboardInterrupt:
        sock.close()
        break