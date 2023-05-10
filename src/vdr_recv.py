import socket
import asyncio

UDP_IP = "0.0.0.0"  # 수신할 IP 주소를 설정
UDP_PORT = 6501  # 수신할 포트 번호를 설정

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
text = open("./vdr_log/test.log", "wb")

async def start_record_vdr():
    try:
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                # line = data.decode('utf-8')
                text.write(data)
                print('vdr inputted')
                
            except KeyboardInterrupt:
                sock.close()
                break

    except asyncio.CancelledError:
        print('vdr stop')