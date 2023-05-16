import asyncio
import datetime


def get_unix_timestamp():
  utc_now = datetime.datetime.utcnow()
  unix_timestamp = int(utc_now.timestamp())

  return unix_timestamp


async def start_record_vdr(sock):
    now = get_unix_timestamp()
    text = open(f"./src/vdr_log/{now}.log", "wb")

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

            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print('vdr stop')