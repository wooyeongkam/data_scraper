from redis import Redis
import io
from PIL import Image
import datetime
import asyncio
import datetime


redis = Redis(host="192.168.0.200", port=30379, db =0)

pubsub_eo = redis.pubsub()
pubsub_ir = redis.pubsub()

pubsub_eo.subscribe("nas:image:eo", timeout=1)
pubsub_ir.subscribe("nas:image:ir", timeout=1)


def get_unix_timestamp():
  utc_now = datetime.datetime.utcnow()
  unix_timestamp = int(utc_now.timestamp())

  return unix_timestamp


def save_image(message, type):
  if message and "data" in message and type(message["data"]) == int:
    image = Image.open(io.BytesIO(message["data"]))
    now = get_unix_timestamp()
    image.save(f"./{type}_img/{now}.jpg")


async def start_record_eo():
  try:
    while True:
      for message in pubsub_eo.listen():
        save_image(message, 'eo')

  except asyncio.CancelledError:
    print('eo stop')


async def start_record_ir():
  try:
    while True:
      for message in pubsub_ir.listen():
        save_image(message, 'ir')

  except asyncio.CancelledError:
    print('ir stop')


async def main():
  task1 = asyncio.create_task(start_record_eo())
  task2 = asyncio.create_task(start_record_ir())
  await asyncio.gather(task1, task2)

loop = asyncio.get_event_loop()

try:
  asyncio.run(main())
except:
  loop.stop()
  loop.close()