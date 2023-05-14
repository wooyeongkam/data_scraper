import asyncio

text = open("./vdr_log/test.log", "wb")

async def start_record_vdr(sock):
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