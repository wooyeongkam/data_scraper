import typer
import asyncio
import socket
from redis import Redis
from img_recv import start_record_eo, start_record_ir
from vdr_recv import start_record_vdr

vdr_ip= "0.0.0.0"
vdr_port= 6501

redis_ip='192.168.0.200'
redis_port= 30379
redis_db= 0

async def main(vdr: bool = True, camera: bool = True, vdr_ip: str = vdr_ip, vdr_port: int = vdr_port, redis_ip: str=redis_ip, redis_port:int=redis_port, redis_db:int = redis_db):
  tasks = []

  if vdr:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((vdr_ip, vdr_port))

    tasks.push(asyncio.create_task(start_record_vdr(sock)))

  if camera:
    redis = Redis(host=redis_ip, port=redis_port, db=redis_db)

    pubsub_eo = redis.pubsub()
    pubsub_ir = redis.pubsub()

    pubsub_eo.subscribe("nas:image:eo", timeout=1)
    pubsub_ir.subscribe("nas:image:ir", timeout=1)

    tasks.push(asyncio.create_task(start_record_eo(pubsub_eo)))
    tasks.push(asyncio.create_task(start_record_ir(pubsub_ir)))

  await asyncio.gather(*tasks)


if __name__ == "__main__":
  loop = asyncio.get_event_loop()

  try:
    asyncio.run(typer.run(main))
  except:
    loop.stop()
    loop.close()
