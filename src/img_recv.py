import io
from PIL import Image
import datetime
import asyncio


def get_unix_timestamp():
  utc_now = datetime.datetime.utcnow()
  unix_timestamp = int(utc_now.timestamp())

  return unix_timestamp


def save_image(message, camera_type):
  if message and "data" in message and type(message["data"]) != int:
    image = Image.open(io.BytesIO(message["data"]))
    now = get_unix_timestamp()
    image.save(f"./src/{camera_type}_img/{now}.jpg")


async def start_record_eo(pubsub_eo):
  try:
    while True:
      for message in pubsub_eo.listen():
        save_image(message, 'eo')

        await asyncio.sleep(0.001)

  except asyncio.CancelledError:
    print('eo stop')


async def start_record_ir(pubsub_ir):
  try:
    while True:
      for message in pubsub_ir.listen():
        save_image(message, 'ir')

        await asyncio.sleep(0.001)

  except asyncio.CancelledError:
    print('ir stop')
